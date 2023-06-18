from django.contrib import admin

from .models import Category, BlogPost, Comment

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)