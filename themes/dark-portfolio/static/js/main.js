/* ── NAV: scroll class + active link ── */
const nav = document.getElementById('nav');
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__links a[href^="#"]');

window.addEventListener('scroll', () => {
  // Scrolled class for shadow
  nav.classList.toggle('scrolled', window.scrollY > 20);

  // Active link highlight
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
  });
  navLinks.forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === `#${current}`);
  });
}, { passive: true });

/* ── HAMBURGER MENU ── */
const hamburger = document.getElementById('hamburger');
const navLinkList = document.querySelector('.nav__links');

hamburger.addEventListener('click', () => {
  navLinkList.classList.toggle('open');
});

// Close on link click
navLinkList.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => navLinkList.classList.remove('open'));
});

/* ── SCROLL REVEAL ── */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.card, .stat-card, .section-header, .hero__content').forEach((el, i) => {
  el.classList.add('reveal');
  if (i % 3 === 1) el.classList.add('reveal--delay-1');
  if (i % 3 === 2) el.classList.add('reveal--delay-2');
  revealObserver.observe(el);
});
