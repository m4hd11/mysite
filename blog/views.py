from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = list(Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date'))

    post = get_object_or_404(Post, pk=pid, status=1)

    post.counted_views += 1
    post.save(update_fields=['counted_views'])

    current_index = posts.index(post)

    prev_post = posts[current_index - 1] if current_index > 0 else None
    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post
    }
    
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {
        'post': post
    }
    return render(request, 'test.html', context)

