from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'featured_image')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'categories')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
