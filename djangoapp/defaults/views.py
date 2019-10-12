from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .forms import SignUpForm,ContactForm

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
