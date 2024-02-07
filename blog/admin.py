from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category, Favorite


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for managing the Post model.

    This class customizes the admin interface for Posts, including which fields
    are displayed in the list view, available search fields, filters, and the
    integration of Summernote for rich text editing of the post content.

    Attributes:
        list_display (tuple): Specifies the columns that should be displayed in the list view.
        search_fields (list): Defines the fields that should be searchable in the admin.
        list_filter (tuple): Determines the filters available in the sidebar of the list view.
        prepopulated_fields (dict): Automatically fills the slug field based on the post title.
        summernote_fields (tuple): Specifies the fields that will use the Summernote widget for rich text editing.
    """
    list_display = ('title', 'author', 'status',
                    'created_on', 'featured_image')
    search_fields = ['title', 'content']
    list_filter = (('author', admin.RelatedOnlyFieldListFilter), 'status', 'created_on',
                   'categories', ('favorited_by__user', admin.RelatedOnlyFieldListFilter))
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for managing the Comment model.

    Customizes the display of comments in the admin interface, allowing for easy moderation
    and review of comments posted by users. It includes configuration for list display, and
    filtering options.

    Attributes:
        list_display (tuple): Columns shown in the comment list view, including the author, body of the comment, related post, creation date, and approval status.
        list_filter (tuple): Filters to quickly view comments based on approval status.
    """
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for managing the Category model.

    Simplifies category management by specifying the displayed columns in the admin list view.

    Attributes:
        list_display (tuple): Specifies the 'name' column to be displayed in the list view for categories.
    """
    list_display = ('name',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for managing the Favorite model.

    Provides an overview of favorite posts marked by users, including custom display columns
    and filter options to navigate through favorites efficiently.

    Attributes:
        list_display (tuple): Columns shown in the favorite list view, including the user who favorited a post and the post itself, along with a count of how many times a post has been favorited.
        list_filter (tuple): Filters to quickly view favorites based on the post's title.
    """
    list_display = ('user', 'post', 'get_favorite_count')
    list_filter = ('post__title',)


admin.site.register(Comment, CommentAdmin)
