__author__ = 'pridemai'
from django.db import models

class VirtualMachine(models.Model):
    filename=models.CharField(max_length=70)
    display_name=models.CharField(max_length=50)

    def __unicode__(self):
        return self.display_name