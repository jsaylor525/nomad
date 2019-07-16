"""nomad_wod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

# from apps.accounts.views import views as apps_views
# from apps.accounts import views as account_views

urlpatterns = [
    # enable the admin interface
    path('admin/',      admin.site.urls),

    # provide social authentication
    path('oauth/',      include('social_django.urls', namespace='social')),
    
    path('',            TemplateView.as_view(template_name='core/home.html')),
    path('account/',    include('accounts.urls')),
    path('workout/',    include('workout.urls')),    
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
