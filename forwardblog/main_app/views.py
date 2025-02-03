from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Book
from .forms import PostForm, BookForm


class PostCreate(CreateView):
    model = Post 
    form_class = PostForm
    success_url = '/posts/'

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books/'

class PostUpdate(UpdateView):
    model= Post
    fields = ['title', 'description']
    success_url = '/posts/'

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'description']
    success_url = '/books/'

class BookDelete(DeleteView):
    model = Book 
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