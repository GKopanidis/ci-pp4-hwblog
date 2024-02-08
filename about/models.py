from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Model to store information about the site owner for an 'About Me' section.

    Represents an individual 'About Me' entry with a title, profile image,
    last updated timestamp, and detailed content. This model is ideal for
    personal websites or portfolios to share information about the site owner
    or their services.

    Attributes:
        title (CharField): Title of the 'About Me' entry.
        profile_image (CloudinaryField): Profile image associated with the
                                        'About Me' text, stored using
                                         Cloudinary.
        updated_on (DateTimeField): Timestamp indicating when the
                                    entry was last updated.
        Automatically set to now upon saving.
        content (TextField): Detailed 'About Me' content text.
    """

    title = models.CharField(max_length=200)
    profile_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return str(self.title)


class CollaborateRequest(models.Model):
    """
    Model to store requests from users seeking to collaborate.

    Each instance of this model captures essential information
    from users who wish to collaborate, including their name, email,
    optional phone number, and a detailed message. It also includes
    a 'read' status to track whether the request has been
    addressed.

    Attributes:
        name (CharField): Name of the person requesting collaboration.
        email (EmailField): Email address of the requester.
        message (TextField): Detailed message regarding the collaboration
                             request.
        phone (CharField): Optional phone number of the requester.
        read (BooleanField): Status flag indicating whether the request
                             has been read, defaulting to False.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
