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

def about(request):
    lorem_ipsum = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
    return HttpResponse(lorem_ipsum)


# 1)Make a view function
# 2) add the view to the urls.py inside main_app.urls file
