# Generated by Django 4.2.4 on 2023-08-18 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='local_videos/'),
        ),
    ]
