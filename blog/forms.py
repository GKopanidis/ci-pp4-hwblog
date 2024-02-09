from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Category, Post, Favorite, UserProfile


class CommentForm(forms.ModelForm):
    """
    A form for submitting comments on a blog post by users.

    This ModelForm is linked to the `Comment` model. It allows
    users to enter a comment body, facilitating user engagement with
    blog content.

    Meta:
        model (Model): Specifies the Django model (`Comment`) associated
        with this form.
        fields (tuple): Defines the single field ('body') included in the form.
    """

    class Meta:
        model = Comment
        fields = ("body",)


class BlogPostForm(forms.ModelForm):
    """
    A form for creating or editing blog posts, including title, content,
    and category selection.

    Attributes:
        categories (ModelMultipleChoiceField): Enables selection of multiple
        categories for a blog post,
        presented as checkbox options derived from the Category model.

    Meta:
        model (Post): Links this form to the `Post` model.
        fields (list): Lists the fields included in the form, integrating
        a custom 'categories' field alongside 'title' and 'content'.
    """

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Post
        fields = ["title", "content", "categories"]


class FavoriteForm(forms.ModelForm):
    """
    A form for marking a blog post as a favorite, designed for internal
    mechanics without direct user input.

    This ModelForm is associated with the `Favorite` model, primarily
    used to create or delete favorite instances through view logic
    rather than form inputs.

    Meta:
        model (Favorite): Specifies the model linked with this form.
        fields (list): An empty list, indicating no fields are required
        from the user for this operation.
    """

    class Meta:
        model = Favorite
        fields = []


class UserProfileForm(forms.ModelForm):
    """
    A form for users to edit their profile details, specifically the
    profile image and a personal bio.

    Meta:
        model (UserProfile): The model associated with this form,
        pointing to user profile information.
        fields (list): Specifies which fields ('profile_image', 'about')
        are editable through this form.
    """

    class Meta:
        model = UserProfile
        fields = ["profile_image", "about"]


class UserForm(forms.ModelForm):
    """
    A form for editing basic user information, including the username
    and email address.

    Meta:
        model (User): The Django default User model linked to this form.
        fields (list): Lists 'username' and 'email' as the fields
        available for editing by the user.
    """

    class Meta:
        model = User
        fields = ["username", "email"]


class PostForm(forms.ModelForm):
    """
    Form for creating and editing blog posts, offering fields for the
    title, featured image, content, status, excerpt, and category selection,
    with a rich text editor for the content.

    Meta:
        model (Post): Specifies the `Post` model this form is associated with.
        fields (list): Includes the post attributes to be edited or created
        via the form.
        widgets (dict): Customizes the rendering of the 'content' field using
        `SummernoteWidget` for rich text editing.
        help_texts (dict): Provides additional guidance for the
        'categories' field, instructing users on multiple selection.
    """

    class Meta:
        model = Post
        fields = [
            "title",
            "featured_image",
            "content",
            "status",
            "excerpt",
            "categories",
        ]
        widgets = {
            "content": SummernoteWidget(),
        }
        help_texts = {
            "categories": '(Multiple choices allowed. Hold down "Control", '
            'or "Command" on a Mac, to select more than one.)',
            "featured_image": "Optional: If you dont add a picture, it will take a placeholder image.",
        }
