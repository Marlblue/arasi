import os, html
OUT = os.path.join(os.path.dirname(__file__), 'pages', 'produk.html')

CATS = [
    ('listrik', 'Listrik &amp; kontrol'),
    ('pneumatik', 'Pneumatik &amp; hidrolik'),
    ('transmisi', 'Transmisi &amp; handling'),
    ('pelumas', 'Pelumas &amp; utilitas'),
    ('perkakas', 'Perkakas &amp; alat ukur'),
    ('custom', 'Custom part'),
]
# (slug, brand, item, cat)
ITEMS = [
    ('schneider', 'Schneider Electric', 'MCCB / circuit breaker', 'listrik'),
    ('mitsubishi', 'Mitsubishi Electric', 'Circuit protector', 'listrik'),
    ('omron', 'Omron', 'Safety light curtain', 'listrik'),
    ('autonics', 'Autonics', 'Sensor tekanan', 'listrik'),
    ('idec', 'IDEC', 'Push button HA-C10', 'listrik'),
    ('hanyoung', 'Hanyoung Nux', 'Push button &amp; selector switch', 'listrik'),
    ('fuji-electric', 'Fuji Electric', 'Pilot lamp', 'listrik'),
    ('haiwell', 'Haiwell', 'HMI touch panel', 'listrik'),
    ('moflon', 'Moflon', 'Slip ring', 'listrik'),
    ('festo', 'Festo', 'Silinder pneumatik kompak', 'pneumatik'),
    ('smc', 'SMC', 'Guided cylinder', 'pneumatik'),
    ('bosch-rexroth', 'Bosch Rexroth', 'Vane pump hidrolik', 'pneumatik'),
    ('omega-air', 'Omega Air', 'Condensate drain', 'pneumatik'),
    ('nissei-gtr', 'Nissei GTR', 'Gear reducer', 'transmisi'),
    ('megadyne', 'Megadyne', 'Timing belt', 'transmisi'),
    ('forbo-siegling', 'Forbo Siegling', 'Flat belt conveyor', 'transmisi'),
    ('black-bear', 'Black Bear', 'Electric chain hoist', 'transmisi'),
    ('mobil-dte', 'Mobil', 'DTE 10 Excel 68 (oli hidrolik)', 'pelumas'),
    ('shell-gadus', 'Shell', 'Gadus (grease)', 'pelumas'),
    ('hencolin', 'Hencolin', 'Filter V-bank', 'pelumas'),
    ('oil-skimmer', 'Oil skimmer', 'Oil skimmer untuk mesin CNC', 'pelumas'),
    ('makita', 'Makita', 'Cordless blower 18V', 'perkakas'),
    ('elora', 'Elora', 'Ring slogging spanner', 'perkakas'),
    ('ophir', 'Ophir', 'Sensor daya laser', 'perkakas'),
    ('baut-titanium', 'Custom', 'Baut titanium Ti M14', 'custom'),
]
CATNAME = dict(CATS)

GROUPS = [
    ('Standard parts', 'Komponen listrik dan kontrol: circuit breaker, kontaktor, relay, push button, sensor, dan HMI.', 'barang/schneider.jpg', 'Pengadaan Produk / Suku Cadang'),
    ('Pneumatik, hidrolik &amp; pompa', 'Silinder, valve, pompa hidrolik, filter udara, dan komponen perpipaan.', 'barang/bosch-rexroth.jpg', 'Pengadaan Produk / Suku Cadang'),
    ('Transmisi &amp; material handling', 'Gear reducer, timing belt, belt conveyor, dan hoist untuk lini produksi.', 'barang/nissei-gtr.jpg', 'Pengadaan Produk / Suku Cadang'),
    ('Pelumas &amp; utilitas mesin', 'Oli hidrolik, grease, filter udara, dan oil skimmer untuk perawatan mesin.', 'barang/mobil-dte.jpg', 'Pengadaan Produk / Suku Cadang'),
    ('Perkakas &amp; alat ukur', 'Hand tools, cordless power tools, dan instrumen ukur untuk workshop dan QC.', 'barang/makita.jpg', 'Pengadaan Produk / Suku Cadang'),
    ('Custom parts', 'Part custom presisi, dies, punch tooling, dan komponen mekanikal sesuai gambar Anda.', 'barang/baut-titanium.jpg', 'Machining &amp; Fabrikasi Custom'),
]

g_html = '\n'.join(f'''      <article class="card flex flex-col">
        <div class="media contain ratio-4-3 border-b border-[#E6EAF0]"><img src="assets/img/{img}" alt="" loading="lazy"></div>
        <div class="card-pad flex-1 flex flex-col">
          <h3 class="h-card">{t}</h3>
          <p class="body-sm mt-2 flex-1">{d}</p>
          <a class="btn btn-outline btn-sm mt-5 self-start" href="#kontak" data-quote="{t}" data-kategori="{k}">Minta penawaran</a>
        </div>
      </article>''' for t, d, img, k in GROUPS)

from collections import Counter
_n = Counter(c for _, _, _, c in ITEMS)
chips = (f'<button type="button" class="chip" data-filter="all" aria-pressed="true">Semua <span class="chip-n">{len(ITEMS)}</span></button>' +
         ''.join(f'<button type="button" class="chip" data-filter="{k}" aria-pressed="false">{v} <span class="chip-n">{_n[k]}</span></button>' for k, v in CATS))

items = '\n'.join(f'''      <li data-cat="{cat}" class="card flex flex-col">
        <div class="media contain ratio-1"><img src="assets/img/barang/{slug}.jpg" alt="{html.escape(html.unescape(brand + ' ' + item))}" loading="lazy"></div>
        <div class="px-4 pb-4 pt-3 border-t border-[#E6EAF0] flex-1 flex flex-col">
          <span class="font-bold text-[#001F4B]">{brand}</span>
          <span class="body-sm flex-1">{item}</span>
          <span class="sr-only">{CATNAME[cat]}</span>
          <a class="link-arrow group !no-underline !text-sm mt-3" href="#kontak" data-quote="{brand} {item}" data-kategori="Pengadaan Produk / Suku Cadang"><span class="underline decoration-transparent underline-offset-4 transition-colors group-hover:decoration-current">Tanya harga</span><span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
        </div>
      </li>''' for slug, brand, item, cat in ITEMS)

doc = f'''<section class="page-hero">
  <div class="wrap">
    <h1 class="h-display">Produk industri</h1>
    <p class="lede">Komponen, suku cadang, alat ukur, dan perlengkapan untuk kebutuhan produksi dan perawatan pabrik. Belum ada di daftar? Kirim nomor part atau spesifikasinya, kami bantu carikan.</p>
  </div>
</section>

<section class="py-12 border-b border-[#E6EAF0]" aria-labelledby="brandsupport-judul">
  <div class="wrap">
    <h2 id="brandsupport-judul" class="text-center text-sm font-bold text-[#001F4B]">Brand yang kami dukung</h2>
    <p class="body-sm text-center mt-1 mb-6">Pengadaan produk dan suku cadang dari brand berikut.</p>
    <div class="marquee">
      <div class="marquee-track"><div class="marquee-item"><img src="assets/img/brands/mitsubishi-electric.png" alt="Mitsubishi Electric"></div><div class="marquee-item"><img src="assets/img/brands/shell.png" alt="Shell"></div><div class="marquee-item"><img src="assets/img/brands/rexroth.png" alt="Bosch Rexroth"></div><div class="marquee-item"><img src="assets/img/brands/misumi.png" alt="MISUMI"></div><div class="marquee-item"><img src="assets/img/brands/schneider-electric.png" alt="Schneider Electric"></div><div class="marquee-item"><img src="assets/img/brands/fanuc.png" alt="FANUC"></div><div class="marquee-item"><img src="assets/img/brands/jembo.png" alt="Jembo"></div><div class="marquee-item"><img src="assets/img/brands/bosch.png" alt="Bosch"></div><div class="marquee-item"><img src="assets/img/brands/abb.png" alt="ABB"></div><div class="marquee-item"><img src="assets/img/brands/makita.png" alt="Makita"></div><div class="marquee-item"><img src="assets/img/brands/smc.png" alt="SMC"></div><div class="marquee-item"><img src="assets/img/brands/rotex.png" alt="Rotex"></div><div class="marquee-item"><img src="assets/img/brands/nafco.png" alt="Nafco"></div><div class="marquee-item"><img src="assets/img/brands/festo.png" alt="Festo"></div><div class="marquee-item"><img src="assets/img/brands/shigatsu.png" alt="Shigatsu"></div><div class="marquee-item"><img src="assets/img/brands/suiden.png" alt="Suiden"></div><div class="marquee-item"><img src="assets/img/brands/trusco.png" alt="Trusco"></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/mitsubishi-electric.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/shell.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/rexroth.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/misumi.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/schneider-electric.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/fanuc.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/jembo.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/bosch.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/abb.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/makita.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/smc.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/rotex.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/nafco.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/festo.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/shigatsu.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/suiden.png" alt=""></div><div class="marquee-item" aria-hidden="true"><img src="assets/img/brands/trusco.png" alt=""></div></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="brand-judul">
  <div class="wrap">
    <div class="section-head-row !mb-8">
      <div class="section-head">
        <h2 id="brand-judul" class="h-section">Contoh barang yang pernah kami suplai</h2>
        <p class="lede">Brand dan tipe bisa disesuaikan dengan standar pabrik Anda.</p>
      </div>
      <div class="catalog-search w-full lg:w-80">
        <span class="material-symbols-outlined" aria-hidden="true">search</span>
        <label for="cari-produk" class="sr-only">Cari brand atau barang</label>
        <input id="cari-produk" type="search" placeholder="Cari brand atau barang" data-filter-search="katalog" autocomplete="off">
      </div>
    </div>
    <div class="catalog-bar">
      <div class="catalog-chips" data-filter-group="katalog" role="group" aria-label="Saring kategori">{chips}</div>
    </div>
    <p class="body-sm mt-4 mb-6" aria-live="polite"><span class="font-semibold text-[#0F172A]" data-filter-count="katalog">{len(ITEMS)}</span> barang ditampilkan</p>
    <ul id="katalog" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
{items}
    </ul>
    <div data-filter-empty hidden class="card card-pad text-center mt-4">
      <p class="font-bold text-[#001F4B]">Tidak ada barang yang cocok.</p>
      <p class="body-sm mt-1">Coba kata lain, atau <a class="underline font-semibold text-[#001F4B]" href="#kontak">kirim nomor part-nya ke kami</a>.</p>
    </div>
  </div>
</section>
'''
open(OUT, 'w', encoding='utf-8').write(doc)
print('ok', len(ITEMS))
