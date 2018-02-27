"""localtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from users import views as users_views
from photos import views as photos_views





urlpatterns = [

    #Photos
    url(r'^admin/', admin.site.urls),
    url(r'^$',photos_views.home,name='home'),

    url(r'^photo/(?P<pk>[0-9]+)$',photos_views.detail,name='photo_detail'),

    # Users
    url(r'^login$', users_views.login, name='user_login'),
    url(r'^logout$', users_views.logout, name='user_logout')


]
