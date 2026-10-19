// const appointmentButton = document.querySelector('#appointments .form-action .btn');
// const uploadButton = document.querySelector('#documents .form-action .btn');
// const paymentButton = document.querySelector('#payment .form-action .btn');
// const appointmentDate = document.querySelector('#appointments input[type="date"]');
// const fileInput = document.querySelector('#documents input[type="file"]');

// appointmentButton.addEventListener('click', function () {
//     if (appointmentDate.value === '') {
//         alert('Please choose an appointment date.');
//         return;
//     }

//     alert('Appointment booked successfully!');
// });

// const cancelButtons = document.querySelectorAll('#history .btn-danger');

// cancelButtons.forEach(function (button) {
//     button.addEventListener('click', function () {
//         const answer = confirm('Are you sure you want to cancel this appointment?');

//         if (answer) {
//             this.closest('.row').remove();
//             alert('Appointment cancelled.');
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

// paymentButton.addEventListener('click', function () {
//     alert('.');
// });