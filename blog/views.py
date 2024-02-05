from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, DetailView, TemplateView
from .models import Post, Comment, Like, Category, Favorite
from .forms import CommentForm, UserForm, UserProfileForm, PostForm

class UserPermissionMixin:
    """
    A mixin to check for specific user permissions.
    """
    def has_permission(self, request, *args, **kwargs):
        obj = self.get_object()
        return obj.author == request.user or request.user.is_superuser

class PostList(generic.ListView):
    """
    Display a list of all published posts.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def post_detail(request, slug):
    """
    Display a detailed view of a single post, including its comments and like status.
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()
    liked_by_user = post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
    favorited_by_user = post.favorited_by.filter(user=request.user).exists() if request.user.is_authenticated else False

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been posted and is awaiting approval.")
            return redirect('blog:post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "liked_by_user": liked_by_user,
        "favorited_by_user": favorited_by_user,
    })

@login_required
def comment_edit(request, slug, comment_id):
    """
    Allow a user to edit their own comment.
    """
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid() and request.user == comment.author:
            form.save()
            messages.success(request, "Your comment has been updated.")
            return redirect('blog:post_detail', slug=slug)
        else:
            messages.error(request, "You do not have permission to edit this comment.")
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form, 'comment': comment})

@login_required
def comment_delete(request, slug, comment_id):
    """
    Allow a user to delete their own comment.
    """
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug)
    if request.user == comment.author:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    else:
        messages.error(request, "You do not have permission to delete this comment.")
    return redirect('blog:post_detail', slug=slug)

@login_required
def like_post(request, post_id):
    """
    Toggle a user's like on a post.
    """
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        messages.success(request, "You have unliked the post.")
    else:
        messages.success(request, "You have liked the post.")
    return redirect('blog:post_detail', slug=post.slug)

@login_required
def unlike_post(request, post_id):
    """
    Allow a user to unlike a post.
    """
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(user=request.user, post=post).delete()
    messages.success(request, "You have unliked the post.")
    return redirect('blog:post_detail', slug=post.slug)

def post_list_by_category(request, category):
    """
    Display a list of posts filtered by a specific category.
    """
    posts = Post.objects.filter(categories__name=category, status=1)
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': posts,
        'categories': categories,
        'category_name': category
    })

@login_required
def favorite_post(request, post_id):
    """
    Allow a user to favorite or unfavorite a post.
    """
    post = get_object_or_404(Post, id=post_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)
    if created:
        messages.success(request, "Post added to favorites.")
    else:
        favorite.delete()
        messages.success(request, "Post removed from favorites.")
    return redirect('blog:post_detail', slug=post.slug)

@login_required
def unfavorite_post(request, post_id):
    """
    Allow a user to remove a post from their favorites.
    """
    post = get_object_or_404(Post, id=post_id)
    try:
        favorite = Favorite.objects.get(user=request.user, post=post)
        favorite.delete()
        messages.success(request, "Post removed from favorites.")
    except Favorite.DoesNotExist:
        messages.warning(request, "Post is not in your favorites.")
    return redirect('blog:post_detail', slug=post.slug)

@login_required
def favorite_list(request):
    """
    Display a list of the user's favorite posts.
    """
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'blog/favorite_list.html', {'favorites': favorites})

@login_required
def edit_profile(request):
    """
    Allow a user to edit their profile information.
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('blog:profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'blog/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def profile_view(request):
    """
    Display the user's profile.
    """
    return render(request, 'blog/profile.html', {'user': request.user})

def not_logged_in(request):
    """
    Display a message to users who are not logged in but are trying to access areas that require authentication.
    """
    return render(request, 'blog/not_logged_in.html')

class PostCreate(LoginRequiredMixin, UserPermissionMixin, generic.CreateView):
    """
    Create a new blog post. Requires user to be logged in and have permission.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Post created successfully.")
        return response

class PostEdit(LoginRequiredMixin, UserPermissionMixin, generic.UpdateView):
    """
    Edit an existing blog post. Requires user to be logged in and have permission.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)

class PostDeleteConfirm(DetailView):
    model = Post
    template_name = 'blog/post_delete_confirm.html'

class PostDelete(LoginRequiredMixin, UserPermissionMixin, DeleteView):
    """
    Delete an existing blog post. Requires user to be logged in and have permission.
    """
    model = Post
    success_url = reverse_lazy('blog:post_delete_success')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully')
        return super().delete(request, *args, **kwargs)

class PostDeleteSuccess(TemplateView):
    template_name = 'blog/post_delete_success.html'
