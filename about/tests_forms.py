from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.


class TestCollaborateForm(TestCase):
    """
    Test case for the CollaborateForm.

    Attributes:
    attribute1 (type): description
    attribute2 (type): description
    """
    def test_form_is_valid(self):
        """
        Test if the form is valid with all fields filled.
        """
        form = CollaborateForm(
            {'name': 'test', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """
        Test if the 'name' field is required.
        """
        form = CollaborateForm(
            {'name': '', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid")

    def test_email_is_required(self):
        """
        Test if the 'email' field is required.
        """
        form = CollaborateForm(
            {'name': 'SP4RT4N', 'email': '', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid")

    def test_message_is_required(self):
        """
        Test if the 'message' field is required.
        """
        form = CollaborateForm(
            {'name': 'SP4RT4N', 'email': 'test@test.com', 'message': ''})
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid")

    def test_form_is_valid_without_phone(self):
        """
        Test if the form is valid with the phone field not filled.
        """
        form = CollaborateForm(
            {'name': 'SP4RT4N', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertTrue(form.is_valid(),
                        msg="Form should be valid even without phone number")

    def test_form_is_valid_with_phone(self):
        """
        Test if the form is valid with all fields filled, including phone.
        """
        form = CollaborateForm(
            {'name': 'test',
             'email': 'test@test.com',
             'phone': '123456789',
             'message': 'Hello!'})
        self.assertTrue(form.is_valid(),
                        msg="Form with phone number is not valid")
