from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=25)
    year = models.IntegerField()
    color = models.CharField(max_length=25)
    photo = models.ImageField(upload_to="car_image/")

class Student(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=40)
    age = models.IntegerField()

class Laptop(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()

class Animal(models.Model):
    name = models.CharField(max_length=25)
    weight = models.IntegerField()

class Fruit(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=20)

class Vegetable(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
