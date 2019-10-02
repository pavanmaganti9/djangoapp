from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)
		
    def __unicode__(self):
        return str(self.title)