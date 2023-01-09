from django import forms
from .models import *
class InputForm(forms.Form):
    search_f=forms.CharField(max_length=255)