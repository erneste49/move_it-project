// const loginForm = document.querySelector('form');
// const loginButton = document.querySelector('.btn.full');
// const roleSelect = document.querySelector('select');
// const emailInput = document.querySelector('input[type="email"]');
// const passwordInput = document.querySelector('input[type="password"]');

// const savedRole = localStorage.getItem('loginRole');

// if (savedRole) {
//     if (savedRole === 'Doctor') {
//         roleSelect.value = 'Doctor';
//     } else if (savedRole === 'Administrator') {
//         roleSelect.value = 'Administrator';
//     } else {
//         roleSelect.value = 'Patient';
//     }
// }

// loginForm.addEventListener('submit', function (event) {
//     event.preventDefault();

//     if (emailInput.value === '' || passwordInput.value === '') {
//         alert('Please enter your email and password.');
//         return;
//     }

//     const role = roleSelect.value;
//     localStorage.setItem('loginRole', role);

//     if (role === 'Doctor') {
//         window.location.href = 'doctor.html';
//     } else if (role === 'Administrator') {
//         window.location.href = 'admin.html';
//     } else {
//         window.location.href = 'user.html';
//     }
// });

// const forgotPassword = document.querySelector('.form-line a');

// forgotPassword.addEventListener('click', function (event) {
//     event.preventDefault();
//     alert('Password reset would be handled by the backend.');
// });
