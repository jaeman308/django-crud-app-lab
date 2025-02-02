from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
class PostCreate(CreateView):
    model = Post 
    fields = '__all__'
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