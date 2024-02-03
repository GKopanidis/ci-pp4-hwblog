from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    This model represents categories for blog posts.

    Attributes:
        name (CharField): The name of the category, should be unique.

    Methods:
        __str__: Returns a string representation of the category.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    This model represents individual blog posts.

    Attributes:
        title (CharField): The title of the blog post, should be unique.
        slug (SlugField): A unique slug for the post's URL.
        author (ForeignKey): A foreign key relation to the User model 
                             representing the post's author.
        featured_image (CloudinaryField): An image field for the post's featured image.
        content (TextField): The main content of the blog post.
        created_on (DateTimeField): The date and time when the post was created 
                                    (auto-generated).
        status (IntegerField): The status of the post (e.g., draft, published).
        excerpt (TextField): A brief excerpt or summary of the post.
        updated_on (DateTimeField): The date and time when the post was last updated 
                                    (auto-generated).
        categories (ManyToManyField): A many-to-many relationship to Category model
                                      representing post categories.

    Meta:
        ordering: The default ordering for blog posts, ordered by 'created_on' in descending order.

    Methods:
        __str__: Returns a string representation of the blog post.
        likes: Returns all the 'Like' objects associated with this post.
        is_liked_by_user(user): Checks if the post is liked by a specific user.
        get_favorite_count(): Gets the count of users who have marked this post as a favorite.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    @property
    def likes(self):
        """
        Get all 'Like' objects associated with this post.

        Returns:
            QuerySet: A queryset containing all 'Like' objects associated with this post.
        """
        return Like.objects.filter(post=self)

    def is_liked_by_user(self, user):
        """
        Check if the post is liked by a specific user.

        Args:
            user (User): The user to check for liking the post.

        Returns:
            bool: True if the user has liked the post, False otherwise.
        """
        return self.likes.filter(user=user).exists()

    def get_favorite_count(self):
        """
        Get the count of users who have marked this post as a favorite.

        Returns:
            int: The count of users who have marked this post as a favorite.
        """
        return Favorite.objects.filter(post=self).count()


class Comment(models.Model):
    """
    This model represents comments on a blog post.

    Attributes:
        post (ForeignKey): A foreign key relation to the Post model representing the commented post.
        author (ForeignKey): A foreign key relation to the User model representing the comment's 
                             author.
        body (TextField): The content of the comment.
        created_on (DateTimeField): The date and time when the comment was created (auto-generated).
        approved (BooleanField): Indicates if the comment has been approved by the admin or not.

    Meta:
        ordering: The default ordering for comments, ordered by 'created_on' in ascending order.

    Methods:
        __str__: Returns a string representation of the comment.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Like(models.Model):
    """
    This model represents post likes by users.

    Attributes:
        user (ForeignKey): A foreign key relation to the User model representing 
                           the user who liked the post.
        post (ForeignKey): A foreign key relation to the Post model representing 
                           the liked post.
        created (DateTimeField): The date and time when the like was created (auto-generated).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    """
    This model represents posts marked as favorites by users.

    Attributes:
        user (ForeignKey): A foreign key relation to the User model representing the user who 
                           marked the post as a favorite.
        post (ForeignKey): A foreign key relation to the Post model representing the favorited post.

    Meta:
        unique_together: Ensures that a user can mark a post as a favorite only once.

    Methods:
        __str__: Returns a string representation of the favorite.
        get_favorite_count(): Gets the count of users who have marked the same post as a favorite.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} favorited {self.post.title}"

    def get_favorite_count(self):
        """
        Get the count of users who have marked the same post as a favorite.

        Returns:
            int: The count of users who have marked the post as a favorite.
        """
        return Favorite.objects.filter(post=self.post).count()

class UserProfile(models.Model):
    """
    A model representing user profiles.

    This model extends the built-in User model by adding additional fields
    such as 'profile_image' for the user's profile picture and 'about' for a
    user's bio.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model,
                              linking each UserProfile to a specific user.
        profile_image (CloudinaryField): A field for storing the user's profile image.
                                         It uses Cloudinary for image storage and
                                         has a default placeholder image.
        about (TextField): A text field where users can provide information about themselves.
                          It is optional and can be left blank.

    Methods:
        __str__: Returns the username of the associated user, used for display purposes.

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    about = models.TextField("About me", blank=True)

    def __str__(self):
        return self.user.username
