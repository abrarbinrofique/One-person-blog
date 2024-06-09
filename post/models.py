from django.db import models

from catagory.models import Catagory

from author.models import Author

from profiles.models import profile

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=200)
    catagory=models.ManyToManyField(Catagory)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    time=models.DateTimeField()

   


    def __str__(self):
        return self.name
