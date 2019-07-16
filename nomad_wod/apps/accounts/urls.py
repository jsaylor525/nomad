from django.conf.urls import url 
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('',                    views.signup,       name="signup"),
    path('home/',               views.home,         name="home"),
    path("signup/",             views.signup,       name="signup"),
    path("settings/",           views.settings,     name="settings"),
    path("settings/password",   views.settings,     name="password"),    
    path('profile/',            views.account,      name='account'),
    path('logged_out/',         views.logged_out,   name='logged_out'),

    path('login/',  auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  
]

