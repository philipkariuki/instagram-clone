from django.contrib import admin
from .models import Uzer

# Register your models here.

class UzerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Uzer)

