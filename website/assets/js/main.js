// ARASI v1 — perilaku bersama: menu mobile, tahun footer, form kontak, tombol "minta penawaran", filter.
(function () {
  var CONTACT_EMAIL = 'admin@arasinusa.co.id';

  document.addEventListener('DOMContentLoaded', function () {
    // Menu mobile: panel bisa di-scroll, halaman dikunci saat terbuka
    var btn = document.querySelector('[data-menu-toggle]');
    var menu = document.querySelector('[data-menu]');
    if (btn && menu) {
      var setOpen = function (open) {
        menu.classList.toggle('hidden', !open);
        document.documentElement.classList.toggle('menu-open', open);
        btn.setAttribute('aria-expanded', String(open));
        btn.setAttribute('aria-label', open ? 'Tutup menu' : 'Buka menu');
        btn.querySelector('.material-symbols-outlined').textContent = open ? 'close' : 'menu';
        if (open) menu.scrollTop = 0;
      };
      btn.addEventListener('click', function () { setOpen(menu.classList.contains('hidden')); });
      menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
      menu.addEventListener('click', function (e) { if (e.target === menu) setOpen(false); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.classList.contains('hidden')) { setOpen(false); btn.focus(); } });
      window.addEventListener('resize', function () { if (window.innerWidth >= 1280) setOpen(false); });
      menu.querySelectorAll('.m-expand').forEach(function (x) {
        x.addEventListener('click', function () {
          var sub = document.getElementById(x.getAttribute('aria-controls'));
          var open = x.getAttribute('aria-expanded') !== 'true';
          x.setAttribute('aria-expanded', String(open));
          sub.hidden = !open;
        });
      });
    }

    // Tahun footer
    document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

    // Form kontak: susun email ke tim ARASI (situs statis, tidak ada server)
    document.querySelectorAll('form[data-contact-form]').forEach(function (form) {
      var status = form.querySelector('[data-form-status]');
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!form.reportValidity()) return;
        var d = new FormData(form);
        var kategori = d.get('kategori') || 'Umum';
        var subject = 'Permintaan konsultasi: ' + kategori + ' (' + d.get('perusahaan') + ')';
        var body = [
          'Nama: ' + d.get('nama'),
          'Perusahaan: ' + d.get('perusahaan'),
          'Email: ' + d.get('email'),
          'Telepon/WhatsApp: ' + d.get('telepon'),
          'Kategori: ' + kategori,
          '',
          'Kebutuhan:',
          d.get('pesan')
        ].join('\n');
        window.location.href = 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
        if (status) {
          status.hidden = false;
          status.innerHTML = 'Aplikasi email Anda sedang dibuka dengan pesan yang sudah terisi. Kalau tidak terbuka, kirim langsung ke <a class="underline font-semibold" href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a> atau telepon (021) 897 74919.';
          status.focus();
        }
      });
    });

    // Tombol "Minta penawaran": isi kategori + pesan di form kontak
    document.querySelectorAll('[data-quote]').forEach(function (el) {
      el.addEventListener('click', function () {
        var form = document.querySelector('form[data-contact-form]');
        if (!form) return;
        var sel = form.querySelector('select[name="kategori"]');
        var msg = form.querySelector('textarea[name="pesan"]');
        if (sel && el.getAttribute('data-kategori')) sel.value = el.getAttribute('data-kategori');
        if (msg) msg.value = 'Mohon penawaran untuk: ' + el.getAttribute('data-quote') + '\nJumlah / spesifikasi: ';
      });
    });

    // Filter generik: [data-filter-group] berisi tombol [data-filter], item [data-cat], hitungan [data-filter-count]
    document.querySelectorAll('[data-filter-group]').forEach(function (group) {
      var scope = document.getElementById(group.getAttribute('data-filter-group'));
      if (!scope) return;
      var buttons = group.querySelectorAll('[data-filter]');
      var count = document.querySelector('[data-filter-count="' + group.getAttribute('data-filter-group') + '"]');
      var search = document.querySelector('[data-filter-search="' + group.getAttribute('data-filter-group') + '"]');
      var empty = scope.parentNode.querySelector('[data-filter-empty]');
      var current = 'all';
      function apply() {
        var q = search ? search.value.trim().toLowerCase() : '';
        var n = 0;
        scope.querySelectorAll('[data-cat]').forEach(function (item) {
          var okCat = current === 'all' || item.getAttribute('data-cat') === current;
          var okQ = !q || item.textContent.toLowerCase().indexOf(q) !== -1;
          var show = okCat && okQ;
          item.hidden = !show;
          if (show) n++;
        });
        if (count) count.textContent = n;
        if (empty) empty.hidden = n !== 0;
      }
      buttons.forEach(function (b) {
        b.addEventListener('click', function () {
          current = b.getAttribute('data-filter');
          buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          apply();
        });
      });
      if (search) search.addEventListener('input', apply);
    });
    // Carousel manual: [data-carousel] berisi .tf-slide, [data-prev]/[data-next], .tf-dot[data-go], [data-count]
    document.querySelectorAll('[data-carousel]').forEach(function (c) {
      var slides = c.querySelectorAll('.tf-slide');
      var dots = c.querySelectorAll('[data-go]');
      var count = c.querySelector('[data-count]');
      var i = 0;
      function go(n) {
        i = (n + slides.length) % slides.length;
        slides.forEach(function (s, k) { s.hidden = k !== i; });
        dots.forEach(function (d, k) { if (k === i) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
        if (count) count.textContent = (i + 1) + ' / ' + slides.length;
        var img = slides[i].querySelectorAll('img[loading="lazy"]');
        img.forEach(function (im) { im.loading = 'eager'; });
      }
      var prev = c.querySelector('[data-prev]'), next = c.querySelector('[data-next]');
      if (prev) prev.addEventListener('click', function () { go(i - 1); });
      if (next) next.addEventListener('click', function () { go(i + 1); });
      dots.forEach(function (d) { d.addEventListener('click', function () { go(+d.getAttribute('data-go')); }); });
      c.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') { go(i - 1); } else if (e.key === 'ArrowRight') { go(i + 1); }
      });
      var x0 = null;
      c.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
      c.addEventListener('touchend', function (e) {
        if (x0 === null) return;
        var dx = e.changedTouches[0].clientX - x0; x0 = null;
        if (Math.abs(dx) > 40) go(dx < 0 ? i + 1 : i - 1);
      });
    });
    // Slider foto/video proyek: [data-slider] > .slides (scroll-snap) + [data-sl-prev]/[data-sl-next] + [data-sl-go]
    document.querySelectorAll('[data-slider]').forEach(function (sl) {
      var track = sl.querySelector('.slides');
      var slides = track.children;
      var dots = sl.querySelectorAll('[data-sl-go]');
      var prev = sl.querySelector('[data-sl-prev]'), next = sl.querySelector('[data-sl-next]');
      var i = 0, inView = false;
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) { inView = es[0].isIntersecting; sync(); }, { threshold: 0.4 }).observe(sl);
      }
      function idx() { return Math.round(track.scrollLeft / Math.max(1, track.clientWidth)); }
      function go(n) { n = Math.max(0, Math.min(slides.length - 1, n)); track.scrollTo({ left: n * track.clientWidth }); }
      function sync() {
        i = idx();
        dots.forEach(function (d, k) { if (k === i) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
        if (prev) prev.disabled = i === 0;
        if (next) next.disabled = i === slides.length - 1;
        Array.prototype.forEach.call(slides, function (s, k) {
          var v = s.querySelector('video');
          if (v) { if (k === i && inView) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } else if (!v.paused) v.pause(); }
          if (Math.abs(k - i) <= 1) s.querySelectorAll('img[loading="lazy"]').forEach(function (im) { im.loading = 'eager'; });
        });
      }
      function stop(e) { e.preventDefault(); e.stopPropagation(); }
      if (prev) prev.addEventListener('click', function (e) { stop(e); go(i - 1); });
      if (next) next.addEventListener('click', function (e) { stop(e); go(i + 1); });
      dots.forEach(function (d) { d.addEventListener('click', function (e) { stop(e); go(+d.getAttribute('data-sl-go')); }); });
      track.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') { e.preventDefault(); go(i - 1); } else if (e.key === 'ArrowRight') { e.preventDefault(); go(i + 1); }
      });
      var t; track.addEventListener('scroll', function () { clearTimeout(t); t = setTimeout(sync, 60); }, { passive: true });
      window.addEventListener('resize', function () { track.scrollLeft = i * track.clientWidth; });
      sync();
    });
  });
})();
