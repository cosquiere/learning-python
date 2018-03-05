# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


def home(request):
    """
    This function show all photos on the main page.
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photo_list': photos[:6]
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


@login_required()
def create(request):
    """
    Show a form for create a new photo post.
    :param request: HttpRequest Object
    :return: HttpResponse Object
    """

    success_message = ''

    if request.method == 'GET': #GET REQUEST
        form = PhotoForm()
    else: #POST REQUEST
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user #Automatic asign user autenticated as owner

        form = PhotoForm(request.POST,instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save() #Save the object photo and return it
            form =  PhotoForm() #Empty form after submitting
            success_message = 'Photo created succesfully'
            success_message += '<a href="{0}">'.format(reverse('photo_detail',args=[new_photo.pk]))
            success_message += 'Take a look'
            success_message += '</a>'
    context = dict(form=form,success_message=success_message)

    return render(request,'photos/new_photo.html',context)

