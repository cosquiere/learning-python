# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login


# Create your views here.
from users.forms import LoginForm


def login(request):
    form = LoginForm()
    error_messages = []
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pwd')  # get('key','default_value')

        user = authenticate(username=username, password=password)

        if user is None:
            error_messages.append('Username or password incorrect')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('home')
            else:
                error_messages.append('The user is not active')

    context = dict(errors=error_messages, login_form=form)
    return render(request, 'users/login.html', context)


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('home')
