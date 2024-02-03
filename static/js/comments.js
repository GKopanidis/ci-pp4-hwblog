document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById("commentForm");
    const commentText = document.getElementById("id_body");
    const submitButton = document.getElementById("submitButton");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");
    var userIsAuthenticated = document.body.getAttribute('data-user-authenticated') === 'true';

    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('btn-edit')) {
            handleEdit(e);
        } else if (e.target.classList.contains('btn-delete')) {
            handleDelete(e);
        } else if (e.target.classList.contains('auth-required')) {
            e.preventDefault();
            if (!userIsAuthenticated) {
                window.location.href = '/not_logged_in/';
            }
        }
    });

    function handleEdit(e) {
        const commentId = e.target.getAttribute("data-comment_id");
        const commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    }

    function handleDelete(e) {
        const commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    }
});
