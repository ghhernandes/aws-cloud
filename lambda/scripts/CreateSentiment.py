# Generate sentiment analysis of lambda inputs

import json
import boto3

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')
    sentiment = comprehend.batch_detect_sentiment(
            TextList=event['text'],
            LanguageCode='pt')

    return {
            'statusCode': 200,
            'body': json.dumps(sentiment)
    }
