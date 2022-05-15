import json

def lambda_handler(event, context):

    event_body = json.loads(event['body'])

    return {
        "statusCode": 200,
        "body": json.dumps(event_body),
    }
