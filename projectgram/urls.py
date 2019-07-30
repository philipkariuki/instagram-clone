"""projectgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views

from registration.backends.simple.views import RegistrationView

class RegView(RegistrationView):
    def get_success_url(self, user):
        success_url =  '/' 
        return success_url



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^',include('instaclone.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', RegView.as_view(), name='registration_register'),
    url(r'^logout/$', views.logout, {"next_page": '/'})
]
