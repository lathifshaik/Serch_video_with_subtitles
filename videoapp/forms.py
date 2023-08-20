from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_file']
        widgets = {
            'video_file': forms.FileInput(attrs={'required': True})
        }
