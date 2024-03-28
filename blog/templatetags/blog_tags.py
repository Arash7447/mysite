from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.simple_tag(name = 'totalposts')

def function () :
    posts = Post.objects.filter(status = 1).count()
    return posts 


@register.simple_tag(name = 'posts')

def function () :
    posts = Post.objects.filter(status = 1)
    return posts 

@register.filter

def snippet (value,arg = 20) :
    return value [:arg] + '...'

@register.inclusion_tag('blog/popular-posts.html')
def latestposts(arg = 2) :
    posts = Post.objects.filter(status = 1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/post-categories.html')
def postcategories() :
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict} 


@register.inclusion_tag('blog/latest-posts.html')

def latest_posts():
    posts = Post.objects.order_by('-published_date')[:6]
    categories = Category.objects.all()
    return {'latest_posts': posts, 'categories':categories}

