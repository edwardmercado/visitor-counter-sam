import json
import boto3
from decimal import Decimal

Table_Name = 'visitor-count-table'

client = boto3.resource('dynamodb')
table = client.Table(Table_Name)

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    #Atomic updates on our current_counter
    updateValue = table.update_item(
        Key={
            'website_id': '12345'
        },
        UpdateExpression = "set current_counter = current_counter + :val",
        ExpressionAttributeValues={
            ':val': Decimal(1)
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
        "body": json.dumps(updateValue,cls=DecimalEncoder)
    };
    
