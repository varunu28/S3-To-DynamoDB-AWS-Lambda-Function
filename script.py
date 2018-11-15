import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    
    if event:
        print("Event: ", event)
        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket='test-bucket-cmpe295', Key=filename)
        file_content = fileObj["Body"].read().decode("utf-8")
        print(file_content)
        
        file_json = json.loads(file_content)
        print(str(file_json["user"]["location"]))
        
        dynamo_db = boto3.resource('dynamodb')
        dynamoTable = dynamo_db.Table('cmpe295A')
        
        dynamoTable.put_item(Item = {
            'id': file_json['id_str'],
            'tweet_date': file_json['created_at'],
            'tweet_text': file_json['text'],
            'tweet_location': str(file_json["user"]["location"])
        })
        
    return "Testing Lambda Function"

