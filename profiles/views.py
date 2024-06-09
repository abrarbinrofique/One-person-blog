from django.shortcuts import render

from profiles.forms import new_profile

# Create your views here.
def add_profile(request):
    if request.method=='POST':
        form=new_profile(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)

    else:
         form=new_profile()

    return render (request,'add_profile.html',{'form':form})