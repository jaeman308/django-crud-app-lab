from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post, Book


class PostCreate(CreateView):
    model = Post 
    fields = '__all__'
    success_url = '/posts/'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

def home(request):
    return render(request, 'main_app/home.html')

def about(request): 
    return render(request, 'main_app/about.html')

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/detail.html', {'post': post})

def book_index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book/detail.html', {'book': book})