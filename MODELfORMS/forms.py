from django import forms
from django.forms import fields
from .models import *

class Myform(forms.ModelForm):
    class Meta:
        model = FORM
        fields = '__all__'