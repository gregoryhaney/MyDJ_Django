from django.db import models

class Moodtag(models.Model):
    tag_title = models.CharField(max_length=25)
    
    
    # 'ordering' returns the objects sorted by the
    # tag_title field in alphabetic order.
    # ASC is the default.
    
    class Meta:
        ordering=['tag_title']