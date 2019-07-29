from django.db import models

# Create your models here.


class Uzer(models.Model):
    username = models.CharField(max_length =25)
    email = models.CharField(max_length =35)
    password = models.CharField(max_length =35)
    last_login = models.DateTimeField(auto_now=True)
