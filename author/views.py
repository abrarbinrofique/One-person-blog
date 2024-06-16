from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from author.forms import Author
from django.contrib import messages
from post.models import Post

# Create your views here.
def add_author(request):
#   if not request.user.is_authenticated:
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
#   else:
#       return redirect('add_author')

def authorprofile(request):
    if request.user.is_authenticated:
       data=Post.objects.all()
       return render (request,'profile.html',{'data':data})
    else:
        return redirect('login')

def authorlogin(request):
#   if not request.user.is_authenticated:
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
#   else:
#       return redirect('add_author')


def authorlogout(request):
        logout(request)
        return redirect('login')
       
            
  

def home(request):
    data=Post.objects.all()
    print(data)
    return render (request,'home.html',{'data':data})


