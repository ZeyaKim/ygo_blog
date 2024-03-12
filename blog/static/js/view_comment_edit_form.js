document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.comment-edit-btn').forEach(function (button) {
    button.addEventListener('click', function () {
      var commentId = this.parentElement.parentElement.id.split('-')[1];
      var displayDiv = document.querySelector('#comment-' + commentId + ' .comment-display');
      var editForm = document.querySelector('#comment-' + commentId + ' .comment-edit-form');
      displayDiv.style.display = 'none'; // 기존 댓글 내용을 숨김
      editForm.style.display = 'block'; // 수정 폼을 표시
    });
  });

  document.querySelectorAll('.comment-edit-cancel-btn').forEach(function (button) {
    button.addEventListener('click', function () {
      var commentId = this.closest('.card').id.split('-')[1];  // 변경된 부분
      var displayDiv = document.querySelector('#comment-' + commentId + ' .comment-display');
      var editForm = document.querySelector('#comment-' + commentId + ' .comment-edit-form');
      displayDiv.style.display = 'block'; // 기존 댓글 내용을 다시 표시
      editForm.style.display = 'none'; // 수정 폼을 숨김
    });
  });

  document.querySelectorAll('.reply-btn').forEach(function (button) {
    button.addEventListener('click', function () {
      var commentId = this.getAttribute('data-comment-id');
      var replyForm = document.getElementById('reply-form-' + commentId);
      replyForm.classList.toggle('d-none'); // Bootstrap의 d-none 클래스를 토글합니다.
    });
  });

  document.querySelectorAll('.reply-cancel-btn').forEach(function (button) {
    button.addEventListener('click', function () {
      var commentId = this.dataset.commentId;
      var replyForm = document.getElementById('reply-form-' + commentId);
      replyForm.classList.add('d-none'); // Bootstrap의 d-none 클래스를 토글합니다.
    });
  });

  document.querySelectorAll('.subcomment-edit-btn').forEach(function(button) {
    button.addEventListener('click', function() {
      // Here, you'll need to correctly navigate to the parent .card element of the button
      var subcommentCard = this.closest('.card');
      // Now, target the .subcomment-display and .subcomment-edit-form classes within this card
      var displayDiv = subcommentCard.querySelector('.card-body'); // Assuming this is your display div
      var editForm = subcommentCard.nextElementSibling; // Assuming your edit form follows immediately after the card
      displayDiv.style.display = 'none'; // Hide the display div
      editForm.style.display = 'block'; // Show the edit form
    });
  });

  document.querySelectorAll('.subcomment-edit-cancel-btn').forEach(function(button) {
    button.addEventListener('click', function() {
      // Again, find the nearest .card element (this time, the form itself is part of what needs to be hidden)
      var subcommentCard = this.closest('.card').previousElementSibling; // Assuming the card that needs to be shown is immediately preceding the form
      // Now, toggle the display of .card-body and the form
      var displayDiv = subcommentCard.querySelector('.card-body');
      var editForm = this.closest('.subcomment-edit-form');
      displayDiv.style.display = 'block'; // Show the display div
      editForm.style.display = 'none'; // Hide the edit form
    });
  });

});
