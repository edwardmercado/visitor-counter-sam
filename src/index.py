import json
import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key

client = boto3.resource('dynamodb')
table = client.Table('visitor-count-table')

def lambda_handler(event, context):
    response = table.put_item(
        Item={
            'website_id': '12345',
            'current_counter': 1
        }  
    )