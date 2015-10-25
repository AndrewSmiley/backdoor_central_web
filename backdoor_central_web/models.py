__author__ = 'pridemai'
from django.db import models

class Semester(models.Model):
    semester_name = models.CharField(max_length=70,null=False)
    def __unicode__(self):
        return self.semester_name

class Course(models.Model):
    course_name = models.CharField(max_length=70,null=False)
    semester = models.ForeignKey(Semester)
    def __unicode__(self):
        return self.course_name
class VirtualMachine(models.Model):
    filename=models.CharField(max_length=70,null=False)
    display_name=models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return self.display_name

