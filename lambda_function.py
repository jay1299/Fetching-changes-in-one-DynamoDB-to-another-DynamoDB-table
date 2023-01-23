import json #importing JSON package to be used when inserting data into LambdaToDynamoDB table
import boto3 # importing this AWS SDK for Python
from time import gmtime, strftime  # importing these two packages for date formatting

dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('LambdaToDynamoDB')
date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) # store the current time in a human readable format in the variable "date" 
                                                         # so that when INSERT is performed in Testing table, the time when it was  
                                                         # inserted will be updated in the LambdaToDynamoDB table
def lambda_handler(event, context):
    try:
        for i in event['Records']: #This loop will be checking the "Records" segment for INSERT command
            if i['eventName'] == 'INSERT':
                insert(i)  #Function call
    except Exception as e:
        print(e)
        return "uh oh!"

def insert(i):
    newID = i['dynamodb']['NewImage']['Id']['N'] #Nested data fetching for Id entered in Testing table
    newMessage = i['dynamodb']['NewImage']['Message']['S'] #Nested data fetching for Message entered in Testing table
    table_name.put_item(
        Item={
            'Id':newID,
            'Message':newMessage,
            'Time': date
        })
