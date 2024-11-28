import requests
import pandas as pd
from pandas import json_normalize
import boto3
import json
import logging
# import fast as pa

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    try:
        response = client.get_secret_value(SecretId=secret_name)      
        # Check if the secret is in 'SecretString'
        
        secret = response['SecretString']
        return json.loads(secret) 
    
    except Exception as error:
        logging.error(F"Error retrieving secret: {error}")
        raise error

def generate_api_header():
    try:
        secrets = get_secret('commbox-api-key')
        api_key = secrets.get('api_key')

        header = {
        'Content-Type': "application/json",
        'Authorization': api_key
        }
        return(header)
    
    except Exception as error:
        logging.error(F"{error}")
        raise error

def get_commbox_data(base_uri, end_point, header, parquet_file, json_file):

    try:
        response = requests.get(base_uri+end_point, headers=header) 
        print(base_uri+end_point)
        if response.status_code == 200:
            data = response.json()  
            df = pd.DataFrame(data)

            # info_df = json_normalize(df['data'], max_level = 0)
            # df_flattened = pd.concat([df.drop(columns=['data', 'status', 'description']), info_df.drop(columns=['user', 'childs', 'activityLogs'])], axis=1)
            df.to_json(json_file, orient='index')
            df.to_parquet(parquet_file, engine='fastparquet')

            return(data)
        print(response)
    except Exception as error:
        logging.error(F"{error}")
        raise error    
