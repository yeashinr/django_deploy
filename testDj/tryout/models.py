from django.db import models
from datetime import date
from django.forms import ModelForm
# Create your models here.

class portList(models.Model):
    serviceName = models.CharField(max_length=50)

class internalapp(models.Model):
    PERIMETER_DOM = (("ALL","All"),("ECN","ECN"),("GIZ","GIZ"),)

    appGrpNm  = models.CharField('Application Group Name',max_length=100)
    servGrpNm = models.CharField('Service Group Name',max_length=100,null=True)
    perimeter = models.CharField('Perimeter',max_length=10, choices=PERIMETER_DOM, default= "All")
    groupInd  = models.IntegerField('Group Index')
    appGrpFunc= models.CharField('Application Group Function',max_length=100, blank=False, null=True)
    paloApp   = models.CharField('PaloAlto Application',max_length=1000, blank=False, null=True)
    services  = models.CharField('Services',max_length=1000, blank=False, null=True)
    plServConfig = models.CharField('PaloAlto Service Config',max_length=1000, blank=False, null=True)
    plAppConfig  = models.CharField('PaloAlto Application Config',max_length=1000, blank=False, null=True)
    comment   = models.CharField('Comments',max_length=1000, blank=False, null=True)
    createdDt = models.DateField('Creation Date',default=date.today)                             # Automatically set the field to now when the object is first created. 
    ports = models.ManyToManyField(portList,blank=True)

    def __str__(self):
        return self.servGrpNm
class externalapp(models.Model):
    appGrpNm  = models.CharField('Application Group Name',max_length=100)
    servGrpNm = models.CharField('Service Group Name',max_length=100,null=True)
    ports = models.ManyToManyField(portList,blank=True)