from django.db import models
from django.utils import timezone


class Album(models.Model):
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title


class News(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=200)
    news_file = models.FileField()
    news_text = models.TextField()

    def __str__(self):
        return self.news_title
