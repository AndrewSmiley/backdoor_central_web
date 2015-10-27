__author__ = 'pridemai'
from models import Semester, Course,VirtualMachine
import json
import requests
from constants import *
from virtual_machine_functions import write_vm_upload

def get_all_semesters():
    return Semester.objects.all()

def get_all_courses():
    return Course.objects.all()

def get_courses_in_semster(semster_name):
    return Course.objects.filter(semester__in=Semester.objects.filter(semester_name=semster_name))

def get_vms_in_course(course_name):
    return VirtualMachine.objects.filter(course=Course.objects.get(course_name=course_name))

def load_json(json_data):
    return json.loads(json_data)

def create_new_clone(alternate_id):
    #basically send the esxi instance the alternate id
    #of the vm we want to clone
    return load_json(send_clone_request(alternate_id))
    #the local version of this call
    # return load_json(open("static/json/data.json"))
def send_clone_request(alternate_id):
    r = requests.get(ESXI_CLONE_URL+"%s/"%(alternate_id))
    return r.text
def save_vm_file(folder,vmfile):
    return write_vm_upload(folder, vmfile)
    # r = requests.post(ESXI_UPLOAD_VM_URL,data={'folder':folder}, files={vmfile.name: vmfile})
    # return load_json(r.text)