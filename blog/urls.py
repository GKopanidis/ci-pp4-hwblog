"""
This module contains the models for the blog app.
"""

from django.urls import path
from . import views
from .views import like_post

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<int:post_id>/', views.unlike_post, name='unlike_post'),
    path('category/all/', views.PostList.as_view(), name='post_list_by_category_all'),
    path('category/<str:category>/', views.post_list_by_category, name='post_list_by_category'),
    path('favorite_post/<int:post_id>/', views.favorite_post, name='favorite_post'),
    path('unfavorite_post/<int:post_id>/', views.unfavorite_post, name='unfavorite_post'),
]
