from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Video
from .tasks import process_video
from boto3.dynamodb.conditions import Key
import boto3
from django.conf import settings
from .forms import VideoUploadForm
import os
from boto3.dynamodb.conditions import Attr


AWS_ACCESS_KEY_ID = 'AKIA5QPZYIHIN2WYKGFJ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION_NAME = 'us-east-2' 

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME
)
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('VideoSubtitles')

def index(request):
    return render(request, 'index.html')


def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            # Use the temporary file path, which is in-memory or temporarily on disk.
            video_path = video.video_file.temporary_file_path()
            # Process the video
            process_video(video_path)

            return render(request, 'videoapp/uploded.html')
    else:
        form = VideoUploadForm()

    return render(request, 'videoapp/upload.html', {'form': form})



def search_videos(request):
    keyword = request.GET.get('q', '').strip().upper()
    matches = []

    if keyword:
        response = table.scan()

        for item in response.get('Items', []):
            subtitles_list = item.get('subtitles', [])
            
            for subtitle_entry in subtitles_list:
                text = subtitle_entry.get('text', '')
                if keyword in text:
                    video_id = item.get('video_id', 'Unknown video_id')
                    timestamp = subtitle_entry.get('timestamp', 'Unknown timestamp')
                    matches.append({'video_id': video_id, 'timestamp': timestamp})
                    break  # Exit loop once a match is found for this video

    # Fetch videos from your Django model (assuming you have such a model).
    matching_video_ids = [match['video_id'] for match in matches]
    matching_videos = Video.objects.filter(video_id__in=matching_video_ids)

    return render(request, 'videoapp/search.html', {'videos': matching_videos, 'matches': matches})








