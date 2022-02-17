# main/blog/admin.py

# Django modules
from django.contrib import admin

# My modules
from .models import Post, Comment

# Adding the model to the adminsitration site
# Customizing the way models are displayed
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customizing the model to display
    """
    list_display = ('title', 'slug',
                    'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')