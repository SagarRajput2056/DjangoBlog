from django.shortcuts import render
from blog.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {
        'posts':posts,
    })

def about(request):
    return render(request, 'main/about.html')

