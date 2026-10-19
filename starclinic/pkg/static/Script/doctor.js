// const acceptButtons = document.querySelectorAll('.btn-success');
// const rejectButtons = document.querySelectorAll('.btn-danger');
// const uploadButton = document.querySelector('#prescription .form-action .btn');
// const fileInput = document.querySelector('#prescription input[type="file"]');

// acceptButtons.forEach(function (button) {
//     button.addEventListener('click', function () {
//         const row = this.closest('.row');
//         const status = row.querySelector('.badge');

//         status.textContent = 'Accepted';
//         status.classList.remove('orange');
//         status.classList.add('green');

//         this.remove();
//     });
// });

// rejectButtons.forEach(function (button) {
//     button.addEventListener('click', function () {
//         const answer = confirm('Are you sure you want to reject this appointment?');

//         if (answer) {
//             const row = this.closest('.row');
//             row.remove();
//         }
//     });
// });

// uploadButton.addEventListener('click', function () {
//     if (fileInput.files.length === 0) {
//         alert('Please select a document first.');
//         return;
//     }

//     alert('Document uploaded successfully!');
// });