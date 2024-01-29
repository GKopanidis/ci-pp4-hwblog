from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text.

    Attributes:
        title (CharField): The title of the about me text.
        profile_image (CloudinaryField): The profile image associated with the about me text.
        updated_on (DateTimeField): The date and time the about me text was last updated.
        content (TextField): The content of the about me text.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return str(self.title)


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message.

    Attributes:
        name (CharField): The name of the person requesting collaboration.
        email (EmailField): The email of the person requesting collaboration.
        message (TextField): The collaboration request message.
        phone (CharField): The phone number of the person requesting collaboration (optional).
        read (BooleanField): Whether the collaboration request has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
