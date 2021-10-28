from kafka import KafkaConsumer
import sys
import json
import os

from kafka.consumer import group

from dotenv import load_dotenv
load_dotenv('.env')

key = os.getenv('bootstrap_servers')
consumer = KafkaConsumer('Stock2',auto_offset_reset = 'earliest',group_id = None)

sys.stdout=open('StockData2.txt','w')
for message in consumer:
    values = message.value
    print(values)

sys.stdout.close()    