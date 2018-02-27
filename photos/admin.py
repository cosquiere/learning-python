# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# This file is necesary for showing the apps model in the django admin
from photos.models import Photo

admin.site.register(Photo)

