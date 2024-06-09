from django.shortcuts import render
from author.forms import Add_author

# Create your views here.
def add_author(request):
    if request.method=='POST':
        form=Add_author(request.POST)
        if form.is_valid:
            form.save()
            print(form.cleaned_data)

    else:
        form=Add_author()
    return render(request,'add_author.html',{'form':form})