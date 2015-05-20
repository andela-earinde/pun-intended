from django.contrib import admin
from issues.models import Post 
from issues.models import Category
from issues.models import Comment  

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


