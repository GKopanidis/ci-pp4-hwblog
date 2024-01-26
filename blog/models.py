from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    @property
    def likes(self):
        return Like.objects.filter(post=self)

    def is_liked_by_user(self, user):
        return self.likes.filter(user=user).exists()

    def get_favorite_count(self):
        return Favorite.objects.filter(post=self).count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} favorited {self.post.title}"

    def get_favorite_count(self):
        return Favorite.objects.filter(post=self.post).count()
