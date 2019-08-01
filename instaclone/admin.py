from django.contrib import admin
from .models import Image, tags, Profile

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Image, ImageAdmin)
admin.site.register(tags)
admin.site.register(Profile)