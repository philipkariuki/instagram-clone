from django.shortcuts import render,redirect
from .models import Uzer
from .forms import UserSignup
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required





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


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('welcome')
    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})






