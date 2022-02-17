# main/blog/forms.py

# Django modules
from django import forms

# My modules
from .models import Comment

class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    """
    Building a form dynamically from the model Comment
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    """
    Allow users to search posts
    """
    query = forms.CharField()