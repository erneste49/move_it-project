/* ============================================
   HomeOwner Foundation — Main JavaScript
   Mobile menu, sticky navbar, scroll reveal
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ============ MOBILE MENU TOGGLE ============

  const navToggle = document.getElementById('nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navOverlay = document.getElementById('nav-overlay');
  const navLinks = document.querySelectorAll('.navbar__links a');

  function openMenu() {
    navToggle.classList.add('open');
    navToggle.setAttribute('aria-expanded', 'true');
    navMenu.classList.add('open');
    navOverlay.classList.add('visible');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    navToggle.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
    navMenu.classList.remove('open');
    navOverlay.classList.remove('visible');
    document.body.style.overflow = '';
  }

  if (navToggle) {
    navToggle.addEventListener('click', () => {
      const isOpen = navToggle.classList.contains('open');
      isOpen ? closeMenu() : openMenu();
    });
  }

  if (navOverlay) {
    navOverlay.addEventListener('click', closeMenu);
  }

  // Close mobile menu when a link is clicked
  navLinks.forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  // Close menu on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navToggle && navToggle.classList.contains('open')) {
      closeMenu();
    }
  });


  // ============ STICKY NAVBAR SCROLL EFFECT ============

  const navbar = document.getElementById('navbar');

  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }, { passive: true });
  }


  // ============ SCROLL REVEAL ANIMATION ============
  // Elements with class "reveal" fade in when they enter the viewport

  const revealElements = document.querySelectorAll('.reveal');

  if (revealElements.length > 0 && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback: show all elements if IntersectionObserver not supported
    revealElements.forEach(el => el.classList.add('revealed'));
  }


  // ============ ANIMATED STAT COUNTERS ============
  // Counts up numbers for elements with data-count attribute

  const statNumbers = document.querySelectorAll('[data-count]');

  if (statNumbers.length > 0 && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(el => counterObserver.observe(el));
  }

  function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-count'), 10);
    const suffix = element.getAttribute('data-suffix') || '';
    const duration = 2000; // 2 seconds
    const startTime = performance.now();

    function updateCount(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Ease-out cubic for smooth deceleration
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);

      element.textContent = current.toLocaleString() + suffix;

      if (progress < 1) {
        requestAnimationFrame(updateCount);
      } else {
        element.textContent = target.toLocaleString() + suffix;
      }
    }

    requestAnimationFrame(updateCount);
  }


  // ============ ACTIVE NAVBAR LINK ============
  // Highlights the current page link in the navbar

  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  navLinks.forEach(link => {
    const linkPage = link.getAttribute('href');
    if (linkPage === currentPage) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });


  // ============ DONATE BUTTON ALERT ============
  // Show alert that donations are not yet being accepted

  const donateBtns = document.querySelectorAll('.donate-btn');

  donateBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      alert('Thank you for your generosity! We are not receiving donations currently as we are setting up our account. Please check back soon or contact us for more information.');
    });
  });

});
