from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [

    path('add',views.add_author,name='add_author'),
    path('author/login',views.authorlogin,name='login'),
    path('author/logout',views.authorlogout,name='logout'),
    path('author/profile',views.authorprofile,name='profile'),
     path('home/',views.home,name='home')
]


