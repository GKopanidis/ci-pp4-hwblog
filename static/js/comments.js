// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Initialize form and input elements
    const commentForm = document.getElementById("commentForm");
    const commentText = document.getElementById("id_body");
    const submitButton = document.getElementById("submitButton");
    // Initialize the delete confirmation modal using Bootstrap's Modal class
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal")); /*global bootstrap*/
    const deleteConfirm = document.getElementById("deleteConfirm");
    // Check if the user is authenticated by reading a data attribute from the body
    var userIsAuthenticated = document.body.getAttribute('data-user-authenticated') === 'true';

    // Event listener for all click events in the document
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('btn-edit')) {
            // Handle comment editing
            handleEdit(e);
        } else if (e.target.classList.contains('btn-delete')) {
            // Handle comment deletion
            handleDelete(e);
        } else if (e.target.classList.contains('auth-required')) {
            // Prevent default action and redirect to login if the user is not authenticated
            e.preventDefault();
            if (!userIsAuthenticated) {
                window.location.href = '/not_logged_in/';
            }
        }
    });

    // Function to handle editing comments
    function handleEdit(e) {
        // Retrieve comment ID and content
        const commentId = e.target.getAttribute("data-comment_id");
        const commentContent = document.getElementById(`comment${commentId}`).innerText;
        // Populate the form with the comment content and change the submit button text
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        // Update the form's action URL to target the edit_comment endpoint
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    }

    // Function to handle deletion confirmation
    function handleDelete(e) {
        // Retrieve the comment ID and set the confirmation link href
        const commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        // Show the delete confirmation modal
        deleteModal.show();
    }
});
