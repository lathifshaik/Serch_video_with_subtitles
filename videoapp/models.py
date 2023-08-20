from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=255, primary_key=True, unique=True)
    video_file = models.FileField(upload_to='videos/')
    processed = models.BooleanField(default=False)
