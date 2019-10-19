from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .forms import SignUpForm, ContactForm, PostForm

from django.core.signals import request_finished
from django.dispatch import receiver

from django.db.models import Q
from .models import blog, post

# Create your views here.
def home(request):
	return render(request, 'home.html', {'title': 'Site'})
	
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(data = request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Account created successfully')
			auth_login(request, user)
			return redirect('signup')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'title' : 'Signup','form': form})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(data = request.POST)
		if form.is_valid:
			contact = form.save()
			messages.success(request, 'Form Submitted Successfully!')
			return redirect('contact')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'title': 'Contact','form': form})

@receiver(request_finished)
def post_contact_receiver(sender, **kwargs):
	print("Someone contacted from views!")
	
def search(request):
	if request.method == 'POST':
		srch = request.POST['srh']
		print(srch)
		if srch:
			match = blog.objects.filter(Q(title__icontains=srch)|Q(tag__icontains=srch))
			#title__istartswith, title__iendswith, title__iexact, title__exact
			if match:
				return render(request, 'search.html', {'sr':match})
			else:
				messages.error(request, 'No result found!')
	return render(request, 'search.html', {'title':'Search'})
	
def posts(request):
	if request.method == "POST":  
		form = PostForm(data = request.POST)
		if form.is_valid():  
			try:
				post = form.save()
				messages.success(request, 'Form Submitted Successfully!')
				return redirect('posts')
			except:
				pass
	else:  
		form = PostForm()
	return render(request, 'posts.html', {'title' : 'Add Posts','form':form})
	
def allposts(request):
	posts = post.objects.all()
	return render(request, 'allposts.html', {'title' : 'All Posts','allposts':posts})
	
def postupdate(request, id):
	Posts = post.objects.get(id=id)
	form = PostForm(request.POST or None, instance=Posts)
	if form.is_valid():
		#instance = form.save(commit=False)
		form.save()
		return redirect('allposts')
	return render(request, 'posts.html', {'title' : 'Edit Posts','form':form,'Posts':Posts})
	
def postdelete(request, id):
	Post = post.objects.get(id=id)
	if Post:
		Post.delete()
		return redirect('allposts')
	return render(request, 'posts.html')