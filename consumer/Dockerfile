FROM python:3.7-stretch

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY wait-for-it.sh .
COPY pika_consumer.py .

RUN chmod +x /wait-for-it.sh
RUN /wait-for-it.sh

CMD ["python3", "-u", "./pika_consumer.py"]
