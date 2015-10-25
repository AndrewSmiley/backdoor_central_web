__author__ = 'pridemai'
from models import Semester, Course,VirtualMachine


def get_all_semesters():
    return Semester.objects.all()

def get_all_courses():
    return Course.objects.all()

def get_courses_in_semster(semster_name):
    return Course.objects.filter(semester__in=Semester.objects.filter(semester_name=semster_name))

def get_vms_in_course(course_name):
    return VirtualMachine.objects.filter(course=Course.objects.get(course_name=course_name))

