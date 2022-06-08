
from django.db import models

class Moodtag(models.Model):
    tag_title = models.CharField(max_length=25)