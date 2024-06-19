from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from author.forms import Author,editinfo
from django.contrib import messages
from post.models import Post
from catagory.models import Catagory

# Create your views here.
def add_author(request):
 if not request.user.is_authenticated:
    if request.method=='POST':
        forms=Author(request.POST)
        if forms.is_valid():
            forms.save()
            print(forms.cleaned_data)
            messages.success(request,'Please login here')
            return redirect ('login')
 

    else:
        forms=Author()
    return render(request,'add_author.html',{'form':forms})
 else:
       return redirect('profile')

@login_required
def authorprofile(request):
    if request.user.is_authenticated:
       data=Post.objects.filter(author=request.user)
       return render (request,'profile.html',{'data':data})
    else:
        return redirect('login')

def authorlogin(request):
 if not request.user.is_authenticated:
    if request.method=='POST':
         forms=AuthenticationForm(request=request,data=request.POST)
         if forms.is_valid():
             user=forms.cleaned_data['username']
             userpassword=forms.cleaned_data['password']
             User=authenticate(username=user,password=userpassword)
             if User is not None:
                 messages.success(request,f'welcome to your prfile {user}')
                 login(request,User)
                #  forms.save()
                 return redirect('profile')
             else:
                 return redirect('login')

    
    else:
        forms=AuthenticationForm()
    return render(request,'login.html',{'form':forms})
 else:
      return redirect('profile')



@login_required
def authorlogout(request):
        logout(request)
        return redirect('login')
       
            
  

@login_required
def home(request,category_slug=None):

  if category_slug is not None:
    cmod=Catagory.objects.get(slug=category_slug)
    data=Post.objects.filter( catagory =cmod)
    mod=Catagory.objects.all()
  else:
    mod=Catagory.objects.all()
    data=Post.objects.all()

   

    print(data)
    print(mod)
  return render (request,'home.html',{'data':data,'mod':mod})


def edit_author(request):
 if request.user.is_authenticated:
    if request.method=='POST':
        forms=editinfo(request.POST,instance=request.user)
        if forms.is_valid():
            forms.save()
            print(forms.cleaned_data)
            messages.success(request,'Please login here')
            return redirect ('profile')
 

    else:
        forms=editinfo(instance=request.user)
    return render(request,'edit_author.html',{'form':forms})
 else:
       return redirect('login')
 

@login_required
def oldpass(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Your password has been updated')
            return redirect('profile')
        
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'oldpass.html',{'form':form}) 



@login_required
def withoutoldpass(request):
    if request.method=='POST':
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Your password has been updated')
            return redirect('profile')
        
    else:
        form=SetPasswordForm(user=request.user)
    return render(request,'withoutoldpass.html',{'form':form}) 







