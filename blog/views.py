from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, Category, Favorite, UserProfile
from .forms import CommentForm, UserForm, UserProfileForm

# Create your views here.


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
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
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    ``liked_by_user``
        Boolean indicating whether the user has liked the post.
    ``favorited_by_user``
        Boolean indicating whether the user has favorited the post.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    # Set liked_by_user and favorited_by_user to False if the user is not authenticated
    liked_by_user = False
    favorited_by_user = False
    if request.user.is_authenticated:
        liked_by_user = post.likes.filter(user=request.user).exists()
        favorited_by_user = post.favorited_by.filter(user=request.user).exists()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "liked_by_user": liked_by_user,
            "favorited_by_user": favorited_by_user,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def like_post(request, post_id):
    """
    This function handles the 'liking' of a post by a user.

    Args:
        request: The HTTP request object.
        post_id: The unique identification of the post to be liked.

    Returns:
        A redirection to the detail view of the liked post.
    """
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

    messages.success(request, 'Post liked successfully!')
    return redirect('post_detail', slug=post.slug)

def unlike_post(request, post_id):
    """
    This function handles the 'unliking' of a post by a user.

    Args:
        request: The HTTP request object.
        post_id: The unique identification of the post to be unliked.

    Returns:
        A redirection to the detail view of the unliked post.
    """
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()

    messages.success(request, 'Post unliked successfully!')
    return redirect('post_detail', slug=post.slug)

def post_list_by_category(request, category):
    """
    This function displays a list of posts based on a specific category.

    Args:
        request: The HTTP request object.
        category: The name of the category by which the posts should be filtered.

    Returns:
        An HTML page displaying a list of posts from the specified category.
    """
    posts = Post.objects.filter(categories__name=category)
    categories = Category.objects.all()
    context = {
        'post_list': posts,
        'categories': categories,
        'category_name': category,
        'current_category': category,
    }
    return render(request, 'blog/index.html', context)


def favorite_post(request, post_id):
    """
    This function allows a user to add or remove a post from their favorites.

    Args:
        request: The HTTP request object.
        post_id: The unique identification of the post to be added or removed from favorites.

    Returns:
        A redirection to the detail view of the respective post.
    """
    post = get_object_or_404(Post, id=post_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)

    if created:
        messages.success(request, 'Added to favorites!')
    else:
        favorite.delete()
        messages.success(request, 'Removed from favorites!')

    return redirect('post_detail', slug=post.slug)


def unfavorite_post(request, post_id):
    """
    This function allows a user to remove a post from their favorites.

    Args:
        request: The HTTP request object.
        post_id: The unique identification of the post to be removed from favorites.

    Returns:
        A redirection to the detail view of the respective post.
    """
    post = get_object_or_404(Post, id=post_id)
    favorite = Favorite.objects.filter(user=request.user, post=post).first()

    if favorite:
        favorite.delete()
        messages.success(request, 'Removed from favorites!')
    else:
        messages.success(request, 'Not in favorites!')

    return redirect('post_detail', slug=post.slug)


@login_required
def favorite_list(request):
    """
    This function displays a list of posts marked as favorites by a user.

    Args:
        request: The HTTP request object.

    Returns:
        An HTML page displaying a list of posts marked as favorites.
    """
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'blog/favorite_list.html', {'favorites': favorites})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated.')
            return redirect('profile') 
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
    This view displays the user's profile.

    Args:
        request: The HTTP request object.

    Returns:
        An HTML page displaying the user's profile.
    """
    UserProfile.objects.get_or_create(user=request.user)

    return render(request, 'blog/profile.html', {'user': request.user})

def not_logged_in(request):
    return render(request, 'blog/not_logged_in.html')