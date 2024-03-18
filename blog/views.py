from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request) :
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    next_post = Post.objects.filter(id__gt=post.id, status=1, published_date__lte=timezone.now()).order_by('id', '-published_date').first()
    previous_post = Post.objects.filter(id__lt=post.id, status=1, published_date__lte=timezone.now()).order_by('-id', '-published_date').first()
    context = {'post': post, 'counted_view': post.counted_view, 'next_post': next_post, 'previous_post': previous_post}
    post.counted_view += 1
    post.save()
    return render(request, "blog/blog-single.html", context)


    