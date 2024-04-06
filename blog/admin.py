from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
# in the class below we have a inheritance from admin page.
# changes of admin panel should be here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ('title','author','counted_view','status','login_required','published_date')
    list_filter = ('status','author')
    #ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content','title')

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ['name','post']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
