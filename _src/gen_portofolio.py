import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slider import slider
OUT = os.path.join(os.path.dirname(__file__), 'pages', 'portofolio.html')

CATS = [('all', 'Semua'), ('jig', 'Jig &amp; Fixture'), ('fabrikasi', 'Fabrikasi'), ('otomasi', 'Otomasi'), ('modifikasi', 'Modifikasi Fasilitas')]
CN = dict(CATS)
# id, cat, title, client, context, body, route, img, cad
P = [
 ('jig-punch-press', 'jig', 'Jig part ke mesin punch press', 'PT Sugity Creatives', 'Otomotif · stamping',
  'Base plate jig dengan fixture connector, insert bushing berflens, dan handle angkat untuk memosisikan part secara konsisten saat proses punching.',
  ['Gambar &amp; sampel part', 'Desain 3D', 'Machining', 'Inspeksi dimensi', 'Trial di mesin'], 'projects/jig-punch-press.jpg', True),
 ('jig-cover-drl', 'jig', 'Jig Assy Cover DRL', 'PT Sugity Creatives', 'Otomotif · perakitan lampu',
  'Tiga varian dudukan perakitan cover DRL, dirancang agar permukaan part tidak tergores dan posisinya konsisten di setiap siklus.',
  ['Gambar &amp; sampel', 'Desain 3D', 'Machining', 'Inspeksi dimensi', 'Trial di lini'], 'real/jig-drl-1-mfg.jpg', False),
 ('base-robot-fanuc', 'fabrikasi', 'Base &amp; jig robot Fanuc', 'PT Sugity Creatives', 'Otomotif · stasiun robot',
  'Meja dudukan robot Fanuc dan meja controller berangka baja, dengan roda dan leveling foot agar stasiun robot mudah dipindah dan diposisikan ulang.',
  ['Data robot &amp; area', 'Desain 3D rangka', 'Fabrikasi las', 'Finishing', 'Instalasi'], 'projects/base-robot-fanuc.jpg', True),
 ('cover-grille-bumper', 'fabrikasi', 'Cover grille bumper Fortuner', 'PT Sugity Creatives', 'Otomotif · custom part',
  'Komponen cover grille bumper untuk lini Toyota Fortuner, dibuat mengikuti gambar kerja dan dimensi part dari customer.',
  ['Gambar kerja', 'Desain 3D', 'Fabrikasi', 'Inspeksi dimensi', 'Serah terima'], 'projects/cover-grille-bumper.jpg', True),
 ('folding-pallet', 'fabrikasi', 'Folding pallet', 'PT Sugity Creatives', 'Logistik · material handling',
  'Palet baja lipat untuk penumpukan komponen dan penghematan ruang saat kosong, dengan engsel yang dirancang untuk pemakaian berulang.',
  ['Kebutuhan beban', 'Desain struktur', 'Fabrikasi las', 'Finishing', 'Serah terima'], 'real/folding-pallet.jpg', False),
 ('trolley-door-plate', 'fabrikasi', 'Trolley door plate', 'PT Shin Heung Indonesia', 'Material handling',
  'Troli pemindah pelat pintu antarstasiun, dengan rangka dan dudukan yang menjaga permukaan benda kerja tetap aman.',
  ['Survei part', 'Desain 3D', 'Fabrikasi', 'Finishing', 'Serah terima'], 'real/trolley-door-plate.jpg', False),
 ('trolley-pipe-ac', 'fabrikasi', 'Trolley pipe AC', 'LG Electronics Indonesia', 'Material handling',
  'Troli stainless untuk penyimpanan dan pemindahan pipa AC di area produksi.',
  ['Survei part', 'Desain', 'Fabrikasi stainless', 'Finishing', 'Serah terima'], 'real/trolley-pipe-ac.jpg', False),
 ('tools-cabinet', 'fabrikasi', 'Tools cabinet', 'PT KAO Indonesia', 'Shop floor',
  'Kabinet dan meja stainless untuk penyimpanan perkakas di area produksi.',
  ['Survei area', 'Desain', 'Fabrikasi stainless', 'Finishing', 'Instalasi'], 'real/tools-cabinet.jpg', False),
 ('dryer-tools-cabinet', 'fabrikasi', 'Dryer tools cabinet', 'PT KAO Indonesia', 'Shop floor · higienis',
  'Kabinet pengering perkakas berbahan stainless, dari desain rak bagian dalam sampai unit terpasang.',
  ['Kebutuhan proses', 'Desain 3D', 'Fabrikasi stainless', 'Finishing', 'Instalasi'], 'real/dryer-cabinet.jpg', False),
 ('halal-certify-tools', 'fabrikasi', 'Halal certify tools', 'PT KAO Indonesia', 'Fasilitas produksi',
  'Pembuatan dan pemasangan perlengkapan stainless pendukung proses sertifikasi halal di area produksi.',
  ['Survei lapangan', 'Desain', 'Fabrikasi stainless', 'Instalasi', 'Serah terima'], 'real/kao-halal-6.jpg', False),
 ('air-assist', 'otomasi', 'Air assist injection machine', 'PT Sugity Creatives', 'Special purpose machine',
  'Unit air assist untuk mesin injeksi, dirakit lengkap dengan regulator, tabung udara, dan panel kontrol.',
  ['Studi proses', 'Desain', 'Perakitan', 'Wiring', 'Commissioning'], 'real/spm-air-assist.jpg', False),
 ('temperature-control', 'otomasi', 'Temperature control panel', 'PT Sugity Creatives', 'Special purpose machine',
  'Panel kontrol temperatur untuk proses produksi, dari perakitan komponen sampai uji fungsi.',
  ['Studi proses', 'Desain panel', 'Perakitan', 'Wiring', 'Uji fungsi'], 'real/spm-temp-control.jpg', False),
 ('pick-to-light', 'otomasi', 'Pick To Light System', 'PT Sugity Creatives', 'Perakitan · poka-yoke',
  'Lampu indikator di setiap rak memandu operator mengambil komponen yang benar, terhubung ke panel HMI dan kontrol lini.',
  ['Audit rak', 'Desain modul', 'Wiring &amp; PLC', 'Uji urutan', 'Pelatihan operator'], 'slider:pick-to-light', False),
 ('agv', 'otomasi', 'AGV System', '', 'Intralogistik',
  'Kendaraan berpemandu otomatis yang menarik troli komponen antar-stasiun, mendukung keselamatan kerja dan kelancaran alur produksi.',
  ['Pemetaan rute', 'Desain troli', 'Instalasi', 'Integrasi stasiun', 'Uji jalan'], 'slider:agv', False),
 ('robot-painting', 'otomasi', 'Robot Painting Integrated System', '', 'Coating',
  'Integrasi robot pengecatan di stasiun kerja untuk hasil lapisan yang konsisten, proses lebih efisien, dan produksi yang stabil.',
  ['Studi proses', 'Desain base &amp; layout', 'Integrasi robot &amp; PLC', 'Teaching', 'Commissioning'], 'slider:robot-painting', False),
 ('bypass-conveyor', 'modifikasi', 'Bypass conveyor', 'PT Nippon Indosari Corpindo (Sari Roti)', 'Food processing',
  'Jalur conveyor bypass untuk lini roti lapis dan dorayaki, menghubungkan slicer ke mesin packing dengan belt food grade dan rangka stainless.',
  ['Survei layout', 'Desain jalur', 'Fabrikasi rangka', 'Instalasi &amp; motor', 'Uji aliran'], 'projects/bypass-conveyor.jpg', False),
 ('tangga-operator', 'modifikasi', 'Modifikasi tangga operator', 'PT KAO Indonesia', 'K3 · ergonomi',
  'Perpanjangan platform tangga operator lengkap dengan handrail dan pijakan anti-slip, disesuaikan dengan ketinggian area kerja yang baru.',
  ['Ukur area', 'Desain K3', 'Fabrikasi', 'Instalasi', 'Serah terima'], 'projects/tangga-operator-kao.jpg', True),
 ('asphalt-repair', 'modifikasi', 'Perbaikan jalan aspal pabrik', 'TACI', 'Fasilitas pabrik',
  'Perbaikan permukaan jalan aspal di area pabrik, dikerjakan bertahap dengan pengamanan area kerja.',
  ['Survei kerusakan', 'Rencana kerja', 'Pembongkaran', 'Pengaspalan', 'Serah terima'], 'real/taci-2.jpg', False),
]

rows = []
for pid, cat, title, client, ctx, body, route, img, cad in P:
    cl = f'<p class="client mt-1">{client}</p>' if client else ''
    lis = ''.join(f'<li>{r}</li>' for r in route)
    alt = html.escape(html.unescape(title))
    rows.append(f'''<article id="{pid}" class="row" data-cat="{cat}">
  <div class="row-text">
    <p class="meta">{CN[cat]} · {ctx}</p>
    <h3 class="h-card !text-[1.375rem] mt-1">{title}</h3>
    {cl}
    <p class="body mt-3">{body}</p>
  </div>
  <ol class="route" aria-label="Tahapan pengerjaan">{lis}</ol>
  {slider(img[7:], 'ratio-4-3 rounded-lg') if img.startswith('slider:') else f'<div class="media ratio-4-3 rounded-lg{chr(32) + "contain border border-[#E6EAF0]" if cad else ""}"><img src="assets/img/{img}" alt="{alt}" loading="lazy"></div>'}
</article>''')

from collections import Counter
_n = Counter(x[1] for x in P)
chips = ''.join(f'<button type="button" class="chip" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v} <span class="chip-n">{len(P) if k == "all" else _n[k]}</span></button>' for k, v in CATS)

STEPS = [
    ('Kebutuhan produksi', 'Mempelajari kondisi lini, target cycle time, masalah defect, dan toleransi yang diminta.'),
    ('Lingkup pekerjaan', 'Konsep desain 3D, pemilihan material, dan estimasi waktu pengerjaan.'),
    ('Dokumentasi', 'Gambar kerja, laporan inspeksi dimensi, wiring diagram, dan panduan operasional.'),
    ('Fungsi alat / sistem', 'Uji fungsi di workshop, lalu instalasi dan trial di pabrik klien sampai berjalan stabil.'),
]
steps = ''.join(f'<li class="border-t-[3px] border-[#001F4B] pt-5"><span class="block text-sm font-bold text-[#CC0000]">Tahap {i}</span><h3 class="h-card mt-1">{t}</h3><p class="body-sm mt-2">{d}</p></li>' for i, (t, d) in enumerate(STEPS, 1))

doc = f'''<style>
  .rows {{ border-top: 2px solid #001F4B; }}
  .row {{ display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr) 260px; gap: 2rem; padding: 2rem 0; border-bottom: 1px solid #D5DCE5; align-items: start; }}
  .route {{ list-style: none; margin: 0; padding: 0; position: relative; font-size: .9375rem; color: #3F4654; counter-reset: step; }}
  .route::before {{ content: ""; position: absolute; left: 5px; top: 12px; bottom: 12px; width: 2px; background: #D5DCE5; }}
  .route li {{ position: relative; padding: 4px 0 4px 26px; }}
  .route li::before {{ content: ""; position: absolute; left: 0; top: 10px; width: 12px; height: 12px; border-radius: 999px; background: #001F4B; box-shadow: 0 0 0 3px #fff; }}
  .route li:last-child::before {{ background: #CC0000; }}
  @media (max-width: 1023px) {{ .row {{ grid-template-columns: minmax(0, 1fr) 220px; }} .route {{ grid-column: 1; }} .row .media {{ grid-column: 2; grid-row: 1 / span 2; }} }}
  @media (max-width: 639px) {{ .row {{ grid-template-columns: 1fr; gap: 1.25rem; }} .row .media {{ grid-column: 1; grid-row: 1; }} }}
</style>
<section class="page-hero">
  <div class="wrap">
    <h1 class="h-display">Portofolio proyek</h1>
    <p class="lede">Jig dan fixture, fabrikasi peralatan, integrasi otomasi, serta modifikasi fasilitas yang sudah kami kerjakan untuk pabrik klien.</p>
  </div>
</section>

<section class="section" aria-labelledby="daftar-judul">
  <div class="wrap">
    <h2 id="daftar-judul" class="sr-only">Daftar proyek</h2>
    <div class="catalog-chips mb-4" data-filter-group="daftar-proyek" role="group" aria-label="Saring proyek">{chips}</div>
    <p class="body-sm mb-6" aria-live="polite"><span data-filter-count="daftar-proyek">{len(P)}</span> proyek ditampilkan</p>
    <div id="daftar-proyek" class="rows">
{chr(10).join(rows)}
    </div>
  </div>
</section>

<section class="section bg-paper-2" aria-labelledby="alur-judul">
  <div class="wrap">
    <div class="section-head">
      <h2 id="alur-judul" class="h-section">Alur pengerjaan</h2>
      <p class="lede">Setiap proyek melewati empat tahap yang sama, dari kebutuhan di lini sampai alat berjalan di pabrik Anda.</p>
    </div>
    <ol class="grid sm:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-10">{steps}</ol>
    <a class="btn btn-primary mt-12" href="#kontak">Diskusikan proyek serupa</a>
  </div>
</section>
'''
open(OUT, 'w', encoding='utf-8').write(doc)
print('ok', len(P))
