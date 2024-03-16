from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request) :
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request,pid) :
    post = get_object_or_404(Post, pk=pid)
    context = context = {'post': post, 'counted_view': post.counted_view}
    post.counted_view += 1
    post.save()
    
    if post.published_date <= timezone.now() :
        return render(request, "blog/blog-single.html", context)
    
    else :
        return redirect("blog_view")
    
    
    
    #return render(request, "blog/blog-single.html", context)

    