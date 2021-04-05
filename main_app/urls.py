#handles all the urls for our main app
from django.urls import path
from . import views

urlpatterns = [  # create a list to handle all the paths
    path('', views.index, name='index'), # when we hit the home route it will run the http response of views.index
    path('home/', views.Home, name='home'), # when we hit the home route it will run the http response of views.index
    path('add_food/', views.add_food, name='add_food'),
    path('profile/',views.ProfilePage,name='profile'),
    path('select_food/',views.select_food,name='select_food'),
    path('update_food/<str:pk>/',views.update_food,name='update_food'),
    path('delete_food/<str:pk>/',views.delete_food,name='delete_food'),
    path('about/', views.about, name='about'), #specify the path
    path('contact/', views.contact, name='contact'),
    path('accounts/signup', views.sign_up, name='sign_up'),
    path('resources', views.resources, name='resources'),
    path('shop', views.shop, name='shop'),
   
]
