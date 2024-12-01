from django import forms
from .models import request, Accounts

class accountsform (forms.ModelForm):
    model =  Accounts
    fields = "__all__"

class requestform(forms.ModelForm):
    model =  request
    fields = "__all__"


