from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    authors = models.ManyToManyField(Author)
# Create your models here.
