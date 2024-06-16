from django.db import models

from catagory.models import Catagory

from django.contrib.auth.models import User




# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=200)
    catagory=models.ManyToManyField(Catagory)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField()

   


    def __str__(self):
        return self.name
