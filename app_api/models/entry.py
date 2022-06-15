from django.db import models

class Entry(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=8000)
    is_public = models.BooleanField()
    techtag = models.ForeignKey('Techtag', on_delete=models.CASCADE)
    moodtag = models.ForeignKey('Moodtag', on_delete=models.CASCADE)
    developer = models.ForeignKey("Developer", 
            on_delete=models.CASCADE, related_name='developer')