from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    A form class for users to submit requests for collaboration.

    This form is linked to the `CollaborateRequest` model, allowing users to
    provide their name, email, phone number, and a message detailing their
    collaboration request.

    Attributes:
        Meta: Provides metadata options to the form. Specifies the model
              (`CollaborateRequest`) and the order of fields to be displayed
              in the form.
    """

    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "phone", "message")
