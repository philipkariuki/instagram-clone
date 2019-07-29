from django.shortcuts import render,redirect
from .models import Uzer
from .forms import *
from django.http  import HttpResponse, Http404, HttpResponseRedirect




def welcome(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


