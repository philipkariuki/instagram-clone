from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


# class Uzer(models.Model):
#     username = models.CharField(max_length =25)
#     email = models.CharField(max_length =35)
#     password = models.CharField(max_length =35)
#     last_login = models.DateTimeField(auto_now=True)


class tags(models.Model):
    name = models.CharField(max_length =30)

    def save_tag(self):
        self.save()

    def __str__(self):
        return self.name 


class Image(models.Model):
    image_name = models.CharField(max_length =60)
    caption = HTMLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'userposts/', blank=True)

    def __str__(self):
        return self.image_name