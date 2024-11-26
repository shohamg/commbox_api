import pandas as pd
from pandas import json_normalize
import boto3
from utils import *

base_uri = "https://api.commbox.io/"    # base url
end_point = "streams/5247/objects/1407374883872618"  # end point url

parquet_file = "data_modified.parquet"
json_file = "data_modified.json"

def handler(event, context):
    s3_bucket = 'commbox-api'  # Replace with your S3 bucket name
    s3_key_parquet = 'test/data_modified.parquet'   # Path in S3 where the file will be stored
    s3_key_json = 'test/data_modified.json'
    s3_client = boto3.client('s3')
    get_commbox_data(base_uri, end_point)
    s3_client.upload_file(parquet_file, s3_bucket, s3_key_parquet)
    s3_client.upload_file(json_file, s3_bucket, s3_key_json)
    return('success')

if __name__ == '__main__':
    handler('None','None')
