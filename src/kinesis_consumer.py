import boto3
import json
import sys
import logging

logging.basicConfig(level = logging.INFO)

session = boto3.Session(region_name='eu-west-1')
client = session.client('kinesis')

aws_kinesis_stream = client.describe_stream(StreamName='YourGamerDataStream')

shard_id = aws_kinesis_stream['StreamDescription']['Shards'][0]['ShardId']

stream_response = client.get_shard_iterator(
    StreamName='YourGamerDataStream',
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)

iterator = stream_response['ShardIterator']

while True:
  try:
    aws_kinesis_response = client.get_records(ShardIterator=iterator, Limit=5)
    iterator = aws_kinesis_response['NextShardIterator']
    for record in aws_kinesis_response['Records']:
        if 'Data' in record and len(record['Data']) > 0:
          logging.info("Received New Gamer Score: %s", json.loads(record['Data']))
  except KeyboardInterrupt:
    sys.exit()
