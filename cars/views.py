from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from .models import User
from .models import Login
from .models import Vehicle
from django.contrib.auth import authenticate
from django.contrib import messages


def home(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        Email = request.POST['Email']
        password = request.POST['password']
        ContactNumber = request.POST['ContactNumber']
        Location = request.POST['Location']
        Gender = request.POST['Gender']


    else:

        return render(request, 'index.html')




def base(request):
    return render(request,'base.html')

def login(request):
      if request.method == "POST":
           Username = request.POST['Username']
           Password = request.POST['Password']

           messages.success(request, "login")
           return redirect('home')

      else:
          return render(request,'login.html')


def vehicle(request):
    if request.method == "POST":
        vehicle_name = request.POST['vehicle_name']
        VehicleModel_number = request.POST['VehicleModel_number']
        vehicle_problem = request.POST['Vehicle_problem']
        Date = request.POST['Date']

        messages.success(request, "vehicle_name")
        return redirect('vehicle')
    else:

        return render(request, 'vehicle.html')

