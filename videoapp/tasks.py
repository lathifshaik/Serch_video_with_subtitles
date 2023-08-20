from celery import shared_task
import subprocess
import boto3
import os

from time import sleep

AWS_ACCESS_KEY_ID = 'AKIA5QPZYIHIN2WYKGFJ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION_NAME = 'us-east-2'

s3 = boto3.resource('s3', 
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=AWS_REGION_NAME)
dynamodb = boto3.resource('dynamodb', region_name='us-east-2', 
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
table = dynamodb.Table('VideoSubtitles')



def process_video(video_path):
    video_filename = os.path.basename(video_path)
    video_id, _ = os.path.splitext(video_filename)
    
    # Extract subtitles using ccextractor
    output_file = f"{video_id}.srt"
    subprocess.run(['ccextractor', video_path, '-o', output_file])
    
    # Upload video to S3
    s3.Bucket('videoapp-django').upload_file(video_path, f"videos/{video_id}.mp4")

    # Extract keywords from .srt file and store in DynamoDB
    with open(output_file, 'r') as f:
        content = f.read().splitlines()
        subtitles = []
        for index, line in enumerate(content):
            if line.isnumeric() and index + 2 < len(content):
                timestamp = content[index + 1]
                text = content[index + 2]
                subtitle_entry = {
                'timestamp': timestamp,
                'text': text
            }
            subtitles.append(subtitle_entry)

        table.put_item(
            Item={
                'video_id': str(video_id),
                'subtitles': subtitles
                }
            )
    


    os.remove(output_file)  # Removing the generated subtitle file.
    os.remove(video_path)
