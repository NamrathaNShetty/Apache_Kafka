from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'MyTest'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

ack = producer.send(topicName, b'Hello Shobhith')
ack = producer.send(topicName, b'Namratha here')
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)


