from kafka import KafkaConsumer
import sys

from kafka.consumer import group

bootstrap_servers = ['localhost:9092']
consumer = KafkaConsumer('Stock2',bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest',group_id = None)

sys.stdout=open("StockData1.txt","w")
for message in consumer:
    values = message.value
    print(values)

sys.stdout.close()    