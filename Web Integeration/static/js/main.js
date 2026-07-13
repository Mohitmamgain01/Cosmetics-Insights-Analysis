// Subtle scroll-reveal for the KPI pans and gallery — respects reduced motion.
(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const targets = document.querySelectorAll('.pan, .gallery__item, .embed-section__head');

  if (prefersReduced || !('IntersectionObserver' in window)) {
    targets.forEach((el) => el.style.opacity = 1);
    return;
  }

  targets.forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = (el.style.transform || '') + ' translateY(10px)';
    el.style.transition = 'opacity .5s ease, transform .5s ease';
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = entry.target.style.transform.replace('translateY(10px)', 'translateY(0)');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  targets.forEach((el) => observer.observe(el));
})();
