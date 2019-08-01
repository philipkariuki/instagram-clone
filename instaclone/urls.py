from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^post/(\d+)',views.theposts, name='theposts'),
    url(r'^profile/',views.profile,name ='profile'),
    url(r'^updateprofile/',views.update_profile,name ='updateprofile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photoz/',views.theimages,name ='photoz')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)