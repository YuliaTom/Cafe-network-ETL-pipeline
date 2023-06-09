import json
import boto3
import pandas as pd
import handler

s3 = boto3.client('s3')


def lambda_handler(event, contex=None):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        fieldnames = ['timestamp', 'store', 'customer_name',
                      'basket_items', 'total_price', 'cash_or_card', 'card_number']
        df = pd.read_csv(response["Body"], names=fieldnames)
    except Exception as e:
        print(e)
        print(
            f"Error getting object {key} from bucket {bucket}. Make sure they exist and your bucket is in the same region as this function.")
        raise e
    print(key)
    handler.main(df)
