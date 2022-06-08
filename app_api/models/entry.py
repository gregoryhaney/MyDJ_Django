from django.db import models

class Entry(models.Model):
    datetime = models.DateTimeField()
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=8000)
    is_public = models.BooleanField()
    techtag = models.IntegerField()
    moodtag = models.IntegerField()
    developer = models.ForeignKey("Developer", on_delete=models.CASCADE)