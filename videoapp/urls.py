from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('search/', views.search_videos, name='search_videos'),
    path('',views.index, name='index')
   
]