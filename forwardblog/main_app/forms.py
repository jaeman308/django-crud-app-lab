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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_published'].input_formats = ['%Y-%m-%dT%H:%M']



class BookForm(forms.ModelForm):  
    class Meta:
        model = Book 
        fields = ['title', 'description', 'is_published', 'date_published']
        widgets = {
            'date_published': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_published'].input_formats = ['%Y-%m-%dT%H:%M']
