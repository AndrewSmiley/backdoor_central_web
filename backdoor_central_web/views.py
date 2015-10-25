__author__ = 'pridemai'
from django.shortcuts import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.db.models import Q
from django.core import serializers
from django.http import Http404
import threading, Queue
from django.contrib.auth.models import *
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.forms import PasswordResetForm
from functions import *


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html', {"login_form": AuthenticationForm()})


def authenticate(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("index"))
    else:
        user = auth.authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'login.html', {"login_form": AuthenticationForm(), "errors": "User %s does not exist"%(request.POST.get('username', ''))})

def logout(request):
    pass
def virtual_machine_selection(request):
    pass
def start_session_selection(request):
    return render(request, "start_session.html", {"semesters":get_all_semesters()})
def ajax_handler(request, action):
    if action == u'get_virtual_machines_in_semester':
        return HttpResponse(''.join())
    elif action == u'get_vms_in_course':
        return HttpResponse(''.join(list("<option value=\"%s\">%s</option>" % (x.id, x.display_name) for x in get_vms_in_course(request.POST['course_name']))))
    elif action == u'get_courses_in_semester':
        return HttpResponse(''.join(list("<option value=\"%s\">%s</option>" % (x.course_name, x.course_name) for x in get_courses_in_semster(request.POST['semester_name']))))

"""
So here's the big one
In this function, we want to call the esxi web service, create the vm and
get the return data to display to the user
"""
def start_session(request):
    return render(request, "session_details.html", {"data":create_new_clone(request.POST['virtual_machine'])})

# def login_authenticate(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         user = auth.authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
#         if user is not None:
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, 'login.html', {"login_form": AuthenticationForm(), "errors": "User %s does not exist"%(request.POST.get('username', ''))})