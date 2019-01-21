# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.template import RequestContext
from django.http import HttpResponse

from movie_site.models import Movie,slide,bollywoodone,tollywoodtwo,hollywoodthree,upcomingone,upcomingtwo,toprating,contact
from django.template.context_processors import csrf
from django.db.models import Q 
import re
from. forms import ContactForm

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
				login(requests)
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
			login(user)
			request.session['user']=username
			movies=Movie.objects.all()
			return render(request,'movie/register.html',{'movies':movies})
                  
   return render(request,'movie/register.html')


def log_out(request):
	if 'user' in request.session:
		del request.session['user']
		logout(request)
		return redirect('logged_in')	




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


def contact(request):
	form_class = ContactForm
	if request.method == "POST":
		form = form_class(request.POST)
		
		if form.is_valid():
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('first_name')
			email = request.POST.get('email')
			message = request.POST.get('message')
			
			send_mail('Subject here', message, email, ['atindradutta9.com'], fail_silently=False)
			return HttpResponseRedirect('movie/contact.html')
		
	return render(request, 'movie/contact.html')





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

