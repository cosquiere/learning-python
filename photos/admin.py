# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# This file is necesary for showing the apps model in the django admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    def owner_name(self, obj):
        return obj.owner.first_name + u' ' + obj.owner.last_name

    owner_name.short_description = u' Photo owner'  # Cabecera columna
    owner_name.admin_order_field = 'owner'  # Order by

    fieldsets = (
        (None,{
            'fields' : ('name',),   #Commas de las tuplas
            'classes' : ('wide',)
        }), #Tupla
        ('Description and author',{
            'fields' : ('description','owner'),
            'classes': ('wide',)
        }),
        ('Extra',{
            'fields':('url','license','visibility'),
            'classes':('wide','collapse')
        })
    )


admin.site.register(Photo, PhotoAdmin)
