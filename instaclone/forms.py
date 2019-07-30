from django import forms
from django.contrib.auth import authenticate
from instaclone.models import Uzer
from urllib.request import urlopen
from random import randint




class UserSignup(forms.Form):
    username = forms.CharField(label='Username',max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',max_length=30)
