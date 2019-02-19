# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie,slide,contact,upcomingtwo

admin.site.register(Movie)
admin.site.register(slide)
admin.site.register(contact)
admin.site.register(upcomingtwo)


