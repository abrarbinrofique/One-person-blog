from django import forms

from author.models import Author

class Add_author(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'


