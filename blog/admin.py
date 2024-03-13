from django.contrib import admin
from blog.models import Post

# Register your models here.
# in the class below we have a inheritance from admin page.
# changes of admin panel should be here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    #empty_value_display = "-empty-"
    list_display = ('title','counted_view','status','published_date')
    list_filter = ('status',)
    #ordering = ['-created_date']
    search_fields = ['title','content']


admin.site.register(Post, PostAdmin)
