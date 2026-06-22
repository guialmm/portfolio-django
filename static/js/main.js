// Theme toggle
const toggle = document.getElementById('themeToggle');
const icon = toggle ? toggle.querySelector('.theme-icon') : null;
const html = document.documentElement;

const saved = localStorage.getItem('theme') || 'dark';
html.setAttribute('data-theme', saved);
if (icon) icon.textContent = saved === 'dark' ? '☀' : '☾';

if (toggle) {
  toggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    if (icon) icon.textContent = next === 'dark' ? '☀' : '☾';
  });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="/#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href').replace('/', ''));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
