from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)

def mark_as_read(modeladmin, request, queryset):
    queryset.update(read=True)
mark_as_read.short_description = "Mark selected requests as read"

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('name', 'email', 'phone', 'message', 'read',)
    actions = [mark_as_read]
    fields = ['name', 'email', 'phone', 'message', 'read']
