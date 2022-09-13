from django.db import models
class Idproof(models.Model):
    aadharid = models.CharField(max_length=16)
    voterid = models.CharField(max_length=12)

    def __str__(self):
        return self.aadharid

class Person(models.Model):
    name = models.CharField(max_length=40)
    qualification = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    idproof = models.OneToOneField(Idproof,on_delete=models.CASCADE,primary_key=True)
# Create your models here.
