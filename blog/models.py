# main/blog/models.py

# Django modules
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Third party modules
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    """
    Modifying our own manager
    """
    def get_query(self):
        return super(PublishedManager, 
                    self).get_queryset().filter(status='published')


class Post(models.Model):
    """
    It creates the post model
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # Default manager
    published = PublishedManager() # Our custom manager

    
    class Meta:
        ordering = ('-publish',)
    
    # Canonical URLs form models
    # The convention in Django is to add a get_absolute_url()
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
    

    def __str__(self):
        return self.title

    # It adds a tag
    tags = TaggableManager()

class Comment(models.Model):
    """
    Model to comment posts
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)