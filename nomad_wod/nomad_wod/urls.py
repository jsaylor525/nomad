"""nomad_wod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import logout

# from apps.accounts.views import views as apps_views
from apps.accounts import views as account_views

urlpatterns = [
    # enable the admin interface
    path('admin/',              admin.site.urls),

    # provide social authentication
    path('oauth/',              include('social_django.urls', namespace='social')),

    path('',                    account_views.signup,   name="signup"),
    path('home/',               account_views.home,     name="home"),
    path("signup/",             account_views.signup,   name="signup"),
    path("settings/",           account_views.settings, name="settings"),
    path("settings/password",   account_views.settings, name="password"),
    
    path('workout/',            include('workout.urls')),

    path('login/',              auth_views.LoginView.as_view(), name='login'),
    path("logout/",             auth_views.LogoutView.as_view(), name="logout"),
    
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
