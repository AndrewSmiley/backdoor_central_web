__author__ = 'pridemai'
from django.db import models

class VirtualMachine(models.Model):
    filename=models.CharField(max_length=70,null=False)
    display_name=models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    def __unicode__(self):
        return self.display_name