from django import forms
from .models import userrequest, useraccounts, Post
from django.contrib.auth.forms import UserCreationForm


class accountsform (forms.ModelForm):
    model =  useraccounts
    fields = "__all__"

class requestform(forms.ModelForm):
    model =  userrequest
    fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= (forms.PasswordInput))



class CustomUserCreationForm(UserCreationForm):
    pass 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'mesage']