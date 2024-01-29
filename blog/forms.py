from django import forms
from .models import Comment, Category, Post, Favorite


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('body',)

class BlogPostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = []