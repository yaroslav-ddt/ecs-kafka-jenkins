from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='kafka.test.yy:9093',
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(10):
    data = {'number' : e}
    producer.send('numtest', value=data)
    print('message sent')
    sleep(5)
