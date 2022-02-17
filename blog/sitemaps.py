# blog/sitemaps.py
# Django modules
from django.contrib.sitemaps import Sitemap

# My modules
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    
    def lastmod(self, obj):
        return obj.updated