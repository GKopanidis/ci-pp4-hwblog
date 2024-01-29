from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category, Favorite


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Post model.
    """
    list_display = ('title', 'author', 'status', 'created_on', 'featured_image')
    search_fields = ['title', 'content']
    list_filter = (('author', admin.RelatedOnlyFieldListFilter), 'status', 'created_on',
                   'categories', ('favorited_by__user', admin.RelatedOnlyFieldListFilter))
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model.
    """
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the Category model.
    """
    list_display = ('name',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """
    Admin interface for the Favorite model.
    """
    list_display = ('user', 'post', 'get_favorite_count')
    list_filter = ('post__title',)


admin.site.register(Comment, CommentAdmin)
