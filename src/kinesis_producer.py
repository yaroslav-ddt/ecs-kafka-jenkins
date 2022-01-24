import boto3
import json
import logging
import time

logging.basicConfig(level = logging.INFO)

session = boto3.Session(region_name='eu-west-1')
client = session.client('kinesis')

test_data = {'gamer_tag': 'JoeGamer', 'score': '100', 'character': 'Flame Warrior'}

for x in range(100):
	response = client.put_record(
	  StreamName='YourGamerDataStream',
	  Data=json.dumps({
		"gamer_tag":  test_data['gamer_tag'],
		"score":      x,
		"character":  test_data['character']
	  }),
	  PartitionKey='a01'
	)
	time.sleep(2)
  
logging.info("Input New Gamer Score: %s", test_data)
