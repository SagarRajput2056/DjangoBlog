from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Category
from .forms import CommentForm
from django.db.models import Q

# Create your views here.

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'form': form,
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html',{
        'category': category,
        'posts': posts,
    })

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query) | 
        Q(body__icontains=query) | 
        Q(category__title__icontains=query))

    return render(request, 'blog/search.html', {
        'query': query,
        'posts': posts,
    })