from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('loginUser',views.loginUser, name='login'),
    path('logout',views.logout, name='logout'),
    path('deshboard', views.deshboard, name='deshboard')
    
]
