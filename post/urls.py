from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [

    path('add',views.addpost,name='add_post'),
    path('edit <int:id>',views.editpost,name='edit'),
     path('delete <int:id>',views.deletepost,name='delete'),

]

