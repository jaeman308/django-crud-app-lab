from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.models import Post, Book
from .forms import PostForm, BookForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required 


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

class Login(LoginView):
    template_name = 'login.html'



def home(request):
    return render(request, 'main_app/home.html')

def about(request): 
    return render(request, 'main_app/about.html')

@login_required
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/detail.html', {'post': post})

@login_required
def book_index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book/detail.html', {'book': book})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('post-index')

        else: 
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main_app/signup.html', context)