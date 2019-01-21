# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie,slide,bollywoodone,hollywoodthree,tollywoodtwo,upcomingone,upcomingtwo,toprating,contact


admin.site.register(Movie)
admin.site.register(slide)
admin.site.register(bollywoodone)
admin.site.register(hollywoodthree)
admin.site.register(tollywoodtwo)
admin.site.register(upcomingone)
admin.site.register(upcomingtwo)
admin.site.register(toprating)
admin.site.register(contact)

