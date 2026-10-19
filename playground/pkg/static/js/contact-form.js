/* ============================================
   HomeOwner Foundation — Contact Form Validation
   Client-side validation with inline error messages
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  const form = document.getElementById('contact-form');
  if (!form) return;

  const submitBtn = document.getElementById('contact-submit');
  const submitText = form.querySelector('.contact__submit-text');
  const submitLoading = form.querySelector('.contact__submit-loading');
  const successMessage = document.getElementById('contact-success');

  // Field definitions
  const fields = [
    {
      input: document.getElementById('contact-name'),
      error: document.getElementById('name-error'),
      validate: (value) => value.trim().length >= 2,
      message: 'Please enter your full name (at least 2 characters)'
    },
    {
      input: document.getElementById('contact-email'),
      error: document.getElementById('email-error'),
      validate: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim()),
      message: 'Please enter a valid email address'
    },
    {
      input: document.getElementById('contact-subject'),
      error: document.getElementById('subject-error'),
      validate: (value) => value.trim().length >= 3,
      message: 'Please enter a subject (at least 3 characters)'
    },
    {
      input: document.getElementById('contact-message'),
      error: document.getElementById('message-error'),
      validate: (value) => value.trim().length >= 10,
      message: 'Please enter a message (at least 10 characters)'
    }
  ];

  // ---- Real-time validation on blur ----
  fields.forEach(field => {
    if (!field.input) return;

    field.input.addEventListener('blur', () => {
      validateField(field);
    });

    // Clear error on focus
    field.input.addEventListener('focus', () => {
      clearFieldError(field);
    });
  });

  // ---- Form submission ----
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Validate all fields
    let isValid = true;
    fields.forEach(field => {
      if (!validateField(field)) {
        isValid = false;
      }
    });

    if (!isValid) {
      // Focus first invalid field
      const firstInvalid = fields.find(f => f.input && f.input.parentElement.classList.contains('has-error'));
      if (firstInvalid) {
        firstInvalid.input.focus();
      }
      return;
    }

    // Simulate form submission
    submitForm();
  });

  // ---- Validate a single field ----
  function validateField(field) {
    if (!field.input) return true;

    const value = field.input.value;

    if (!field.validate(value)) {
      showFieldError(field);
      return false;
    }

    clearFieldError(field);
    return true;
  }

  // ---- Show field error ----
  function showFieldError(field) {
    field.input.parentElement.classList.add('has-error');
    if (field.error) {
      field.error.textContent = field.message;
      field.error.style.display = 'block';
    }
  }

  // ---- Clear field error ----
  function clearFieldError(field) {
    field.input.parentElement.classList.remove('has-error');
    if (field.error) {
      field.error.style.display = 'none';
    }
  }

  // ---- Simulate form submission ----
  function submitForm() {
    // Show loading state
    submitBtn.disabled = true;
    if (submitText) submitText.style.display = 'none';
    if (submitLoading) submitLoading.style.display = 'inline';

    // Simulate network delay
    setTimeout(() => {
      // Reset button state
      submitBtn.disabled = false;
      if (submitText) submitText.style.display = 'inline';
      if (submitLoading) submitLoading.style.display = 'none';

      // Show success message
      if (successMessage) {
        successMessage.style.display = 'flex';
      }

      // Reset form
      form.reset();

      // Hide success after 5 seconds
      setTimeout(() => {
        if (successMessage) {
          successMessage.style.display = 'none';
        }
      }, 5000);

    }, 1500);
  }

});
