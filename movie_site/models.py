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
