# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.db.models import Q

from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC

# Create your views here.


class PhotosQuerySet(object):

    @staticmethod
    def get_photos_queryset(request):
        if not request.user.is_authenticated():
            photos_list = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos_list = Photo.objects.all()
        else:
            photos_list = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos_list
        #Esto no devuelve una lista de objectos, devuelve una query configurada.
        #Django no dispara la query hasta que no sea necesario por eso es posible
        #Continuar añadiendo .filter y etc en DetailView por ejemplo.

class HomeView(View):


    def get(self,request):
        """
        This function show all photos on the main page.
        """
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            'photos_list': photos[:6]
        }

        return render(request, 'photos/home.html', context)

class DetailView(View):

    def get(self,request, pk):
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

        # TODO research select_related
        photo = PhotosQuerySet.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        photo = photo[0] if len(photo) == 1 else None

        if photo is not None:
            # Load photo detail view
            context = {
                'photo': photo
            }

            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound()

class OnlyAuthenticatedView(View):

    def get(self,request):
        if request.user.is_authenticated():
            return super(OnlyAuthenticatedView,self).get(request)
        else:
            return HttpResponseNotFound('Photo doesnt exist!') #Error 404

class CreateView(View):
    """
    Show a form for create a new photo post.
    :param request: HttpRequest Object
    :return: HttpResponse Object
    """

    @method_decorator(login_required())
    def get(self,request):
        form = PhotoForm()
        context = dict(form=form)
        return render(request, 'photos/new_photo.html', context)

    @method_decorator(login_required())
    def post(self,request):
        success_message = ''
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


class ListView(View):


    def get(self,request):
        """
        Return
            - Public photos is user is not authenticated
            - User photos and publics is user is authenticated
            - Publics and not publics is user is a superuser
        :param request: HttpRequest
        :return: HttpResponse
        """

        context = dict(photos_list=PhotosQuerySet.get_photos_queryset(request))

        return render(request,'photos/photos_list.html',context)

#Otra forma de hacer PhotosQuerySet es con multiherencia
#
# def get_photos_queryset(self,request):
# ...
#
# class ListView(View,PhotosQuerySet)
# ....
# context = dict(photos_list=self.get_photos_queryset(request))






































