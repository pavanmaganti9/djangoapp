from django.db import models
from datetime import datetime


COLOR_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


# Create your models here.
class blog(models.Model):
	title = models.CharField(max_length=400)
	email = models.EmailField(max_length=50, blank=True)
	tag = models.CharField(max_length=50)
	author = models.CharField(max_length=120)
	color = models.CharField(max_length=6, choices=COLOR_CHOICES)
	#gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
	date = models.DateTimeField(default=datetime.now(), blank=True)
	
	def __str__(self):
		return str(self.title)