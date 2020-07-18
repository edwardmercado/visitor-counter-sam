import json
import os
import boto3
from decimal import Decimal

Table_Name = os.environ['DB_NAME']

client = boto3.resource('dynamodb')
table = client.Table(Table_Name)

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    putItemToDB()
    #Atomic updates on our current_counter
    updateValue = table.update_item(
        Key={
            'website_id': '12345'
        },
        UpdateExpression = "SET current_counter = current_counter + :val",
        ConditionExpression = "attribute_exists(current_counter)",
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return {
        'statusCode' : 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        "body": json.dumps(updateValue, cls=DecimalEncoder)
    };
    
def putItemToDB():
    table.put_item(
        Item={
            'website_id': '12345',
            'current_counter': 0
        },
        ConditionExpression = "attribute_not_exists(current_counter)"
    )
    os.environ['ITEM_CREATED'] = TRUE