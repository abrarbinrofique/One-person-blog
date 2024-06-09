from django.shortcuts import render

from catagory.forms import newcatagory

# Create your views here.
def add_catagory(request):
     if (request.method=='POST'):
          form=newcatagory(request.POST)
          form.is_valid()
          form.save()

     else:
          form=newcatagory()

     return render (request,'addcatagory.html',{'form':form})