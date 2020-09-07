import json
import boto3
import tweepy

def lambda_handler(event, context):
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""

    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    response = api.search(q=str(event['hashtag']), count=100, result_type="popular")

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
