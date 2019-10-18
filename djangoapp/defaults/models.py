from django.db import models
from datetime import datetime

from django.db.models.signals import post_save, pre_save, post_delete


COLOR_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FEATURED = [
	(0, 'No'),
	(1, 'Everwhere'),
	(2, 'Category-only')
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
	featured = models.IntegerField(choices = FEATURED, default=0)
	
	def __str__(self):
		return format(self.title)
		
class contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, blank=True)
	address = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return format(self.name)
		
#Receiver of the signal
# sender is the model that we send signal to, instance is the model instance
def sig_post_contact(sender, instance, **kwargs):
	print("Someone contacted!")
	
def sig_pre_contact(sender, instance, **kwargs):
	print("Before executing save contacted!")
	
def sig_after_delete_contact(sender, instance, **kwargs):
	print("Deleted contacted!")

# link the receiver to the actual signal
# connect is the method that you pass to attach the receiver
# connect syntax -- connect(self, receiver, sender=None, weak=True, dispatch_uid=None)
pre_save.connect(sig_pre_contact, sender=contact)

post_save.connect(sig_post_contact, sender=contact)

post_delete.connect(sig_after_delete_contact, sender=contact)