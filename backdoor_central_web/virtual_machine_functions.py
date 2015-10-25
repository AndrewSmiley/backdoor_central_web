__author__ = 'pridemai'
from models import *


def get_virtual_machines_in_semester(semester):
    return VirtualMachine.objects.filter(course__in=Course.objects.filter(semester= Semester.objects.get(semester_name=semester)))


