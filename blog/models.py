from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)


    def __str__(self):
        return self.name    


class Post (models.Model) :
    image = models.ImageField(upload_to = 'blog/',default = 'blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField (max_length = 200)
    content = models.TextField ()
    tags = TaggableManager()
    category = models.ManyToManyField (Category)
    counted_view = models.IntegerField (default = 0)
    status = models.BooleanField (default = False)
    published_date = models.DateTimeField (null = True)
    created_date = models.DateTimeField (auto_now_add = True)
    update_date = models.DateTimeField (auto_now = True)


    class Meta:
        ordering = ['-created_date']
        


    def __str__(self) :
        return "{} - {}".format(self.title, self.id) 


    def excerpt(self) :
        return truncatewords(self.content,20)

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
