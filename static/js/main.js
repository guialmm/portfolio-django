// ── Theme toggle ──
(function () {
  const html = document.documentElement;
  const btn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('icon-sun');
  const moonIcon = document.getElementById('icon-moon');

  const saved = localStorage.getItem('theme') || 'dark';
  applyTheme(saved);

  if (btn) {
    btn.addEventListener('click', function () {
      const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem('theme', next);
    });
  }

  function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    if (!sunIcon || !moonIcon) return;
    if (theme === 'dark') {
      sunIcon.style.display = 'block';
      moonIcon.style.display = 'none';
    } else {
      sunIcon.style.display = 'none';
      moonIcon.style.display = 'block';
    }
  }
})();

// ── Reveal on scroll ──
(function () {
  const items = document.querySelectorAll('.reveal');
  if (!items.length) return;

  const obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  items.forEach(function (el, i) {
    el.style.transitionDelay = (i * 60) + 'ms';
    obs.observe(el);
  });
})();

// ── Active nav link ──
(function () {
  const links = document.querySelectorAll('.nav-links a');
  const path = window.location.pathname;
  links.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href && href !== '/' && path.startsWith(href)) {
      link.classList.add('active');
    }
  });
})();
