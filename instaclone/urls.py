from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.welcome),
    url(r'^register/',views.register),
    url(r'^ajax-sign-up$', views.ajaxsignup),
    url(r'^ajax-login$', views.ajaxlogin)
]

