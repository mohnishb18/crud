from django.db import models
from django.conf import settings

# Create your models here.

class Topic(models.Model):
    top_name=models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    category=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.category

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=200)
    ecity=models.CharField(max_length=200)
    esal=models.FloatField()

    def __str__(self):
            return self.ename


class contact(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Credential(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    value=models.CharField(max_length=200)