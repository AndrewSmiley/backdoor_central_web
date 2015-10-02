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
from django.contrib.auth.forms import PasswordResetForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def authenticate(request):
    return render(request, 'login.html')