import json
import time
import zlib
from os import environ

import pika
import sqlalchemy
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.types import BIGINT, String


def dict_key_filter(d_in: dict) -> dict:
    valid_keys = ('DeviceName', 'Unixtime Request', 'Unixtime Reply',
                  'Wechselspannung', 'Wechselspannung', 'Wechselstrom', 'Leistung')
    d_out = {key: d_in[key] for key in valid_keys}
    return d_out


if __name__ == '__main__':
    # We use an environment variable to configure the consumer-container via docker-compose
    if ('BLADL_SETUP_NR' in environ) and ('RABBIT_HOST' in environ):
        bladl_setup_nr = str(environ['BLADL_SETUP_NR'])  # e.g BLADL_01
        rabbit_host = str(environ['RABBIT_HOST'])  # e.g 10.10.10.2
    else:
        bladl_setup_nr = 'BLADL_00'

    time.sleep(3)  # sleep for SQL start

    engine = create_engine(
        'postgresql://dmis_dbuser:dmis_dbpassword@dmis_db-container/dmis_recordings_db',
        echo=False)

    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')  # TODO change username and password
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_qos(prefetch_count=1)

    for method_frame, properties, body in channel.consume('task_queue'):
        body_decompressed = zlib.decompress(body)
        list_of_dicts = json.loads(body_decompressed, encoding='utf-8')
        print("Tag ", method_frame.delivery_tag,
              " Received %0.2f kB %03d Messages" % ((len(body) / 1024), len(list_of_dicts)), flush=True)

        table_dict_lists = {}
        list_of_dicts = [dict_key_filter(d) for d in list_of_dicts]
        # Convert Unixtime from seconds[float] to milliseconds[int] 
        # TODO round() instead of int() ?
        for d in list_of_dicts:
            device_name = d['DeviceName']
            del d['DeviceName']
            if type(d['Unixtime Request']) == float:
                d['Unixtime Request'] = int(d['Unixtime Request'] * 1000)
            if type(d['Unixtime Reply']) == float:
                d['Unixtime Reply'] = int(d['Unixtime Reply'] * 1000)
            try:
                float(d['Wechselspannung']) # check if value is float
                float(d['Leistung'])
                float(d['Wechselstrom'])
                if device_name in table_dict_lists:
                    previous_list = table_dict_lists[device_name]
                    list(previous_list).append(d)
                    table_dict_lists[device_name] = previous_list
                else:
                    table_dict_lists[device_name] = [d]
            except ValueError:
                print("Not a float, ignored")
                continue

        metadata = MetaData()
        recordings_table_dict = {}
        for (listkey, listvalue) in table_dict_lists:
            recordings_table = Table(listkey, metadata,
                                     Column('Unixtime Request', BIGINT, primary_key=True, autoincrement=False),
                                     Column('Unixtime Reply', BIGINT, primary_key=True, autoincrement=False),
                                     Column('Wechselspannung', postgresql.DOUBLE_PRECISION),
                                     Column('Wechselstrom', postgresql.DOUBLE_PRECISION),
                                     Column('Leistung', postgresql.DOUBLE_PRECISION))
            recordings_table_dict[listkey] = recordings_table

        metadata.create_all(engine)

        for (listkey, recordings_table) in recordings_table_dict:
            try:
                # https://docs.sqlalchemy.org/en/13/core/tutorial.html#executing-multiple-statements
                # runs as SQL-transaction
                with engine.begin() as connection:
                    result = connection.execute(recordings_table.insert(), list_of_dicts)
                    assert result
            except sqlalchemy.exc.IntegrityError as e:
                print("sqlalchemy.exc.IntegrityError -> Postgres UPSERT DO_NOTHING")
                print(e)
                with engine.begin() as connection:
                    insert_stmt = insert(table=recordings_table, values=list_of_dicts)
                    do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
                        index_elements=['Unixtime Request', 'Unixtime Reply'])
                    result = connection.execute(do_nothing_stmt)
                    assert result
            except Exception as e:
                channel.basic_nack(method_frame.delivery_tag)
                raise e

            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)

    # Cancel the consumer and return any pending messages
    requeued_messages = channel.cancel()
    print('Requeued %i messages' % requeued_messages)

    # Close the channel and the connection
    channel.close()
    connection.close()
