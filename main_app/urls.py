#handles all the urls for our main app
from django.urls import path
from . import views

urlpatterns = [  # create a list to handle all the paths
    path('', views.index, name='index'), # when we hit the home route it will run the http response of views.index
    path('about/', views.about, name='about') #specify the path

]