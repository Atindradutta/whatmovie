# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slugify import slugify 
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(null=True,max_length=40, unique=True)
    description = models.CharField(null=True,max_length=100)
    date =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    duration = models.DurationField(null=True,blank=True)
    picture = models.ImageField(upload_to='static',null=True,blank=True)
    Path=models.CharField(max_length=100,null=True)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.name)
	super(Movie,self).save(*args,**kwargs)

    def __str__(self):
	return self.name
    
class slide(models.Model):
    images = models.ImageField(upload_to='static',null=True,blank=True)

class bollywoodone(models.Model):
    nameone = models.CharField(null=True,max_length=40, unique=True)
    descriptionone = models.CharField(null=True,max_length=100)
    dateone =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    durationone = models.DurationField(null=True,blank=True)
    pictureone = models.ImageField(upload_to='static',null=True,blank=True)
    Pathone = models.CharField(max_length=100,null=True)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.nameone)
	super(bollywoodone,self).save(*args,**kwargs)

    def __str__(self):
	return self.nameone

class tollywoodtwo(models.Model):
    nametwo = models.CharField(null=True,max_length=40, unique=True)
    descriptiontwo = models.CharField(null=True,max_length=100)
    datetwo =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    durationtwo = models.DurationField(null=True,blank=True)
    picturetwo = models.ImageField(upload_to='static',null=True,blank=True)
    Pathtwo = models.CharField(max_length=100,null=True)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.nametwo)
	super(tollywoodtwo,self).save(*args,**kwargs)

    def __str__(self):
	return self.nametwo

class hollywoodthree(models.Model):
    namethree = models.CharField(null=True,max_length=40, unique=True)
    descriptionthree = models.CharField(null=True,max_length=100)
    datethree =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    durationthree = models.DurationField(null=True,blank=True)
    picturethree = models.ImageField(upload_to='static',null=True,blank=True)
    Paththree = models.CharField(max_length=100,null=True)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.namethree)
	super(hollywoodthree,self).save(*args,**kwargs)

    def __str__(self):
	return self.namethree


class upcomingone(models.Model):
    namefour = models.CharField(null=True,max_length=40, unique=True)
    picturefour = models.ImageField(upload_to='static',null=True,blank=True)

    def save(self,*args,**kwargs):
	self.slug = slugify(self.namefour)
	super(upcomingone,self).save(*args,**kwargs)

    def __str__(self):
	return self.namefour

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

class toprating(models.Model):
    namesix = models.CharField(null=True,max_length=40, unique=True)
    descriptionsix = models.CharField(null=True,max_length=100)
    datesix =  models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    durationsix = models.DurationField(null=True,blank=True)
    picturesix = models.ImageField(upload_to='static',null=True,blank=True)
    Pathsix=models.CharField(max_length=100,null=True)


    def save(self,*args,**kwargs):
	self.slug = slugify(self.namesix)
	super(toprating,self).save(*args,**kwargs)

    def __str__(self):
	return self.namesix


class contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
	return self.first_name



