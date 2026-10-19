/* ============================================
   HomeOwner Foundation — Image Carousel
   Auto-play slider with arrows and dot navigation
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  const track = document.getElementById('carousel-track');
  const prevBtn = document.getElementById('carousel-prev');
  const nextBtn = document.getElementById('carousel-next');
  const dotsContainer = document.getElementById('carousel-dots');

  if (!track || !prevBtn || !nextBtn || !dotsContainer) return;

  const slides = track.querySelectorAll('.carousel__slide');
  const dots = dotsContainer.querySelectorAll('.carousel__dot');
  const totalSlides = slides.length;

  let currentIndex = 0;
  let autoPlayInterval = null;
  const AUTO_PLAY_DELAY = 5000; // 5 seconds

  // ---- Core Navigation ----

  function goToSlide(index) {
    if (index < 0) index = totalSlides - 1;
    if (index >= totalSlides) index = 0;

    currentIndex = index;
    track.style.transform = `translateX(-${currentIndex * 100}%)`;

    // Update dots
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentIndex);
      dot.setAttribute('aria-selected', i === currentIndex ? 'true' : 'false');
    });
  }

  function nextSlide() {
    goToSlide(currentIndex + 1);
  }

  function prevSlide() {
    goToSlide(currentIndex - 1);
  }

  // ---- Event Listeners ----

  prevBtn.addEventListener('click', () => {
    prevSlide();
    resetAutoPlay();
  });

  nextBtn.addEventListener('click', () => {
    nextSlide();
    resetAutoPlay();
  });

  // Dot click navigation
  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      goToSlide(index);
      resetAutoPlay();
    });
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    const carousel = document.getElementById('carousel');
    if (!carousel) return;

    // Only respond to keyboard when carousel is in view
    const rect = carousel.getBoundingClientRect();
    const inView = rect.top < window.innerHeight && rect.bottom > 0;

    if (!inView) return;

    if (e.key === 'ArrowLeft') {
      prevSlide();
      resetAutoPlay();
    } else if (e.key === 'ArrowRight') {
      nextSlide();
      resetAutoPlay();
    }
  });

  // ---- Auto-Play ----

  function startAutoPlay() {
    autoPlayInterval = setInterval(nextSlide, AUTO_PLAY_DELAY);
  }

  function stopAutoPlay() {
    if (autoPlayInterval) {
      clearInterval(autoPlayInterval);
      autoPlayInterval = null;
    }
  }

  function resetAutoPlay() {
    stopAutoPlay();
    startAutoPlay();
  }

  // Pause auto-play on hover
  const carousel = document.getElementById('carousel');
  if (carousel) {
    carousel.addEventListener('mouseenter', stopAutoPlay);
    carousel.addEventListener('mouseleave', startAutoPlay);

    // Pause on focus (accessibility)
    carousel.addEventListener('focusin', stopAutoPlay);
    carousel.addEventListener('focusout', startAutoPlay);
  }

  // ---- Touch / Swipe Support ----

  let touchStartX = 0;
  let touchEndX = 0;
  const SWIPE_THRESHOLD = 50;

  if (track) {
    track.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      stopAutoPlay();
    }, { passive: true });

    track.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;

      if (Math.abs(diff) > SWIPE_THRESHOLD) {
        if (diff > 0) {
          nextSlide();
        } else {
          prevSlide();
        }
      }
      startAutoPlay();
    }, { passive: true });
  }

  // ---- Initialize ----
  goToSlide(0);
  startAutoPlay();

});
