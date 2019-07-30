from django.shortcuts import render,redirect
from .models import Uzer
from .forms import UserSignup
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView




def welcome(request):
    return render(request, 'index.html')


def register(request):
	if request.method == 'POST':
		form = UserSignup(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user_signup = Uzer.objects.create_user(username, email, password, username = username,email =email)
			user_signup.save()

			HttpResponseRedirect('welcome')
		else:
			form = UserSignup()
		return render(request, 'index.html')


class RegView(RegistrationView):
    def get_success_url(self, user):
        success_url =  '/' 
        return success_url







