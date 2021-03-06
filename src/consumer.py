from kafka import KafkaConsumer
from json import loads
consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['kafka.test.yy:9093'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
for message in consumer:
    message = message.value
    print('new message in topic {}'.format(message))
