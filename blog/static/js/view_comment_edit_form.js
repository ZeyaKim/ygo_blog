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
});
