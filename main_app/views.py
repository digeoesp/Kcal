from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#  bring in decorator
from django.contrib.auth.decorators import login_required # need this to send a response to the user
from .forms import CreateUserForm, SelectFoodForm, AddFoodForm, ProfileForm
# imports
from .models import Food, Profile


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
    #for showing all food items available
	form = AddFoodForm(request.POST) 
	if request.method == 'POST':
		form = AddFoodForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.person_of = request.user
			profile.save()
			return redirect('add_food')
	else:
		form = AddFoodForm()
		
	return render(request,'foods/index.html') # make sure foods is the same name as the folder
# Foods
def profile_index(request):
    profile = Profile.objects.all()
    return render(request, 'profiles/index.html', { 'profile': profile}) # make sure foods is the same name as the folder

def sign_up(request):
  error_message= ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # ok user creare log thme in
      login(request, user)
      return redirect('index')
    else: 
      error_message='that was a no go, Invalid user'
      #this will run after if its not  a piost or is=t was inva;iod
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  })



def loginPage(request):
    context = {}
    return render(request, 'registration/login.html', context)

def resources(request):
    return render(request, 'resources.html')

def shop(request):
    return render(request, 'shop.html')


# 1) Make a view function
# 2) add the view to the urls.py inside main_app.urls file
# 3) Create functions for html files
# 4) make the html page for our functions
# 5) after creating the function add to the urls.py in the main_app 
