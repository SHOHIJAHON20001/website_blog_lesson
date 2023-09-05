from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogPost(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author']

admin.site.register(Blog, BlogPost)