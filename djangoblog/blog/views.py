from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Create your views here.

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'form': form,
    })