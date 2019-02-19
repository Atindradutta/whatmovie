# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
# from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

from django.template import RequestContext
from django.http import HttpResponse

from movie_site.models import Movie,slide,contact,upcomingtwo
from django.template.context_processors import csrf
from django.db.models import Q 
import re
from. forms import ContactForm

def logged_in(request):
	# if request.user.is_authenticated():
	# 	movies = Movie.objects.all()
	# 	return render(request, 'movie/home.html', {'movies': movies})
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if not User.objects.filter(username=username).exists():
			return render(request, 'movie/login.html', {'error_message': 'Please register First'})
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				auth_login(request, user)
				request.session['user']=username
				movies = Movie.objects.all()
				return render(request, 'movie/home.html', {'movies': movies})
			else:
				return render(request, 'movie/login.html', {'error_message': 'Your account has been suspended'})
		return render(request, 'movie/login.html', {'error_message': 'Wrong Credentials'})
	return render(request,'movie/login.html')


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
			auth_login(request,user)
			request.session['user']=username
			movies=Movie.objects.all()
			return render(request,'movie/home.html',{'movies':movies})
                  
   return render(request,'movie/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')	

def home(request):
	movies = Movie.objects.all()
	all_slide=slide.objects.all()
	all_upcomingtwo=upcomingtwo.objects.all()
	all_type_movie = movies.filter(catagory__in=[1, 2, 3, 4])
	all_toprating = movies.filter(catagory=4)
	context={
		'movies':movies,
		'all_type_movie':all_type_movie,
		'all_slide':all_slide,
		'all_upcomingtwo':all_upcomingtwo,
		'all_toprating':all_toprating

    }	
	return render(request,'movie/home.html',context)

def bollywood(request):
	movies = Movie.objects.filter(catagory=1)
	all_slide=slide.objects.all()
	context={
		'all_bollywood':movies,
		'all_slide':all_slide
   }	
	return render(request,'movie/bollywood.html',context)

def hollywood(request):
	movies = Movie.objects.filter(catagory=2)
	all_slide=slide.objects.all()
	context={
		'all_hollywood':movies,
		'all_slide':all_slide
   }	
	return render(request,'movie/hollywood.html',context)


def tollywood(request):
	movies = Movie.objects.filter(catagory=3)
	all_slide=slide.objects.all()
	context={
		'all_tollywood':movies,
		'all_slide':all_slide
   }	
	return render(request,'movie/tollywood.html',context)




def player(request):
	return render(request,'movie/player.html')



def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		
		if form.is_valid():
			form.save()
	else:
		form = ContactForm()
	return render(request, 'movie/contact.html',{'form':form})

def search_movie(request):
	if request.method == 'POST':
	    if not request.POST['search']:
	        return redirect('login')
	    if '-w' in request.POST['search']:
	        Q=re.findall('(.*)\s+-w',request.POST['search'])
	        if not Q:
				movies=Movie.objects.filter(Watched=False)
				return render(request,'main.html',{'movies':movies})
	        else:
				Q=Q[0]
				list1=Movie.objects.filter(name__icontains=Q)
	    else:
			Q=request.POST['search']
			list1=Movie.objects.filter(name__icontains=Q)

	    res=list(set(list1))
	    context={
	        'movies':res,
	    }
	return render(request,'movie/home.html',context)

