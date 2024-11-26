import requests
import pandas as pd
from pandas import json_normalize
import boto3
import json
# import fast as pa

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    try:
        print(secret_name)
        response = client.get_secret_value(SecretId=secret_name)      
        # Check if the secret is in 'SecretString'
        
        secret = response['SecretString']
        return json.loads(secret) 
    
    except Exception as e:
        print(f"Error retrieving secret: {str(e)}")
        raise e

def get_commbox_data(base_uri, end_point):
    
    secrets = get_secret('commbox-api-key')
    api_key = secrets.get('api_key')

    header = {
    'Content-Type': "application/json",
    'Authorization': api_key
    } 

    parquet_file = 'data_modified.parquet'
    json_file = 'data_modified.json'

    response = requests.get(base_uri+end_point, headers=header) 
    if response.status_code == 200:
        data = response.json()  # Adjust based on response structure
        df = pd.DataFrame(data)

        info_df = json_normalize(df['data'], max_level = 0)
        df_flattened = pd.concat([df.drop(columns=['data', 'status', 'description']), info_df.drop(columns=['user', 'childs', 'activityLogs'])], axis=1)
        df.to_json(json_file, orient='index')
        df.to_parquet(parquet_file, engine='fastparquet')

        return(data)    
