from django import forms
from django.contrib.auth.models import User
from .models import Comment, Category, Post, Favorite, UserProfile


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
    """
    This form is used for creating or editing a blog post.

    Fields:
        - title (CharField): The title of the blog post.
        - content (TextField): The main content of the blog post.
        - categories (ModelMultipleChoiceField): A multiple-choice field for selecting post categories.

    Attributes:
        categories (ModelMultipleChoiceField): A field that allows users to select multiple categories for the blog post.

    Meta:
        model (Post): Specifies the model associated with this form.
        fields (list): Specifies the fields from the model to include in the form.

    """
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class FavoriteForm(forms.ModelForm):
    """
    This form is used for marking a post as a favorite.

    Fields:
        This form has no visible fields, as it's used to mark a post as a favorite without additional user input.

    Meta:
        model (Favorite): Specifies the model associated with this form.
        fields (list): Specifies the fields from the model to include in the form, which is an empty list as it doesn't require user input.

    """
    class Meta:
        model = Favorite
        fields = []

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'about']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']