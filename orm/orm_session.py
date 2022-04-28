import sqlalchemy.orm
from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy import create_engine
from sensors import SENSORS
from workplaces import WORKPLACE_TYPES, WORKPLACES
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DMIS_RECORDINGS_DB_PATH = "postgresql://dmis_dbuser:dmis_dbpassword@energy.uni-passau.de:5432/dmis_recordings_db"
WORKPLACE_ENUM_TABLE_NAME = "workplaceType"
SENSOR_TO_WORKPLACE_TABLE_NAME = "sensorToWorkplace"
SENSOR_TO_DEVICETYPE_TABLE_NAME = "sensorToDeviceType"

class SensorToWorkplace(Base):
    __tablename__ = SENSOR_TO_WORKPLACE_TABLE_NAME
    sensorID = Column(Integer, ForeignKey('sensors.id'))
    workplaceID = Column(Integer, ForeignKey('workplace.id'))

class SensorToDeviceGroup(Base):
    __tablename__ = SENSOR_TO_DEVICETYPE_TABLE_NAME
    sensorID = Column(Integer, ForeignKey('sensors.id'))
    deviceTypeID = Column(Integer, ForeignKey('deviceType.id'))

metadata = MetaData()



if __name__ == '__main__':

    engine = create_engine(
        DMIS_RECORDINGS_DB_PATH,
        echo=False)

    Session = sqlalchemy.orm.sessionmaker(bind=engine)

    session = Session()

    # insert sensors
    for sensor in SENSORS:
        session.add(sensor)

    #insert workplaces and types
    for wtype in WORKPLACE_TYPES:
        session.add(wtype)

    for place in WORKPLACES:
        session.add(place)








"JSON Mapping:" \
"sensormapping:{" \
"    sensor:{" \
"       name: 'Stromsensor1-BLADL-02-005'," \
"       ip: '192.168.188.100'," \
"       domain: 'stromsensor1'}," \
"    sensor:{" \
"       name: 'Stromsensor2-BLADL-02-006'," \
"       ip: '192.168.188.101'," \
"       domain: 'stromsensor2'}," \
"   sensor:{" \
"       name: 'Stromsensor3-BLADL-02-007'," \
"       ip: '192.168.188.102'," \
"       domain: 'stromsensor3'}," \
"   sensor:{" \
"       name: 'Stromsensor4-BLADL-02-008'," \
"       ip: '192.168.188.103'," \
"       domain: 'stromsensor4'}," \
"   sensor:{" \
"       name: 'Stromsensor5-BLADL-02-009'," \
"       ip: '192.168.188.104'," \
"       domain: 'stromsensor5'}," \
"   sensor:{" \
"       name: 'Stromsensor6-BLADL-02-010'," \
"       ip: '192.168.188.105'," \
"       domain: 'stromsensor6'}," \
"   sensor:{" \
"       name: 'Stromsensor7-BLADL-02-004'," \
"       ip: '192.168.188.106'," \
"       domain: 'stromsensor7'}," \ 
"   sensor:{" \
"       name: 'Stromsensor8-BLADL-03-009'," \
"       ip: '192.168.188.107'," \
"       domain: 'stromsensor8'}," \
"   sensor:{" \
"       name: 'Stromsensor9-BLADL-03-002'," \
"       ip: '192.168.188.108'," \
"       domain: 'stromsensor9'}," \
"   sensor:{" \
"       name: 'Stromsensor10-BLADL-03-001'," \
"       ip: '192.168.188.109'," \
"       domain: 'stromsensor10'}," \
"   sensor:{" \
"       name: 'Stromsensor11-BLADL-03-003'," \
"       ip: '192.168.188.110'," \
"       domain: 'stromsensor11'}," \
"   sensor:{" \
"       name: 'Stromsensor12-BLADL-03-004'," \
"       ip: '192.168.188.111'," \
"       domain: 'stromsensor12'}," \
"   sensor:{" \
"       name: 'Stromsensor13-BLADL-03-005'," \
"       ip: '192.168.188.112'," \
"       domain: 'stromsensor13'}," \
"   sensor:{" \
"       name: 'Stromsensor14-BLADL-03-007'," \
"       ip: '192.168.188.113'," \
"       domain: 'stromsensor14'}," \
"   sensor:{" \
"       name: 'Stromsensor15-BLADL-04-010'," \
"       ip: '192.168.188.114'," \
"       domain: 'stromsensor15'}," \
"   sensor:{" \
"       name: 'Stromsensor16-BLADL-04-009'," \
"       ip: '192.168.188.115'," \
"       domain: 'stromsensor16'}," \
"   sensor:{" \
"       name: 'Stromsensor17-BLADL-01-002'," \
"       ip: '192.168.188.116'," \
"       domain: 'stromsensor17'}," \
"   sensor:{" \
"       name: 'Stromsensor18-BLADL-01-003'," \
"       ip: '192.168.188.117'," \
"       domain: 'stromsensor18'}," \
"   sensor:{" \
"       name: 'Stromsensor19-BLADL-03-006'," \
"       ip: '192.168.188.118'," \
"       domain: 'stromsensor19'}," \
"   sensor:{" \
"       name: 'Stromsensor20-BLADL-04-001'," \
"       ip: '192.168.188.119'," \
"       domain: 'stromsensor20'}," \
"   sensor:{" \
"       name: 'Stromsensor21-BLADL-01-001'," \
"       ip: '192.168.188.120'," \
"       domain: 'stromsensor21'}," \
"   sensor:{" \
"       name: 'Stromsensor22-BLADL-02-003'," \
"       ip: '192.168.188.121'," \
"       domain: 'stromsensor20'}," \
"   sensor:{" \
"       name: 'Stromsensor23-BLADL-02-002'," \
"       ip: '192.168.188.122'," \
"       domain: 'stromsensor23'}," \
"   sensor:{" \
"       name: 'Stromsensor24-BLADL-02-001'," \
"       ip: '192.168.188.123'," \
"       domain: 'stromsensor24'}," \
"   sensor:{" \
"       name: 'Stromsensor25-BLADL-03-010'," \
"       ip: '192.168.188.124'," \
"       domain: 'stromsensor25'}," \
"   sensor:{" \
"       name: 'Stromsensor26-BLADL-03-008'," \
"       ip: '192.168.188.125'," \
"       domain: 'stromsensor26'}," \
"   sensor:{" \
"       name: 'Stromsensor27-BLADL-04-008'," \
"       ip: '192.168.188.126'," \
"       domain: 'stromsensor27'}," \
"   sensor:{" \
"       name: 'Stromsensor28'," \
"       ip: '192.168.188.127'," \
"       domain: 'stromsensor28'}," \
"   sensor:{" \
"       name: 'Stromsensor29-BLADL-04-002'," \
"       ip: '192.168.188.128'," \
"       domain: 'stromsensor29'}," \
"   sensor:{" \
"       name: 'Stromsensor30-BLADL-04-003'," \
"       ip: '192.168.188.129'," \
"       domain: 'stromsensor30'}," \
"   sensor:{" \
"       name: 'Stromsensor31-BLADL-04-004'," \
"       ip: '192.168.188.130'," \
"       domain: 'stromsensor31'}," \
"   sensor:{" \
"       name: 'Stromsensor32-BLADL-04-005'," \
"       ip: '192.168.188.131'," \
"       domain: 'stromsensor32'}," \
"   sensor:{" \
"       name: 'Stromsensor33-BLADL-04-007'," \
"       ip: '192.168.188.132'," \
"       domain: 'stromsensor33'}," \
"   sensor:{" \
"       name: 'Stromsensor34-BLADL-01-004'," \
"       ip: '192.168.188.133'," \
"       domain: 'stromsensor34'}," \
"   sensor:{" \
"       name: 'Stromsensor35-BLADL-01-005'," \
"       ip: '192.168.188.134'," \
"       domain: 'stromsensor35'}," \
"   sensor:{" \
"       name: 'Stromsensor36-BLADL-01-006'," \
"       ip: '192.168.188.133'," \
"       domain: 'stromsensor34'}," \
"   sensor:{" \
"       name: 'Stromsensor37-BLADL-01-007'," \
"       ip: '192.168.188.136'," \
"       domain: 'stromsensor37'}," \
"   sensor:{" \
"       name: 'Stromsensor38-BLADL-01-008'," \
"       ip: '192.168.188.137'," \
"       domain: 'stromsensor38'}," \
"   sensor:{" \
"       name: 'Stromsensor39-BLADL-01-009'," \
"       ip: '192.168.188.138'," \
"       domain: 'stromsensor39'}," \
"   sensor:{" \
"       name: 'Stromsensor40-BLADL-01-010'," \
"       ip: '192.168.188.139'," \
"       domain: 'stromsensor40'}," \
"}"



