from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.urls import reverse

# Create your models here.


class Food(models.Model):
	name = models.CharField(max_length=200 ,null=False)
	quantity = models.PositiveIntegerField(null=False,default=0)
	calorie = models.FloatField(null=False,default=0)
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	#association with user. if you delete the user it will delete the foods associated with it
	# user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Profile(models.Model):
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	calorie_count = models.FloatField(default=0,null=True,blank=True) # counting calories for each day
	food_selected = models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True) # food the user selects for consuming
	quantity = models.FloatField(default=0)
	total_calorie = models.FloatField(default=0,null=True)
	date = models.DateField(auto_now_add = True)
	calorie_goal = models.PositiveIntegerField(default=0) # setting a goal for calorie consumption for each day
	all_food_selected_today = models.ManyToManyField(Food,through='PostFood',related_name='inventory') # stores all the food selected in a day

	

	
	def save(self, *args, **kwargs):# new
		if self.food_selected != None:
			self.amount = (self.food_selected.calorie/self.food_selected.quantity) 
			self.calorie_count = self.amount*self.quantity
			self.total_calorie = self.calorie_count + self.total_calorie  
			calories = Profile.objects.filter(person_of=self.person_of).last()
			PostFood.objects.create(profile=calories,food=self.food_selected,calorie_amount=self.calorie_count,amount=self.quantity)
			self.food_selected = None
			super(Profile, self).save(*args,**kwargs)
	
		else:
			super(Profile,self).save(*args,**kwargs)



	def __str__(self):
		return str(self.person_of.username)


class PostFood(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    calorie_amount = models.FloatField(default=0,null=True,blank=True)
    amount = models.FloatField(default=0)
