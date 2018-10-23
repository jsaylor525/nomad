from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import *

def movementsView(request):
   context = {
      "movements": Movement.objects.all(),   
      "equipment": Equipment.objects.all(),
   }
   return render(request, "workout/movements.html", context)

def workoutsView(request):
   context = {
      "workouts":  Workout.objects.all(),  
      "movements": Movement.objects.all(),     
   }
   return render(request, "workout/workouts.html", context)

def accountView(request):
   return render(request, "workout/account.html")

def clockView(request):
   return render(request, "workout/clock.html")