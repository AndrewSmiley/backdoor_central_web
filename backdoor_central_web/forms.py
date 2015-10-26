__author__ = 'pridemai'
from django.forms import ModelForm
from models import VirtualMachine
class UploadForm(ModelForm):
    class Meta:
        model = VirtualMachine
