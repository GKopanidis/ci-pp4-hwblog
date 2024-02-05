from django.urls import path
from . import views
from .views import PostDeleteConfirm, PostDelete, PostDeleteSuccess

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('not_logged_in/', views.not_logged_in, name='not_logged_in'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteConfirm.as_view(), name='post_delete_confirm'),
    path('post/<int:pk>/delete/confirm', PostDelete.as_view(), name='post_delete'),
    path('post/delete/success', PostDeleteSuccess.as_view(), name='post_delete_success'),
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
