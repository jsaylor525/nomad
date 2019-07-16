from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

'''
arg1: is the extenstion from the base url, ex. www.examplewebsite.com/<arg1>
arg2: is the function that will be called to render the page.
arg3: is the url link that can be used in django's template to. ex.
   <a href="{% url '<arg3>' %}">Page Name</a>
'''
urlpatterns = [
    path('clock/',           views.clockView,        name='clock'),
    path('movements/',       views.movementsView,    name='movements'),
    path('workouts/',        views.WorkoutListView.as_view(), name='workouts'),
    path('workout_builder/', views.workoutBuilderView, name='workout_builder'),
]
