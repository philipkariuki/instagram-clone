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
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'userposts/', blank=True)


    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.image_name

    def delete_image(self):
        self.delete()       

    def save_image(self):
        self.save()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images



    @classmethod
    def search_by_image_name(cls,search_term):
        photos = cls.objects.filter(image_name__icontains=search_term)
        return photos


class Profile(models.Model):
	profile_name = models.CharField(max_length =260)
	bio = models.CharField(max_length =260)
	profile_photo = models.ImageField(upload_to = 'profilepics/', blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.bio

	@classmethod
	def get_profile(cls):
		profile = cls.objects.all()
		return profile

	def save_profile(self):
		self.save()