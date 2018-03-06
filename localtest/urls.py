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
from photos.views import HomeView,DetailView,CreateView,ListView
from users.views import LoginView,LogoutView





urlpatterns = [

    #Photos
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^photos/new',CreateView.as_view(),name="create_photo"),

    url(r'^photo/(?P<pk>[0-9]+)$',DetailView.as_view(),name='photo_detail'),
    url(r'^photos/$',ListView.as_view(),name="photos_list"),

    # Users
    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout')




]
