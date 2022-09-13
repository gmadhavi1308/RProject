from django.db import models
class Album(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=40)
    writer = models.CharField(max_length=30)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

# Create your models here.
