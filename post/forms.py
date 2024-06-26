from django import forms 
from post.models import Post


class newpost(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ['author']

        widgets={

    'time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    'categories': forms.SelectMultiple(attrs={'class': 'select-multiple'}),

    }
