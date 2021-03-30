"""Kcal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# this file is what talks to the manage.py and the settings.py
# i need to import the urls from my main_app.py
from django.contrib import admin
from django.urls import path, include 
#include will allow us to grab another urls file from another folder
#whenever we hit that home route its going to hit urls pattern that is inside of the main app
#
#


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'))
]
