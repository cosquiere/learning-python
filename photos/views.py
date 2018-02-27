# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo, PUBLIC


def home(request):
    """
    This function show all photos on the main page.
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photo_list': photos[:5]
    }

    return render(request, 'photos/home.html', context)


def detail(request, pk):
    """
    Load detail photo page
    :param request: HttpRequest
    :param pk: int Id of the photo.
    :return: HttpResponse
    """
    #try:
    #    photo = Photo.objects.filter(pk=pk)
    #except Photo.DoesNotExist:
    #   photo = None
    #except Photo.MultipleObjects:
    #    photo = None
    # Another way to do it

    photo = Photo.objects.filter(pk=pk)
    photo = photo[0] if len(photo) == 1 else None

    if photo is not None:
        # Load photo detail view
        context = {
            'photo': photo
        }

        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound()

    pass
