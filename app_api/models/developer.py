from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=35)
    nickname = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=75)