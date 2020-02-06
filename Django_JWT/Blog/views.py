from django.shortcuts import render
from .models import Post

def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})