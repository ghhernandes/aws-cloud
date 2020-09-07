# This script is triggered by AWS S3 bucket
# event => S3 PUT/POST JSON


import json
import boto3

def lambda_handler(event, context):
    # Get POST/PUT with files path. Format => (bucket, key)
    files = [(e['s3']['bucket']['name'],e['s3']['object']['key']) for e in event['Records']]
    
    # this lambda function needs S3 and Comprehend IAM role 
    s3 = boto3.client('s3')
    comprehend = boto3.client('comprehend')

    # TODO: change to use this => batch_detect_sentiment()
    for bucket, key in files:
        obj = s3.get_object(Bucket=bucket,Key=key)
        
        # get data and convert binary => str utf8
        data = obj['Body'].read().decode("utf-8") 

        # this case use pt language
        sentiment = comprehend.detect_sentiment(Text=data, LanguageCode='pt')
        
        print(sentiment)
    return {
        'statusCode': 200,
        'body': json.dumps(sentiment)
    }
