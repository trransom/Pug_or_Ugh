from django.contrib.auth.models import User
from django.db import models

class Dog(models.Model):
	GENDERS = (
		('m', 'male'),
		('f', 'female'),
		('u', 'unknown'),
	)
	SIZES = (
		('s', 'small'),
		('m', 'medium'),
		('l', 'large'),
		('xl', 'extra large'),
		('u', 'unknown'),
	
	)
	name = models.CharField(max_length=200)
	image_filename = models.CharField(max_length=300)
	breed = models.CharField(max_length=200)
	age = models.IntegerField(blank=True)
	gender = models.CharField(max_length=50, choices=GENDERS)
	size = models.CharField(max_length=50, choices=SIZES)
	
	def __str__(self):
		return self.name

class UserDog(models.Model):
	STATUS = (
		('l', 'liked'),
		('d', 'disliked'),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=STATUS)
	
	def __str__(self):
		return self.dog.name


class UserPref(models.Model):
	AGES = (
		('b', 'baby'),
		('y', 'young'),
		('a', 'adult'),
		('s', 'senior'),
	)
	GENDER = (
		('m', 'male'),
		('f', 'female'),
	)
	SIZE = (
		('s', 'small'),
		('m', 'medium'),
		('l', 'large'),
		('xl', 'extra large'),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	age = models.CharField(max_length=10, choices=AGES)
	gender = models.CharField(max_length=10, choices=GENDER)
	size = models.CharField(max_length=20, choices=SIZE)
	
	def __str__(self):
		return self.user.username
