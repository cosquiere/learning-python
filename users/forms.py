#-*- coding: utf-8 -*-

from django import forms



class LoginForm(forms.Form):

    usr = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    pwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

