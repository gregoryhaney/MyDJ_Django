from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=35)
    nickname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=75)
        
    
    # 'ordering' returns the objects sorted by the
    # first_name field in alphabetic order.
    # ASC is the default.
    
    class Meta:
        ordering=['first_name']