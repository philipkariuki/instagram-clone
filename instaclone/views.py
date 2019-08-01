from django.shortcuts import render,redirect
from .models import Image, Profile
from .forms import NewImageForm,ProfileForm
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist






# def welcome(request):
#     return render(request, 'index.html')
@login_required(login_url='/accounts/login/')
def welcome(request):
    theposts = Image.get_images()
    return render(request, 'index.html', {'theposts': theposts})


# def register(request):
# 	if request.method == 'POST':
# 		form = UserSignup(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			email = form.cleaned_data['email']
# 			password = form.cleaned_data['password']
# 			user_signup = Uzer.objects.create_user(username, email, password, username = username,email =email)
# 			user_signup.save()

# 			HttpResponseRedirect('welcome')
# 		else:
# 			form = UserSignup()
# 		return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def theposts(request,image_id):
    try:
        theposts = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"theposts":theposts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.profile = current_user
            article.save()
        return redirect('welcome')
    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})





@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form})



# def profile(request,profile_id):
#     try:
#         profile = Profile.objects.get(id = profile_id)
#     except ObjectDoesNotExist:
#         raise Http404()
#     return render(request,"profile.html", {"profile":profile})

def profile(request):
    profile = Profile.get_profile()
    return render(request,"profile.html", {"profile":profile})


def search_results(request):

    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("imagesearch")
        searched_images = Image.search_by_image_name(search_term)
        message = f"{search_term}"
        image = Image.get_images()

        return render(request, 'search.html',{"message":message,"imagess": searched_images, "imgz": image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"imagey":image})


def theimages(request):
    imgs = Image.get_images()
    return render(request,"image.html", {"imgs":imgs})