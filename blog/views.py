from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DeleteView, DetailView, TemplateView
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from .models import Post, Comment, Like, Category, Favorite
from .forms import CommentForm, UserForm, UserProfileForm, PostForm


class UserPermissionMixin:
    """
    Mixin to check user permissions for editing or deleting objects.

    Provides a method `has_permission` to determine if the current user is
    authorized to perform an action on an object, specifically checking if
    the user is the author of the object or a superuser.

    Methods:
        has_permission(request, *args, **kwargs): Returns True if the user
        has permission to perform the action, otherwise False.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not (request.user.is_superuser or request.user.is_staff):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostList(generic.ListView):
    """
    Display a list of all published posts.

    Extends the generic ListView to show all posts with a status of
    'published'. Includes pagination set to 6 posts per page and provides
    a list of all categories to the context for category-based filtering
    in the template.
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
    Display a detailed view of a single post, including its comments
    and like status.

    Fetches a post by its slug and status, lists all approved comments
    associated with it, or unapproved comments made by the current user.
    Also checks whether the current user has liked or favorited the post.
    Handles posting of new comments and redirects back to the post detail
    page on successful comment submission.
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    user_is_auth = request.user.is_authenticated
    user_is_privileged = user_is_auth and (
        request.user.is_superuser or request.user.is_staff
    )

    if user_is_privileged:
        comments = post.comments.order_by("-created_on")
    elif user_is_auth:
        comments = post.comments.filter(
            Q(approved=True) |
            (Q(approved=False) & Q(author=request.user))
        ).order_by("-created_on")
    else:
        comments = post.comments.filter(approved=True).order_by("-created_on")

    comment_count = comments.count()
    liked_by_user = (
        post.likes.filter(user=request.user).exists()
        if user_is_auth else False
    )
    favorited_by_user = (
        post.favorited_by.filter(user=request.user).exists()
        if user_is_auth else False
    )

    if request.method == "POST":
        if "comment_id" in request.POST:
            comment_id = request.POST.get("comment_id")
            comment = Comment.objects.get(id=comment_id)
            if user_is_privileged:
                comment.approved = True
                comment.save()
                messages.success(request, "Comment approved.")
                return redirect('blog:post_detail', slug=slug)
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(
                    request,
                    "Your comment has been posted and is awaiting approval."
                )
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

    Requires the user to be logged in. Validates that the user is the
    author of the comment before allowing the edit. Saves the edited
    comment and redirects to the post detail page.
    """
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug)
    if not (request.user == comment.author
            or request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Kommentar erfolgreich aktualisiert.")
            return redirect('blog:post_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_edit.html', {
        'form': form,
        'comment': comment
    })


@login_required
def comment_delete(request, slug, comment_id):
    """
    Allow a user to delete their own comment.

    Requires the user to be logged in. Validates that the user is the
    author of the comment before deletion. Redirects to the post detail
    page after successful deletion.
    """
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug)
    if request.user.is_authenticated and (request.user.is_staff
                                          or request.user.is_superuser
                                          or request.user == comment.author):
        comment.delete()
        messages.success(request, "Comment has been deleted.")
    else:
        messages.error(request, "You do not have permission "
                       "to delete this comment.")
    return redirect('blog:post_detail', slug=slug)


@login_required
def like_post(request, post_id):
    """
    Toggle a user's like on a post.

    Requires the user to be logged in. Creates a new like for the post
    by the current user if not already liked, otherwise, it removes the like.
    Redirects to the post detail page.
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
    Allows a logged-in user to remove their like from a post.

    Parameters:
        request: HttpRequest object.
        post_id: ID of the post to be unliked.

    Finds the post by ID and removes the like from it for the current user.
    Redirects to the post detail page with a success message.
    """
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(user=request.user, post=post).delete()
    messages.success(request, "You have unliked the post.")
    return redirect('blog:post_detail', slug=post.slug)


def post_list_by_category(request, category):
    """
    Display a list of posts filtered by a specific category.

    Filters the posts by category name and status. Provides a list of
    all categories to the context for display in the template.
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

    Requires the user to be logged in. Toggles the favorite status of
    a post for the current user.
    Redirects to the post detail page after toggling the favorite status.
    """
    post = get_object_or_404(Post, id=post_id)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user, post=post
    )
    if created:
        messages.success(request, "Post added to favorites.")
    else:
        favorite.delete()
        messages.success(request, "Post removed from favorites.")
    return redirect('blog:post_detail', slug=post.slug)


@login_required
def unfavorite_post(request, post_id):
    """
    Allows a logged-in user to remove a post from their list of favorites.

    Parameters:
        request: HttpRequest object.
        post_id: ID of the post to be unfavorited.

    Attempts to find the favorite relation and delete it. Redirects
    to the post detail page with a success message if the post was
    unfavorited, or a warning message if the post was not in the user's
    favorites.
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
    Displays a list of the logged-in user's favorite posts.

    Fetches all favorite relations for the current user and renders
    them in a template.
    """
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'blog/favorite_list.html', {'favorites': favorites})


@login_required
def edit_profile(request):
    """
    Allows a logged-in user to edit their profile information.

    Handles both GET and POST requests. If the method is POST, attempts to save
    the updated user and profile information. On successful update, redirects
    to the profile view with a success message. For GET requests, renders the
    profile editing form with existing user information.
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.userprofile
        )
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
    Displays the profile of the logged-in user.

    Renders a template showing the current user's profile information.
    """
    return render(request, 'blog/profile.html', {'user': request.user})


def not_logged_in(request):
    """
    Informs users who are not logged in that they cannot access certain
    areas.
    Renders a template that displays a message to users trying to access
    restricted areas without being logged in, prompting them to log in
    or register.
    """
    return render(request, 'blog/not_logged_in.html')


class PostCreate(LoginRequiredMixin, UserPermissionMixin, generic.CreateView):
    """
    Create a new blog post. Requires user to be logged in and have
    permission.

    Extends the generic CreateView with additional permission checks to
    ensure that only authorized users can create posts. Upon successful
    form submission, redirects to the home page and displays a success message.
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
    Edit an existing blog post. Requires user to be logged in and have
    permission.

    Extends the generic UpdateView with additional permission checks.
    Ensures that only the author or a superuser can edit a post. Redirects to
    the post detail page on successful update with a success message.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail',
                            kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)


class PostDeleteConfirm(UserPermissionMixin, LoginRequiredMixin, DetailView):
    """
    A view to confirm the deletion of a blog post.

    Extends Django's DetailView to display detailed information about the post
    that is requested to be deleted, allowing users to confirm their action.
    """
    model = Post
    template_name = 'blog/post_delete_confirm.html'


class PostDelete(LoginRequiredMixin, UserPermissionMixin, DeleteView):
    """
    Delete an existing blog post. Requires user to be logged in and have
    permission.

    Extends the generic DeleteView with additional permission checks.
    Ensures that only the author or a superuser can delete a post. Redirects
    to a success page on successful deletion with a success message.
    """
    model = Post
    success_url = reverse_lazy('blog:post_delete_success')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully')
        return super().delete(request, *args, **kwargs)


class PostDeleteSuccess(UserPermissionMixin, LoginRequiredMixin, TemplateView):
    """
    Displays a success message after a post has been successfully deleted.

    Extends Django's TemplateView to render a simple template that informs the
    user of the successful deletion of a blog post.
    """
    template_name = 'blog/post_delete_success.html'


def is_staff_or_superuser(user):
    """
    Check if the user is a staff member or a superuser.

    Args:
        user (User): The user to check.

    Returns:
        bool: True if the user is a staff member or a superuser,
        False otherwise.
    """
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_staff_or_superuser)
def approve_comment(request, slug, comment_id):
    """
    Approve a specific comment and redirect back to the post detail page.

    This view is protected and requires the user to be logged in and either
    a staff member or a superuser.
    It sets the 'approved' attribute of a Comment instance to True and
    saves it.

    Args:
        request (HttpRequest): The request instance.
        slug (str): The slug of the post to which the comment belongs.
        comment_id (int): The ID of the comment to approve.

    Returns:
        HttpResponseRedirect: A redirect to the 'post_detail' view for
        the post associated with the comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = True
    comment.save()
    return redirect('blog:post_detail', slug=slug)
