from django import forms
from django.forms import DateInput
from .models import Post, Book

class PostForm(forms.ModelForm):  
    class Meta:
        model = Post  
        fields = ['title', 'description', 'is_published', 'date_published']
        widgets = {
            'date_published': DateInput(attrs={'type': 'date'})
        }



class BookForm(forms.ModelForm):  
    class Meta:
        model = Book 
        fields = ['title', 'description', 'is_published', 'date_published']
        widgets = {
            'date_published': DateInput(attrs={'type': 'date'})
        }