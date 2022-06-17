from django.db import models

class Techtag(models.Model):
    tech_title = models.CharField(max_length=25)
    
    
    # 'ordering' returns the objects sorted by the
    # tech_title field in alphabetic order.
    # ASC is the default.
    
    class Meta:
        ordering=['tech_title']