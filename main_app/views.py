from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm, SelectFoodForm, AddFoodForm, ProfileForm
from .models import Food, Profile, PostFood
from django.contrib.auth.decorators import login_required # need this to send a response to the user
from datetime import timedelta
from django.utils import timezone
from datetime import date
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .filters import FoodFilter
#pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

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

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Home(request):
  #taking the latest profile object
	# calories = Profile.objects.filter(person_of=request.user).last()
	# calorie_goal = calories.calorie_goal
	
	# #creating one profile each day
	# if date.today() > calories.date:
	# 	profile=Profile.objects.create(person_of=request.user)
	# 	profile.save()

	# calories = Profile.objects.filter(person_of=request.user).last()
		
	# # showing all food consumed present day

	# all_food_today=PostFood.objects.filter(profile=calories)
	
	# calorie_goal_status = calorie_goal -calories.total_calorie
	# over_calorie = 0
	# if calorie_goal_status < 0 :
	# 	over_calorie = abs(calorie_goal_status)

	# context = {
	# 'total_calorie':calories.total_calorie,
	# 'calorie_goal':calorie_goal,
	# 'calorie_goal_status':calorie_goal_status,
	# 'over_calorie' : over_calorie,
	# 'food_selected_today':all_food_today
	# }
	

	return render(request, 'home.html') #,context
	
	
# Foods
def add_food(request):
	


    #for showing all food items available
	food_items = Food.objects.filter(person_of=request.user)
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
	#for filtering food
	myFilter = FoodFilter(request.GET,queryset=food_items)
	food_items = myFilter.qs
	context = {'form':form,'food_items':food_items,'myFilter':myFilter}
	return render(request,'add_food.html',context)
 # make sure foods is the same name as the folder
# Foods

def select_food(request):
	person = Profile.objects.filter(person_of=request.user).last()
	#for showing all food items available
	food_items = Food.objects.filter(person_of=request.user)
	form = SelectFoodForm(request.user,instance=person)

	if request.method == 'POST':
		form = SelectFoodForm(request.user,request.POST,instance=person)
		if form.is_valid():
			
			form.save()
			return redirect('home')
	else:
		form = SelectFoodForm(request.user)

	context = {'form':form,'food_items':food_items}
	return render(request, 'select_food.html',context)

def ProfilePage(request):


	#getting the lastest profile object for the user
	person = Profile.objects.filter(person_of=request.user).last()
	food_items = Food.objects.filter(person_of=request.user)
	form = ProfileForm(instance=person)

	if request.method == 'POST':
		form = ProfileForm(request.POST,instance=person)
		if form.is_valid():	
			form.save()
			return redirect('profile')
	else:
		form = ProfileForm(instance=person)

	#querying all records for the last seven days 
	some_day_last_week = timezone.now().date() -timedelta(days=7)
	records=Profile.objects.filter(date__gte=some_day_last_week,date__lt=timezone.now().date(),person_of=request.user)

	context = {'form':form,'food_items':food_items,'records':records}
	return render(request, 'profile.html',context)

def update_food(request,pk):
	food_items = Food.objects.filter(person_of=request.user)

	food_item = Food.objects.get(id=pk)
	form =  AddFoodForm(instance=food_item)
	if request.method == 'POST':
		form = AddFoodForm(request.POST,instance=food_item)
		if form.is_valid():
			form.save()
			return redirect('profile')
	myFilter = FoodFilter(request.GET,queryset=food_items)
	context = {'form':form,'food_items':food_items,'myFilter':myFilter}

	return render(request,'add_food.html',context)


def delete_food(request,pk):

	food_item = Food.objects.get(id=pk)
	if request.method == "POST":
		food_item.delete()
		return redirect('profile')
	context = {'food':food_item,}
	return render(request,'delete_food.html',context)

def resources(request):



    return render(request, 'resources.html')

def shop(request):
    return render(request, 'shop.html')


# 1) Make a view function
# 2) add the view to the urls.py inside main_app.urls file
# 3) Create functions for html files
# 4) make the html page for our functions
# 5) after creating the function add to the urls.py in the main_app 
