from django.shortcuts import render,redirect

from post.forms import newpost

from post.models import Post

# Create your views here.
def addpost(request):
    if request.method=='POST':
        form=newpost(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect ('profile')

    else:
        form=newpost()
    return render (request,'addpost.html',{'form':form})




def editpost(request,id):
    post=Post.objects.get(pk=id)
    form=newpost(instance=post)
    if request.method=='POST':
        form=newpost(request.POST,instance=post) 
        if form.is_valid():
            form.save()
            return redirect('home')

   
    return render (request,'addpost.html',{'form':form})



def deletepost(request,id):
    post=Post.objects.get(pk=id).delete()

    return redirect('profile')

   
    