from django.test import TestCase
from .forms import CommentForm

# Create your tests here.


class TestCommentForm(TestCase):
    """
    Test case for the CommentForm.
    """
    def test_form_is_valid(self):
        """
        Test the validity of a CommentForm instance when providing a
        valid comment body.

        This function creates a CommentForm instance with a non-empty
        'body' field and checks whether it's considered valid.
        If the form is valid, the test passes; otherwise, it fails.

        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        """
        Test the validity of a CommentForm instance when providing
        an empty comment body.

        This function creates a CommentForm instance with an empty
        'body' field and checks whether it's considered invalid.
        If the form is invalid, the test passes; otherwise, it fails.

        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
