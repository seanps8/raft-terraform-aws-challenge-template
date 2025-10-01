import json
import boto3
import pymysql
import os
import gzip
import csv

s3_client = boto3.client('s3')
rds_host = os.environ['RDS_HOST']
db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']

def lambda_handler(event, context):
    if 'Records' in event and event['Records'][0]['eventSource'] == 'aws:s3':
        return handle_s3_event(event)
    else:
        return handle_api_request(event)


# Complete the functions below in order to handle the S3 event and API request. You can add additional helper functions as needed.
# The S3 event handler should read the uploaded gzip CSV file, parse its contents, and insert the data into the RDS MySQL database.
# Larger files should be processed in chunks to avoid memory issues.
# The API request handler should query the RDS MySQL database and return the results as a JSON response.
# You will need to use the pymysql library to connect to your RDS instance and the boto3 library to interact with S3.
# Note: The SQL commands in modules/storage/README.md may be useful.


def handle_s3_event(event):


def handle_api_request(event):
