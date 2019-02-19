# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slugify import slugify 
from django.contrib.auth.models import User


class SourceProduct(object):
    BOLLYWOOD = 1
    HOLLYWOOD = 2
    TOLLYWOOD = 3
    TOPRATING = 4


class Movie(models.Model):
    MOVIE_CATAGORIES = (
    (SourceProduct.BOLLYWOOD, "Bollywood"),
    (SourceProduct.HOLLYWOOD, "Hollywood"),
    (SourceProduct.TOLLYWOOD, "Tollywood"),
    (SourceProduct.TOPRATING, "Toprating"),
)
    name = models.CharField(null=True,max_length=40, unique=True)
    description = models.CharField(null=True,max_length=100)
    date =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    duration = models.DurationField(null=True,blank=True)
    picture = models.ImageField(upload_to='static',null=True,blank=True)
    path=models.CharField(max_length=100,null=True)
    catagory = models.IntegerField(blank=True, null=True, choices=MOVIE_CATAGORIES, default=None)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.name)
	super(Movie,self).save(*args,**kwargs)

    def __str__(self):
	return self.name
    
class slide(models.Model):
    images = models.ImageField(upload_to='static',null=True,blank=True)



class upcomingtwo(models.Model):
    namefive = models.CharField(null=True,max_length=40, unique=True)
    descriptionfive = models.CharField(null=True,max_length=100)
    datefive =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    picturefive = models.ImageField(upload_to='static',null=True,blank=True)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.namefive)
	super(upcomingtwo,self).save(*args,**kwargs)

    def __str__(self):
	return self.namefive    


class contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
	return self.first_name