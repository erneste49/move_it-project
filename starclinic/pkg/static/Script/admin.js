// // Simple administrator dashboard actions

// const doctorFormButton = document.querySelector('#doctors .form-action .btn');
// const specialtyFormButton = document.querySelector('#specialties .form-action .btn');

// const doctorNameInput = document.querySelector('#doctors input');
// const specialtyInput = document.querySelector('#specialties input');

// const doctorList = document.querySelector('#doctors .list');
// const specialtyList = document.querySelector('#specialties .list');

// // Add a new doctor to the list

// doctorFormButton.addEventListener('click', function () {
//     if (doctorNameInput.value.trim() === '') {
//         alert('Please enter the doctor name.');
//         return;
//     }

//     const newRow = document.createElement('div');
//     newRow.className = 'row';

//     newRow.innerHTML = `
//         <span>${doctorNameInput.value}</span>
//         <span>General Medicine</span>
//         <span class="badge green">Active</span>
//         <span class="actions">
//             <button class="btn btn-light mini">Edit</button>
//             <button class="btn btn-danger mini">Remove</button>
//         </span>
//     `;

//     doctorList.appendChild(newRow);
//     doctorNameInput.value = '';

//     addRemoveButton(newRow.querySelector('.btn-danger'));
//     addEditButton(newRow.querySelector('.btn-light'));

//     alert('Doctor added successfully!');
// });

// // Add a new specialty to the list

// specialtyFormButton.addEventListener('click', function () {
//     if (specialtyInput.value.trim() === '') {
//         alert('Please enter a specialty name.');
//         return;
//     }

//     const newRow = document.createElement('div');
//     newRow.className = 'row';

//     newRow.innerHTML = `
//         <span>${specialtyInput.value}</span>
//         <span>0</span>
//         <span class="badge green">Active</span>
//         <span>
//             <button class="btn btn-light mini">Edit</button>
//         </span>
//     `;

//     specialtyList.appendChild(newRow);
//     specialtyInput.value = '';

//     addEditButton(newRow.querySelector('.btn-light'));

//     alert('Specialty added successfully!');
// });

// // Remove a doctor

// document.querySelectorAll('#doctors .btn-danger').forEach(function (button) {
//     addRemoveButton(button);
// });

// // Edit buttons

// document.querySelectorAll('.btn-light').forEach(function (button) {
//     addEditButton(button);
// });

// function addRemoveButton(button) {
//     button.addEventListener('click', function () {
//         const answer = confirm('Are you sure you want to remove this item?');

//         if (answer) {
//             this.closest('.row').remove();
//         }
//     });
// }

// function addEditButton(button) {
//     button.addEventListener('click', function () {
//         alert('.');
//     });
// }

// // Patient view buttons

// document.querySelectorAll('#patients .btn-light').forEach(function (button) {
//     button.addEventListener('click', function () {
//         const patientName = this.closest('.row').children[0].textContent;
//         alert('Viewing information for ' + patientName + '.');
//     });
// });