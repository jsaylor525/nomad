from django.shortcuts import render, HttpResponse

# Create your views here.
from .forms import (
   WorkoutBuilderForm,
)
from .models import (
   Movement,
   Workout,
)
from django.views.generic import (
   ListView, FormView
)

class WorkoutListView(ListView):
   template_name="workout/movement_list.html"
   model = Movement

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # context['now'] = timezone.now()
      return context

def movementsView(request):
   context = {
      "movements": Movement.objects.all(),   
      "equipment": Equipment.objects.all(),
   }
   return render(request, "workout/movements.html", context)

def workoutsView(request):
   context = {
      "workouts":  Workout.objects.all(),  
   }
   return render(request, "workout/workouts.html", context)

class WorkoutBuilderFormView(FormView):
   template_name = "workout/workout_builder.html"
   form_class = WorkoutBuilderForm
   success_url = '/thanks/'

def workoutBuilderView(request):
   context = {
      "workouts":  Workout.objects.all(),  
   }
   return render(request, "workout/workout_builder.html", context)

def accountView(request):
   return render(request, "workout/account.html")

def clockView(request):
   return render(request, "workout/clock.html")

def loginView(request):
   return render(request, "workout/login.html")
