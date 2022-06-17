from django.db import models

class Entry(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=8000)
    is_public = models.BooleanField()
    techtag = models.ManyToManyField('Techtag')
    moodtag = models.ManyToManyField('Moodtag')
    developer = models.ForeignKey("Developer", 
                on_delete=models.CASCADE, 
                related_name='developer')
    
    
    # 'ordering' returns the objects sorted by the
    # datetime field. Pre-pending the minus sign
    # causes it to be newest date first.
    
    class Meta:
        ordering=['-datetime']