/* =============================================================
   MEDASSIST AI — Main JavaScript
   All interactions: navbar, scroll-reveal, typewriter,
   counters, ripple, report actions, auto-dismiss.
   Guide wizard logic lives inline in guide.html.
   ============================================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Navbar scroll effect ── */
  const navbar = document.querySelector('.navbar-med');
  if (navbar) {
    const onScroll = () => navbar.classList.toggle('scrolled', window.scrollY > 40);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── Scroll reveal (IntersectionObserver) ── */
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.1 });
    revealEls.forEach(el => io.observe(el));
  }

  /* ── Typewriter (hero headline) ── */
  const typer = document.getElementById('typewriter');
  if (typer) {
    const phrases = ['You Need It.', 'Every Moment.', 'Anywhere.'];
    let pi = 0, ci = 0, del = false;
    const tick = () => {
      const cur = phrases[pi];
      typer.textContent = del ? cur.slice(0, ci--) : cur.slice(0, ci++);
      let ms = del ? 55 : 85;
      if (!del && ci > cur.length)  { ms = 1800; del = true; }
      if (del  && ci < 0)           { del = false; ci = 0; pi = (pi + 1) % phrases.length; ms = 350; }
      setTimeout(tick, ms);
    };
    tick();
  }

  /* ── Animated stat counters ── */
  document.querySelectorAll('[data-count]').forEach(el => {
    const io = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      io.disconnect();
      const target = parseInt(el.dataset.count, 10);
      const suffix = el.dataset.suffix || '';
      const dur    = 1500;
      const t0     = performance.now();
      const frame  = now => {
        const p = Math.min((now - t0) / dur, 1);
        el.textContent = Math.round((1 - Math.pow(1 - p, 3)) * target) + suffix;
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    }, { threshold: 0.6 });
    io.observe(el);
  });

  /* ── Ripple effect on primary buttons ── */
  document.querySelectorAll(
    '.btn-hero-primary, .btn-analyze, .btn-action-primary, .guide-submit-btn, .guide-next-btn, .btn-consult'
  ).forEach(btn => {
    btn.addEventListener('click', function (e) {
      const d    = Math.max(this.clientWidth, this.clientHeight);
      const rect = this.getBoundingClientRect();
      const rip  = document.createElement('span');
      rip.style.cssText = `
        position:absolute;pointer-events:none;
        width:${d}px;height:${d}px;border-radius:50%;
        left:${e.clientX - rect.left - d/2}px;
        top:${e.clientY  - rect.top  - d/2}px;
        background:rgba(255,255,255,0.22);
        transform:scale(0);animation:rip 0.55s linear;
      `;
      const prev = this.style.position;
      this.style.position = 'relative';
      this.style.overflow  = 'hidden';
      this.appendChild(rip);
      rip.addEventListener('animationend', () => { rip.remove(); this.style.position = prev; });
    });
  });

  /* ── Print report ── */
  const printBtn = document.getElementById('btn-print');
  if (printBtn) printBtn.addEventListener('click', () => window.print());

  /* ── Smooth scroll anchor links ── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

  /* ── Staggered entrance for report step items ── */
  document.querySelectorAll('.step-item').forEach((el, i) => {
    el.style.animationDelay = `${i * 80}ms`;
  });

  /* ── Stagger avoid/warning items ── */
  document.querySelectorAll('.avoid-item, .warning-item').forEach((el, i) => {
    el.style.opacity    = '0';
    el.style.transform  = 'translateY(12px)';
    el.style.transition = `opacity 0.4s ease ${i * 60}ms, transform 0.4s ease ${i * 60}ms`;
    const io = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      io.disconnect();
      el.style.opacity   = '1';
      el.style.transform = 'translateY(0)';
    }, { threshold: 0.2 });
    io.observe(el);
  });

  /* ── Auto-dismiss Django messages ── */
  setTimeout(() => {
    document.querySelectorAll('.alert-dismissible').forEach(alert => {
      alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      alert.style.opacity    = '0';
      alert.style.transform  = 'translateY(10px)';
      setTimeout(() => alert.remove(), 500);
    });
  }, 4500);

  /* ── Hospital card hover — subtle border glow ── */
  document.querySelectorAll('.hosp-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.borderColor = 'rgba(26,86,219,0.3)';
    });
    card.addEventListener('mouseleave', function() {
      this.style.borderColor = '';
    });
  });

  /* ── Video placeholder click feedback ── */
  document.querySelectorAll('.video-placeholder').forEach(vp => {
    vp.addEventListener('click', function() {
      const btn = this.querySelector('.video-play-btn');
      if (btn) {
        btn.style.transform  = 'scale(0.9)';
        btn.style.background = 'var(--primary)';
        setTimeout(() => { btn.style.transform = ''; }, 200);
      }
    });
  });

});

/* ── Ripple keyframe (injected once) ── */
const s = document.createElement('style');
s.textContent = '@keyframes rip{to{transform:scale(4);opacity:0}}';
document.head.appendChild(s);
