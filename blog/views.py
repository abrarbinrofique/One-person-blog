from django.shortcuts import render

from post.models import Post



def blogerland(request):
   
 
    return render (request,'base.html')



# def profile(request):
#     data=Post.objects.all()
#     print(data)
#     return render (request,'profile.html',{'data':data})

