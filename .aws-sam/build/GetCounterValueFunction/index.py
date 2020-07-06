import json
import boto3
from decimal import Decimal

Table_Name = 'visitor-count-table'

client = boto3.resource('dynamodb')
table = client.Table(Table_Name)

def lambda_handler(event, context):
    response = table.put_item(
        Item={
            'website_id': '12345',
            'current_counter': 1
        }  
    )