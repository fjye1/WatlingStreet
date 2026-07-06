const hero = document.querySelector('.hero-container');

window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    hero.classList.add('shrink');
  } else if (window.scrollY < 5) {
    hero.classList.remove('shrink');
  }
}, { passive: true });

// ─── Fade-in on scroll ─────────────────────────────
const fadeEls = document.querySelectorAll('.fade-text');

const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // fadeObserver.unobserve(entry.target); // uncomment if you only want it to fade in once
    }
  });
}, {
  threshold: 0.15
});

fadeEls.forEach(el => fadeObserver.observe(el));