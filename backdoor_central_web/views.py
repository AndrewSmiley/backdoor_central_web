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