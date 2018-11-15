# S3-To-DynamoDB-AWS-Lambda-Function
An AWS Lambda function which gets triggered whenever a new file gets uploaded to an S3 bucket and then uploads the data to a DynamoDB table

#### Please note that this project is created as a next step for [Twitter HashTag Streamer Project](https://github.com/varunu28/Twitter-HashTag-Streamer). The demo is an extention with the same

![Demo](demo.gif)

## Steps to run
 - Create a Lambda function in AWS Management Console. 
 - Assign a role to the Lambda function and make sure it has read access for S3 and write access for DynamoDB
 - You can reconfigure the code to append it to your project flow. See the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html) for more details.
 - You can remove the print statements which were for debugging purposes. If you want to see the log messages then you would also have to grant access for the CloudWatch to the lambda function
 
 Feel free to open an Issue/PR to report bugs/extensions
