from django.db import models

# Create your models here.
class User(models.Model):
     First_name = models.CharField(max_length=255)
     Last_name = models.CharField(max_length=255)
     Email = models.CharField(max_length=100)
     Password = models.CharField(max_length=100)
     Contact_Number = models.IntegerField()
     location = models.CharField(max_length= 100)
     Gender = models.CharField(max_length=100)

class Login(models.Model):
     User_name = models.CharField(max_length=255)
     password = models.CharField(max_length=100)

class Vehicle(models.Model):
     vehicle_name = models.CharField(max_length=255)
     vehicleModel_Number = models.CharField(max_length=100)
     vehicleproblem = models.CharField(max_length=255)
     Date = models.DateField()
