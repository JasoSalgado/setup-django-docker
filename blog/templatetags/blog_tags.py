# blog/templatetags/blog_tags.py
# Django modules
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
# My modules
from ..models import Post

register = template.Library()

# Display the number of written posts by the user
@register.simple_tag
def total_posts():
    return Post.published.count()


# Display the latest post
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5): # Display until 5 posts
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# Display the most commented post
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
    