__author__ = 'pridemai'
import os
from models import VirtualMachine, Course, Semester
from constants import *
import requests
def get_virtual_machines_in_semester(semester):
    return VirtualMachine.objects.filter(course__in=Course.objects.filter(semester= Semester.objects.get(semester_name=semester)))


"""
File to upload the vmdk or otherwise file to our VirtualMachine repo
"""
def write_vm_upload(folder, vmfile):
    data = {}
    data['errors'] = []
    try:
        if not os.path.exists(VIRTUAL_MACHINE_REPO+folder):
            os.makedirs(VIRTUAL_MACHINE_REPO+folder)
    except Exception,e:
        data['errors'].append(str(e))

    try:
        with open(VIRTUAL_MACHINE_REPO+folder+"/"+vmfile.name, 'wb+') as destination:
            for chunk in vmfile.chunks():
                destination.write(chunk)
    except Exception,e:
        data['errors'].append(str(e))
    data['result'] = 'True' if len(data['errors']) == 0 else 'False'
    return data
# url(r'^new/(?P<filename>.+)/(?P<folder>.+)/(?P<display_name>.+)/(?P<alternate_id>\d+)/$', 'backdoor_central_esxi.views.new_virtual_machine', name="new_virtual_machine"),
"""
This function creates a new VM record on the ESXI server
"""
def create_new_remote_vm(filename, folder, display_name, alternate_id):
    r = requests.get("%s%s/%s/%s/%s/"%(ESXI_CREATE_VM_RECORD,filename,folder,display_name,alternate_id))
    #return the data as a dict
    import json
    return json.loads(r.text)
"""
 filename=models.CharField(max_length=70,null=False)
    display_name=models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    course = models.ForeignKey(Course)
"""
def create_new_local_vm(filename, display_name, username, password, course):
    vm = VirtualMachine()
    vm.filename = filename
    vm.display_name = display_name
    vm.username = username
    vm.password = password
    vm.course = course

    try:
        vm.save()
        return {'result':'True', 'errors': '', 'alternate_id':str(VirtualMachine.objects.get(filename=filename,display_name=display_name).id) }
    except Exception,e:
        return  {'result': 'True', 'errors':str(e)}