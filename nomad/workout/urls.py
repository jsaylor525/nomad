from django.urls import path

from . import views

urlpatterns = [
    path('', views.accountView, name='index'),
    path('account', views.accountView, name='account'),
    path('clock', views.clockView, name='clock'),
    path('workouts', views.workoutsView, name='workouts'),
    path('movements', views.movementsView, name='movements'),
]