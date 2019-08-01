# from django import forms
# from django.contrib.auth import authenticate
# from instaclone.models import Uzer
# from urllib.request import urlopen
# from random import randint
from django import forms
from .models import Image, tags, Profile




# class UserSignup(forms.Form):
#     username = forms.CharField(label='Username',max_length=30)
#     email = forms.EmailField(label='Email')
#     password = forms.CharField(label='Password',max_length=30)



class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['pub_date']