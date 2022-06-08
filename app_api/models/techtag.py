from django.db import models

class Techtag(models.Model):
    tech_title = models.CharField(max_length=25)