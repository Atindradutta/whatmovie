# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.template import RequestContext
from django.http import HttpResponse

from movie_site.models import Movie,slide,bollywoodone,tollywoodtwo,hollywoodthree,upcomingone,upcomingtwo,toprating
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
   all_slide=slide.objects.all()
   all_upcomingone=upcomingone.objects.all()
   all_upcomingtwo=upcomingtwo.objects.all()
   all_toprating=toprating.objects.all()

   context={
	   'movies':movies,
	   'all_slide':all_slide,
	   'all_upcomingone':all_upcomingone,
	   'all_upcomingtwo':all_upcomingtwo,
	   'all_toprating':all_toprating
   }	
   return render(request,'movie/home.html',context)

def bollywood(request):
	all_bollywood=bollywoodone.objects.all()
	all_slide=slide.objects.all()
	context={
		'all_bollywood':all_bollywood,
		'all_slide':all_slide
   }	
	return render(request,'movie/bollywood.html',context)


def hollywood(request):
	all_hollywood=hollywoodthree.objects.all()
	all_slide=slide.objects.all()
	context={
		'all_slide':all_slide,
		'all_hollywood':all_hollywood
	}	
	return render(request,'movie/hollywood.html',context)


def tollywood(request):
	all_tollywood=tollywoodtwo.objects.all()
	all_slide=slide.objects.all()
	context={
		'all_slide':all_slide,
		'all_tollywood':all_tollywood
	}
	return render(request,'movie/tollywood.html',context)
def player(request):
	movies = Movie.objects.all()
	return render(request,'movie/player.html',{'movies':movies})


