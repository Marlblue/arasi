"""Rakit halaman v1: head + header + <main>(body fragment) + kontak + footer."""
import sys, os, html, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slider import slider

PAGES_DIR = os.path.join(os.path.dirname(__file__), 'pages')
OUT = sys.argv[1]

NAV = [
    ('index', 'index.html', 'Beranda'),
    ('solusi', 'solusi-industri.html', 'Solusi Industri'),
    ('portofolio', 'portofolio.html', 'Portofolio Proyek'),
    ('produk', 'produk.html', 'Produk Industri'),
    ('artikel', 'artikel.html', 'Artikel'),
    ('tentang', 'tentang-kami.html', 'Tentang Kami'),
]
SOLUSI_SUB = [
    ('solusi-industri.html#jig-fixture', 'Jig &amp; Fixture Custom'),
    ('solusi-industri.html#otomasi-robotik', 'Otomasi &amp; Integrasi Robotik'),
    ('solusi-industri.html#machining-fabrikasi', 'Machining &amp; Fabrikasi Custom'),
    ('solusi-industri.html#conveyor-modifikasi', 'Conveyor &amp; Modifikasi Fasilitas'),
]

PAGES = {
    'index': ('index.html', 'PT Arasi Nusantara Perkasa | Engineering, Machining, Fabrikasi &amp; General Supply Cikarang',
              'PT Arasi Nusantara Perkasa: jig &amp; fixture, machining, fabrikasi, integrasi otomasi, dan pengadaan barang industri untuk pabrik di Cikarang dan sekitarnya.'),
    'solusi': ('solusi-industri.html', 'Solusi Industri | PT Arasi Nusantara Perkasa',
               'Jig &amp; fixture custom, otomasi dan integrasi robotik, machining dan fabrikasi, serta conveyor dan modifikasi fasilitas produksi.'),
    'portofolio': ('portofolio.html', 'Portofolio Proyek | PT Arasi Nusantara Perkasa',
                   'Proyek jig &amp; fixture, fabrikasi, otomasi, dan modifikasi fasilitas yang dikerjakan PT Arasi Nusantara Perkasa untuk pabrik klien.'),
    'produk': ('produk.html', 'Produk Industri | PT Arasi Nusantara Perkasa',
               'Pengadaan komponen listrik, pneumatik, hidrolik, transmisi, pelumas, perkakas, dan custom part untuk kebutuhan produksi dan perawatan pabrik.'),
    'tentang': ('tentang-kami.html', 'Tentang Kami | PT Arasi Nusantara Perkasa',
                'Profil, visi misi, legalitas, fasilitas mesin, serta alamat kantor dan workshop PT Arasi Nusantara Perkasa di Cikarang Selatan.'),
    'artikel': ('artikel.html', 'Artikel | PT Arasi Nusantara Perkasa',
                'Catatan teknis tim engineering PT Arasi Nusantara Perkasa seputar jig, otomasi, perawatan, dan machining.'),
}

HEAD = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#001F4B">
  <link rel="icon" type="image/png" href="assets/img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&amp;display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <script src="assets/js/tailwind.config.js"></script>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="min-h-screen flex flex-col">
<a href="#konten" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-[60] focus:bg-white focus:px-4 focus:py-2 focus:rounded-md focus:shadow">Langsung ke konten</a>
'''


def header(active):
    links = []
    mobile = []
    for key, href, label in NAV:
        cur = ' aria-current="page"' if key == active else ''
        if key == 'solusi':
            sub = ''.join(f'<a href="{h}">{l}</a>' for h, l in SOLUSI_SUB)
            links.append(
                f'<div class="dropdown"><a class="nav-link" href="{href}"{cur}>{label}'
                f'<span class="material-symbols-outlined" aria-hidden="true">expand_more</span></a>'
                f'<div class="dropdown-menu">{sub}</div></div>')
            subs = ''.join(f'<a class="m-link m-sub" href="{h}">{l}</a>' for h, l in SOLUSI_SUB)
            mobile.append(
                f'<div class="m-row"><a class="m-link" href="{href}"{cur}>{label}</a>'
                f'<button type="button" class="m-expand" aria-expanded="false" aria-controls="m-sub-solusi" aria-label="Tampilkan sub-menu Solusi Industri">'
                f'<span class="material-symbols-outlined" aria-hidden="true">expand_more</span></button></div>'
                f'<div id="m-sub-solusi" class="m-sub-list" hidden>{subs}</div>')
        else:
            links.append(f'<a class="nav-link" href="{href}"{cur}>{label}</a>')
            mobile.append(f'<a class="m-link" href="{href}"{cur}>{label}</a>')
    return f'''<header class="site-header">
  <div class="wrap bar">
    <a class="site-logo" href="index.html" aria-label="PT Arasi Nusantara Perkasa, ke beranda"><img alt="PT Arasi Nusantara Perkasa" src="assets/img/logo.png" width="900" height="187"></a>
    <nav class="nav-desktop" aria-label="Navigasi utama">
      {"".join(links)}
    </nav>
    <div class="flex items-center gap-2">
      <a class="btn btn-primary btn-sm header-cta" href="#kontak">Diskusikan Proyek</a>
      <button type="button" class="menu-toggle" data-menu-toggle aria-label="Buka menu" aria-expanded="false" aria-controls="menu-mobile"><span class="material-symbols-outlined" aria-hidden="true">menu</span></button>
    </div>
  </div>
  <nav id="menu-mobile" class="nav-mobile hidden" data-menu aria-label="Navigasi utama (mobile)">
    <div class="wrap">
      {"".join(mobile)}
      <a class="btn btn-primary btn-block mt-5" href="#kontak">Diskusikan Proyek</a>
    </div>
  </nav>
</header>
'''


KATEGORI = ['Jig &amp; Fixture Custom', 'Otomasi &amp; Integrasi Robotik', 'Machining &amp; Fabrikasi Custom',
            'Conveyor &amp; Modifikasi Fasilitas', 'Pengadaan Produk / Suku Cadang', 'Lainnya']


def contact(pid):
    opts = ''.join(f'<option>{k}</option>' for k in KATEGORI)
    f = lambda n: f'{n}-{pid}'
    return f'''<section id="kontak" class="section bg-navy on-navy" aria-labelledby="kontak-judul">
  <div class="wrap grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-start">
    <div class="lg:col-span-5">
      <h2 id="kontak-judul" class="h-section">Diskusikan kebutuhan lini produksi Anda</h2>
      <p class="lede">Kirim gambar teknik, sampel, atau ringkasan masalah di lini. Tim engineering kami meninjau, lalu menjadwalkan survei ke pabrik bila diperlukan.</p>
      <dl class="mt-8 grid gap-5 text-[15px]">
        <div class="flex gap-3"><span class="material-symbols-outlined text-white/80 mt-0.5" aria-hidden="true">mail</span><div><dt class="sr-only">Email</dt><dd><a class="font-semibold text-white underline-offset-4 hover:underline" href="mailto:admin@arasinusa.co.id">admin@arasinusa.co.id</a></dd></div></div>
        <div class="flex gap-3"><span class="material-symbols-outlined text-white/80 mt-0.5" aria-hidden="true">call</span><div><dt class="sr-only">Telepon</dt><dd><a class="font-semibold text-white underline-offset-4 hover:underline" href="tel:+622189774919">(021) 897 74919</a></dd></div></div>
        <div class="flex gap-3"><span class="material-symbols-outlined text-white/80 mt-0.5" aria-hidden="true">location_on</span><div><dt class="sr-only">Kantor</dt><dd class="text-[#C9D3E3] leading-relaxed">Ruko Lafenza Villa Mutiara Cikarang 1 Blok R4 No. 36, Cikarang Selatan, Kab. Bekasi</dd></div></div>
      </dl>
    </div>
    <div class="lg:col-span-7">
      <form class="surface bg-white text-[#0F172A] rounded-lg p-6 md:p-8 grid gap-5" data-contact-form>
        <div>
          <h3 class="h-card">Form konsultasi proyek</h3>
          <p class="body-sm mt-1">Kolom bertanda <span class="text-[#CC0000] font-semibold">*</span> wajib diisi.</p>
        </div>
        <div class="grid sm:grid-cols-2 gap-5">
          <div class="field"><label for="{f('nama')}">Nama lengkap <span class="req">*</span></label><input id="{f('nama')}" name="nama" type="text" autocomplete="name" required></div>
          <div class="field"><label for="{f('perusahaan')}">Perusahaan <span class="req">*</span></label><input id="{f('perusahaan')}" name="perusahaan" type="text" autocomplete="organization" required></div>
          <div class="field"><label for="{f('email')}">Email kantor <span class="req">*</span></label><input id="{f('email')}" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="{f('telepon')}">Telepon / WhatsApp <span class="req">*</span></label><input id="{f('telepon')}" name="telepon" type="tel" inputmode="tel" autocomplete="tel" pattern="[0-9+()\\-\\s]{{8,20}}" placeholder="08xx xxxx xxxx" required></div>
        </div>
        <div class="field"><label for="{f('kategori')}">Jenis kebutuhan</label><select id="{f('kategori')}" name="kategori">{opts}</select></div>
        <div class="field"><label for="{f('pesan')}">Ringkasan kebutuhan <span class="req">*</span></label><textarea id="{f('pesan')}" name="pesan" rows="4" required placeholder="Proses, part, material, jumlah, atau masalah yang ingin diselesaikan."></textarea></div>
        <div class="form-status ok" data-form-status role="status" tabindex="-1" hidden></div>
        <div class="flex flex-col sm:flex-row sm:items-center gap-4">
          <button class="btn btn-primary" type="submit"><span class="material-symbols-outlined" aria-hidden="true">send</span>Kirim permintaan</button>
          <p class="body-sm">Tombol ini membuka aplikasi email Anda dengan pesan yang sudah terisi.</p>
        </div>
      </form>
    </div>
  </div>
</section>
'''


def footer():
    nav = ''.join(f'<li><a href="{h}">{l}</a></li>' for _, h, l in NAV)
    sol = ''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in SOLUSI_SUB)
    return f'''<footer class="site-footer">
  <div class="wrap py-14 grid gap-10 md:grid-cols-2 lg:grid-cols-12">
    <div class="lg:col-span-4">
      <img src="assets/img/logo-white.png" alt="PT Arasi Nusantara Perkasa" class="h-10 w-auto" width="900" height="187" loading="lazy">
      <p class="mt-5 text-[15px] leading-relaxed max-w-xs">Engineering, machining, precision tools, fabrication, dan general supply untuk industri manufaktur.</p>
    </div>
    <div class="lg:col-span-2">
      <h3>Navigasi</h3>
      <ul class="grid gap-2.5 text-[15px]">{nav}</ul>
    </div>
    <div class="lg:col-span-3">
      <h3>Solusi</h3>
      <ul class="grid gap-2.5 text-[15px]">{sol}</ul>
    </div>
    <div class="lg:col-span-3">
      <h3>Kontak</h3>
      <ul class="grid gap-2.5 text-[15px] leading-relaxed">
        <li><a href="mailto:admin@arasinusa.co.id">admin@arasinusa.co.id</a></li>
        <li><a href="tel:+622189774919">(021) 897 74919</a></li>
        <li><a href="https://www.arasinusa.co.id" target="_blank" rel="noopener noreferrer">www.arasinusa.co.id</a></li>
        <li class="pt-2"><span class="text-white font-semibold">Kantor</span><br>Ruko Lafenza Villa Mutiara Cikarang 1 Blok R4 No. 36, Cikarang Selatan, Kab. Bekasi</li>
        <li><span class="text-white font-semibold">Workshop</span><br>Kp. Nambo RT 011/RW 008, Sukasejati, Cikarang Selatan, Kab. Bekasi</li>
      </ul>
    </div>
  </div>
  <div class="border-t border-white/10">
    <div class="wrap py-6 text-sm">© <span data-year>2026</span> PT Arasi Nusantara Perkasa. Seluruh hak dilindungi.</div>
  </div>
</footer>
'''


def render(pid, fname, title, desc, active):
    frag = os.path.join(PAGES_DIR, pid + '.html')
    if not os.path.exists(frag):
        return
    body = open(frag, encoding='utf-8').read()
    # <!--SLIDER|key|kelas media|kelas img pertama--> diganti markup slider (lihat slider.py)
    body = re.sub(r'<!--SLIDER\|([\w-]+)\|([^|>]*)\|?([^>]*?)-->', lambda m: slider(m.group(1), m.group(2), m.group(3)), body)
    extra = ''
    if '<!--SCRIPTS-->' in body:
        body, extra = body.split('<!--SCRIPTS-->', 1)
    doc = (HEAD.format(title=title, desc=desc) + header(active) +
           '<main id="konten" class="flex-grow">\n' + body + '\n</main>\n' +
           contact(pid) + footer() + extra + '<script src="assets/js/main.js"></script>\n</body>\n</html>\n')
    open(os.path.join(OUT, fname), 'w', encoding='utf-8', newline='\n').write(doc)
    print('built', fname, len(doc))


for pid, (fname, title, desc) in PAGES.items():
    render(pid, fname, title, desc, pid)

# Halaman tambahan (detail artikel) dari gen_artikel.py
import json
_extra = os.path.join(os.path.dirname(__file__), 'pages_extra.json')
if os.path.exists(_extra):
    for e in json.load(open(_extra, encoding='utf-8')):
        render(e['id'], e['file'], e['title'], e['desc'], e['active'])

# sitemap.xml dan robots.txt ikut dirakit di sini, bukan ditulis tangan, supaya halaman
# baru (misalnya artikel dari gen_artikel.py) otomatis masuk. cek-link.yml membaca
# sitemap ini; halaman yang tidak terdaftar tidak ikut diperiksa.
SITE = 'https://arasinusa.co.id'
_files = [f for f, _, _ in PAGES.values()]
if os.path.exists(_extra):
    _files += [e['file'] for e in json.load(open(_extra, encoding='utf-8'))]
_urls = ''.join(f'  <url><loc>{SITE}/{"" if f == "index.html" else f}</loc></url>\n'
                for f in _files if os.path.exists(os.path.join(OUT, f)))
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + _urls + '</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8', newline='\n').write(
    f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
print('built sitemap.xml', len(_files), 'halaman')
