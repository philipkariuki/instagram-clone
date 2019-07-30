from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^register/',views.register,name ='register'),
    url(r'^new/post$', views.new_post, name='new-post')
]

