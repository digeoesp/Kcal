from django.shortcuts import render
from django.http import HttpResponse # need this to send a response to the user

# imports
from .models import Food

# Create your views here.
# controller but called views in django
# set them up like functions
# create functions for template files
# return render from our imports 
# django will automatically look for a folder called templates
#
#
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Foods
def food_index(request):
    food = Food.objects.all()
    return render(request, 'food/index.html', { 'food': food})

# 1) Make a view function
# 2) add the view to the urls.py inside main_app.urls file
# 3) Create functions for html files
# 4) make the html page for our functions
# 5) after creating the function add to the urls.py in the main_app 
