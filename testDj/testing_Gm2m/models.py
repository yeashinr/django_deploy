from django.db import models

# Create your models here.

class portlist(models.Model):
    service = models.CharField(max_length=50)

class internalapp(models.Model):
    appName = models.CharField(max_length=100)

class externalapp(models.Model):
    exappName =  models.CharField(max_length=100)