# -*- coding: utf-8 -*-

from django import forms
from photos.settings import BADWORDS
from photos.models import Photo
from django.core.exceptions import ValidationError


class PhotoForm(forms.ModelForm):


    class Meta:
        model = Photo
        exclude = ['owner']


    def clean(self):
        """
        Validate if badwords are write on description
        :return: dic with atrr if OK
        """

        #Calling tu super class
        #Recover cleaned data from form
        cleaned_data = super(PhotoForm,self).clean()


        description = cleaned_data.get('description','')


        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError(u'The word {0} is not allowed'.format(badword))


        #If all its ok, return cleaned_data
        return cleaned_data