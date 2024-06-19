from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [

    path('add',views.add_author,name='add_author'),
    path('login',views.authorlogin,name='login'),
    path('logout',views.authorlogout,name='logout'),
    path('profile',views.authorprofile,name='profile'),
    path('home/',views.home,name='home'),
    path('home/<slug:category_slug>/',views.home,name='catagory_wise_post'),
    path('edit/authorinfo',views.edit_author,name='edit_author'),
    path('edit/oldpass',views.oldpass,name='oldpass'),
    path('edit/withoutoldpass',views.withoutoldpass,name='withoutoldpass'),
    
]


