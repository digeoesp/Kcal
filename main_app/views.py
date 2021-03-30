from django.shortcuts import render
from django.http import HttpResponse # need this to send a response to the user

# Create your views here.
# controller but called views in django
# set them up like functions
# 
#
#
#
#
def index(request):
    return HttpResponse('<h1>K Cal</h1>')
