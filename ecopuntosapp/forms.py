from django import forms
from .models import userrequest, useraccounts
from django.contrib.auth.forms import UserCreationForm


class accountsform (forms.ModelForm):
    model =  useraccounts
    fields = "__all__"

class requestform(forms.ModelForm):
    model =  userrequest
    fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    pass 