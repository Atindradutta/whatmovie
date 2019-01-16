# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.template import RequestContext
from django.http import HttpResponse

from movie_site.models import Movie
from django.template.context_processors import csrf
from django.db.models import Q 

def login(request):
	if 'user' in request.session and request.user.is_authenticated():
		movies = Movie.objects.all()
		return render(request, 'movie/home.html', {'movies': movies})
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if not user.objects.filter(username=username).exists():
			return render(request, 'movie/login.html', {'error_message': 'Please register First'})
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				request.session['user']=username
				movies = Movie.objects.all()
				return render(request, 'movie/home.html', {'movies': movies})
		else:
			return render(request, 'movie/home.html', {'error_message': 'Your account has been suspended'})
	return render(request, 'movie/login.html', {'error_message': 'Wrong Credentials'})

def register(request):
   if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		rep_password = request.POST['rep_password']
		email= request.POST['email']
		if User.objects.filter(email=email).exists():
			return render(request, 'movie/register.html', {'error_message': 'Email already registered'})
		elif User.objects.filter(username=username).exists():
			return render(request, 'movie/register.html', {'error_message': 'User name not available'})
		elif (password != rep_password):
			return render(request, 'movie/register.html', {'error_message': 'Password dont match'})
		else:
			user = User(username=username, email=email)
			user.set_password(password)
			user.save()
			user=authenticate(username=username,password=password)
			login(request,user)
			request.session['user']=username
			movies=Movie.objects.all()
			return render(request,'movie/register.html',{'movies':movies})
                  
   return render(request,'movie/register.html')


def home(request):
   movies = Movie.objects.all()	
   return render(request,'movie/home.html',{'movies':movies})

                
def hollywood(request):
   return render(request,'movie/hollywood.html')

def bollywood(request):
   return render(request,'movie/bollywood.html')

def tollywood(request):
   return render(request,'movie/tollywood.html')

def search(request):
	if request.method=='POST':
		srch = requesty.POST['srh']

		if srch:
			match = student.objects.filter(Q(Name_icontains=srch)|
			                               Q(title_icontains=srch)

										   )
			if match:
				return render(request,'movie/home.html',{'sr':match})
			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('movie/home/')
	return render(request,'movie/home.html')											   