"""Halaman detail artikel: menulis pages/artikel-<slug>.html + pages_extra.json (dibaca build.py)."""
import os, json, re, html

HERE = os.path.dirname(__file__)
PAGES = os.path.join(HERE, 'pages')

# slug, judul, kategori, gambar, gambar_contain, ringkasan, isi(HTML)
A = [
('poka-yoke-stamping', 'Menekan defect stamping dengan desain nested poka-yoke dan clamping pneumatik', 'Jig & fixture',
 'projects/jig-punch-press.jpg', True,
 'Bagaimana bentuk nest, titik referensi, dan clamping pneumatik pada jig membuat lembaran logam selalu duduk di posisi yang sama saat punching.',
 '''
<p>Di lini stamping, sebagian besar defect bukan berasal dari dies, melainkan dari posisi part yang bergeser sebelum mesin turun. Lembaran yang miring satu atau dua milimeter cukup untuk membuat lubang meleset, burr berlebih, atau part harus di-rework. Jig yang dirancang dengan benar menghilangkan variabel itu dari tangan operator.</p>

<h2>Mulai dari titik referensi part</h2>
<p>Desain jig selalu berangkat dari gambar part dan datum yang dipakai saat inspeksi. Titik referensi pada jig harus sama dengan datum pada gambar, sehingga ketika part lolos di jig, ia juga lolos di alat ukur. Prinsip 3-2-1 dipakai untuk mengunci enam derajat kebebasan:</p>
<ul>
  <li><strong>Tiga titik</strong> pada bidang utama menentukan dudukan dasar.</li>
  <li><strong>Dua titik</strong> pada sisi panjang mengunci arah dan rotasi.</li>
  <li><strong>Satu titik</strong> pada sisi pendek mengunci posisi memanjang.</li>
</ul>
<p>Pin locator dibuat pas dengan lubang referensi part. Satu pin bulat dan satu pin diamond biasanya cukup untuk menghindari part terkunci atau macet karena toleransi lubang.</p>

<h2>Nest yang hanya menerima orientasi benar</h2>
<p>Poka-yoke pada jig berarti part secara fisik tidak bisa dipasang terbalik atau tertukar. Caranya bisa sederhana: profil nest mengikuti kontur part yang asimetris, ditambah pin penolak di posisi yang hanya cocok untuk orientasi yang benar. Operator tidak perlu mengingat urutan; kalau part masuk, berarti posisinya sudah benar.</p>

<h2>Clamping yang menahan, bukan menekan berlebih</h2>
<p>Toggle clamp manual sudah cukup untuk banyak kasus, tetapi pada siklus cepat clamping pneumatik memberi gaya yang konsisten di setiap pukulan. Dua silinder yang bergerak bersamaan menahan part dari dua sisi tanpa membuatnya melengkung. Yang perlu diperhatikan:</p>
<ul>
  <li>Ujung clamp berbahan lunak (urethane atau POM) agar permukaan part tidak tergores.</li>
  <li>Sensor posisi silinder dihubungkan ke interlock mesin, sehingga press tidak bisa turun sebelum clamp benar-benar menutup.</li>
  <li>Regulator tekanan terpisah untuk clamping, supaya gaya jepit tidak ikut berubah ketika tekanan pabrik turun.</li>
</ul>

<h2>Material dan perlakuan panas</h2>
<p>Bagian yang bersentuhan langsung dengan lembaran, seperti locator dan pelat nest, dibuat dari baja perkakas seperti SKD11 yang dikeraskan agar tidak cepat aus. Base plate cukup dari S50C atau baja karbon sedang. Komponen yang sering diganti dibuat modular dan dipasang dengan dowel pin, sehingga penggantian tidak mengubah posisi.</p>

<h2>Uji sebelum dipakai di lini</h2>
<p>Jig diverifikasi dimensinya di workshop, lalu dicoba langsung di mesin dengan part produksi. Beberapa puluh siklus percobaan biasanya cukup untuk melihat apakah ada pergeseran, keausan awal, atau langkah operator yang masih membingungkan. Penyesuaian kecil di tahap ini jauh lebih murah daripada setelah jig dipakai penuh.</p>

<p>Hasil akhirnya bukan hanya defect yang turun. Operator baru lebih cepat terlatih, waktu setting berkurang, dan data kualitas menjadi lebih stabil karena satu sumber variasi sudah hilang.</p>
'''),

('interlock-robot', 'PLC dan safety interlock pada stasiun kerja robot Fanuc', 'Otomasi',
 'real/robot-painting-cad.jpg', False,
 'Menyatukan robot controller, PLC, light curtain, dan pintu pengaman agar robot berhenti otomatis setiap kali area kerjanya dimasuki.',
 '''
<p>Robot industri bekerja cepat dan bertenaga besar. Selama operator tidak pernah masuk ke area geraknya, risikonya kecil. Masalah muncul saat operator perlu memasang part, membersihkan nozzle, atau mengambil hasil kerja. Safety interlock memastikan robot selalu berada dalam keadaan aman ketika itu terjadi.</p>

<h2>Peran masing-masing perangkat</h2>
<ul>
  <li><strong>Robot controller</strong> menjalankan program gerak dan menerima sinyal berhenti dari luar.</li>
  <li><strong>PLC</strong> mengatur urutan stasiun: kapan part siap, kapan robot boleh mulai, dan kapan operator boleh masuk.</li>
  <li><strong>Perangkat pengaman</strong> seperti light curtain, safety mat, dan sakelar pintu mendeteksi kehadiran orang.</li>
  <li><strong>Safety relay atau safety PLC</strong> memutus jalur berhenti darurat secara langsung, tidak bergantung pada logika program biasa.</li>
</ul>

<h2>Pisahkan sinyal kontrol dan sinyal keselamatan</h2>
<p>Kesalahan yang sering terjadi adalah memasukkan sinyal light curtain hanya sebagai input biasa ke PLC. Jika program bermasalah, robot bisa tetap bergerak. Sinyal keselamatan sebaiknya dua kanal dan masuk ke safety relay atau input safety pada robot controller, sementara PLC hanya membaca statusnya untuk keperluan urutan dan tampilan alarm.</p>

<h2>Urutan kerja yang aman</h2>
<ol>
  <li>Operator memasang part di jig, lalu keluar dari area dan menekan tombol dua tangan atau tombol start di luar pagar.</li>
  <li>PLC memeriksa: jig sudah clamp, light curtain bersih, pintu tertutup. Baru setelah itu robot diberi izin mulai.</li>
  <li>Jika light curtain terpotong saat robot bergerak, robot berhenti dengan kategori stop yang sesuai, dan tidak boleh langsung jalan lagi hanya karena area kembali bersih.</li>
  <li>Reset dilakukan dengan sengaja oleh operator dari posisi yang bisa melihat seluruh area.</li>
</ol>

<h2>Mode perawatan</h2>
<p>Teknisi kadang harus masuk saat robot dalam mode teach. Di mode ini kecepatan robot dibatasi, enabling switch pada teach pendant harus ditekan, dan pintu pengaman boleh terbuka. Pemilihan mode sebaiknya memakai kunci, agar tidak ada yang mengubahnya tanpa sengaja.</p>

<h2>Base dan tata letak ikut menentukan</h2>
<p>Base robot yang kaku dan terkunci ke lantai menjaga titik kerja tetap akurat. Jarak light curtain dari zona bahaya dihitung dari waktu berhenti robot, sehingga robot sudah diam sebelum tangan operator mencapai area gerak. Karena itu desain mekanik dan desain kontrol perlu dikerjakan bersamaan.</p>

<p>Stasiun robot yang interlock-nya rapi bukan hanya lebih aman. Downtime karena alarm palsu juga berkurang, dan operator lebih percaya diri bekerja di sekitarnya.</p>
'''),

('perawatan-pneumatik', 'Perawatan silinder pneumatik dan solenoid valve di area berdebu logam', 'Perawatan',
 'barang/smc.jpg', True,
 'Langkah sederhana untuk memperpanjang usia silinder dan valve di area machining dan grinding yang penuh debu serta geram logam.',
 '''
<p>Silinder pneumatik termasuk komponen yang paling banyak dipakai di mesin produksi, dan juga salah satu yang paling sering diganti. Di area machining, grinding, atau welding, penyebab utamanya hampir selalu sama: kotoran masuk ke seal dan udara yang tidak bersih.</p>

<h2>Udara bersih adalah perawatan pertama</h2>
<p>Unit FRL (filter, regulator, lubricator) di setiap mesin adalah garis pertahanan pertama. Yang perlu dicek rutin:</p>
<ul>
  <li>Mangkuk filter dikuras sebelum air mencapai batas. Auto drain sangat membantu di jalur yang lembap.</li>
  <li>Elemen filter diganti saat mulai tersumbat, ditandai dengan tekanan turun ketika silinder bergerak.</li>
  <li>Regulator di-set sesuai kebutuhan, tidak dibiarkan pada tekanan maksimum. Tekanan berlebih mempercepat keausan seal dan membuat gerakan menghentak.</li>
</ul>

<h2>Lindungi batang piston</h2>
<p>Debu logam yang menempel di batang piston akan terbawa masuk saat silinder menarik, lalu merusak seal dan dinding tabung. Untuk area yang kotor:</p>
<ul>
  <li>Gunakan silinder dengan scraper ring yang lebih kuat, atau tambahkan bellows/cover pada batang.</li>
  <li>Arahkan pemasangan agar batang tidak menghadap langsung ke sumber geram.</li>
  <li>Lap batang piston saat jadwal perawatan, jangan disemprot udara karena justru mendorong kotoran ke seal.</li>
</ul>

<h2>Pelumasan secukupnya</h2>
<p>Banyak silinder modern sudah dilumasi dari pabrik dan dirancang tanpa pelumasan tambahan. Jika lubricator sudah terlanjur dipakai, pelumasan harus diteruskan, karena oli tambahan akan membersihkan grease bawaan. Pakai oli yang sesuai rekomendasi pabrikan dan atur tetesannya seminimal mungkin.</p>

<h2>Solenoid valve dan sensor</h2>
<p>Valve yang sering macet biasanya terkena air atau partikel dari jalur udara. Silencer pada port buang juga perlu diganti saat tersumbat, karena membuat gerakan silinder melambat. Untuk sensor posisi, pilih tipe yang tahan percikan dan getaran, dan kencangkan bracket-nya, karena sensor yang bergeser sering dikira valve rusak.</p>

<h2>Jadwal sederhana yang bisa langsung dipakai</h2>
<ol>
  <li><strong>Harian:</strong> cek drain filter, dengarkan kebocoran udara, perhatikan gerakan yang tersendat.</li>
  <li><strong>Mingguan:</strong> bersihkan batang piston dan sensor, cek baut bracket.</li>
  <li><strong>Bulanan:</strong> cek tekanan regulator, kondisi selang dan fitting, serta silencer.</li>
  <li><strong>Saat ganti:</strong> catat nomor part dan penyebab kerusakan untuk melihat pola.</li>
</ol>

<p>Dengan perawatan dasar ini, silinder yang biasanya diganti beberapa bulan sekali bisa bertahan jauh lebih lama. Untuk penggantian, kami bisa membantu pengadaan unit dan seal kit dari brand yang sama dengan yang sudah terpasang di mesin.</p>
'''),

('verifikasi-dimensi', 'Verifikasi dimensi sebelum serah terima', 'Quality control',
 'projects/cover-grille-bumper.jpg', True,
 'Apa saja yang diperiksa sebelum part machining dan jig dikirim ke pabrik klien, dan kenapa laporan inspeksi ikut diserahkan.',
 '''
<p>Part yang terlihat rapi belum tentu sesuai gambar. Satu ukuran kritis yang meleset baru ketahuan saat dirakit di pabrik klien, dan pada saat itu biayanya sudah berlipat. Karena itu setiap part dan jig diperiksa terhadap gambar kerja sebelum dikirim.</p>

<h2>Tentukan dulu ukuran kritis</h2>
<p>Tidak semua dimensi sama pentingnya. Dari gambar kerja, kami menandai ukuran yang menentukan fungsi: posisi lubang referensi, jarak antar-pin locator, kerataan bidang dudukan, dan diameter yang berpasangan dengan bearing atau bushing. Ukuran-ukuran ini diperiksa satu per satu, bukan diambil sampel.</p>

<h2>Membaca toleransi geometrik</h2>
<p>Selain toleransi ukuran, gambar teknik biasanya mencantumkan toleransi geometrik (GD&amp;T):</p>
<ul>
  <li><strong>Kerataan dan ketegaklurusan</strong> untuk bidang dudukan jig.</li>
  <li><strong>Posisi</strong> untuk pola lubang dan pin yang harus sejajar dengan datum.</li>
  <li><strong>Kesejajaran dan konsentrisitas</strong> untuk poros dan rumah bearing.</li>
</ul>
<p>Pengukurannya selalu dimulai dari datum yang sama dengan yang tertulis di gambar. Mengukur dari sisi lain bisa memberi angka yang terlihat lolos padahal part tidak berfungsi.</p>

<h2>Alat ukur yang dipakai</h2>
<ul>
  <li>Caliper dan mikrometer untuk ukuran luar dan dalam.</li>
  <li>Height gauge dan dial indicator di atas surface plate untuk kerataan dan ketinggian.</li>
  <li>Pin gauge dan thread gauge untuk lubang dan ulir.</li>
  <li>Surface roughness tester untuk permukaan yang bergesekan atau menjadi dudukan seal.</li>
</ul>
<p>Alat ukur harus dikalibrasi berkala, dan pengukuran dilakukan setelah part mencapai suhu ruang, karena baja yang baru selesai dimesin masih memuai.</p>

<h2>Uji fungsi untuk jig</h2>
<p>Untuk jig dan fixture, ukuran yang benar saja belum cukup. Jig dicoba dengan part asli atau sampel: apakah part masuk dengan mudah, duduk rapat, terkunci dengan benar, dan bisa dilepas tanpa tersangkut. Clamp dan sensor diuji berulang kali untuk memastikan tidak ada yang longgar.</p>

<h2>Laporan inspeksi</h2>
<p>Hasil pengukuran dicatat dalam laporan yang mencantumkan nilai nominal, toleransi, hasil ukur, dan status. Laporan ini ikut diserahkan bersama barang, sehingga tim quality di pabrik klien tidak perlu mengukur ulang dari nol, dan bisa dipakai sebagai acuan saat part yang sama dipesan lagi.</p>
'''),

('agv-aliran-material', 'AGV untuk aliran material antar-stasiun', 'Otomasi',
 'real/agv.jpg', False,
 'Kapan AGV layak dipakai, apa yang perlu disiapkan di lantai produksi, dan bagaimana troli serta titik docking dirancang.',
 '''
<p>Mendorong troli komponen dari gudang ke lini terlihat sepele, tetapi jika dilakukan puluhan kali per shift, waktunya terasa. Operator meninggalkan stasiunnya, jadwal pasokan tidak konsisten, dan lorong menjadi padat. Automated guided vehicle (AGV) mengambil alih pekerjaan berulang ini.</p>

<h2>Kapan AGV masuk akal</h2>
<ul>
  <li>Rutenya tetap dan berulang, misalnya dari supermarket part ke beberapa stasiun perakitan.</li>
  <li>Beban dan bentuk troli bisa diseragamkan.</li>
  <li>Lantai cukup rata, dan lorongnya bisa dipisahkan dari jalur forklift.</li>
</ul>
<p>Jika rutenya sering berubah atau barangnya sangat beragam, sistem lain mungkin lebih cocok. Pemetaan rute di awal membantu menjawab pertanyaan ini sebelum investasi.</p>

<h2>Jalur dan navigasi</h2>
<p>AGV paling sederhana mengikuti pita magnetik di lantai, dengan penanda tambahan untuk berhenti, belok, atau mengubah kecepatan. Sistem ini mudah dipasang dan diubah. Untuk area yang lebih dinamis, navigasi berbasis QR code atau laser bisa dipakai. Yang penting, persimpangan dan titik berhenti dirancang agar AGV tidak saling menunggu.</p>

<h2>Troli dan docking</h2>
<p>Bagian yang sering dilupakan adalah troli itu sendiri. Troli harus punya titik kait yang seragam, roda yang cocok dengan beban, dan rangka yang menahan part tanpa bergeser saat AGV berbelok. Di setiap stasiun, titik docking memastikan troli berhenti di posisi yang sama, sehingga operator selalu mengambil part dari sisi yang benar.</p>

<h2>Keselamatan di lantai produksi</h2>
<ul>
  <li>Sensor anti-tabrak di depan AGV yang memperlambat lalu menghentikan unit saat ada halangan.</li>
  <li>Tombol berhenti darurat di kedua sisi.</li>
  <li>Lampu dan suara peringatan saat bergerak dan berbelok.</li>
  <li>Marka lantai yang jelas memisahkan jalur AGV dari jalur pejalan kaki.</li>
</ul>

<h2>Integrasi dengan stasiun</h2>
<p>AGV bisa dipanggil dengan tombol di stasiun atau dijadwalkan oleh sistem. Sinyal sederhana dari PLC stasiun, misalnya troli kosong sudah siap diambil, sudah cukup untuk membuat alur pasokan berjalan sendiri tanpa operator perlu menelepon gudang.</p>
'''),

('parameter-vmc', 'Kecepatan spindle dan pemilihan tooling di vertical machining center', 'Machining',
 'real/mc-ycm-vmc.jpg', True,
 'Hubungan antara kecepatan spindle, feed, coolant, dan kekakuan fixture terhadap ketelitian bentuk part aluminium.',
 '''
<p>Pada vertical machining center, hasil akhir part ditentukan oleh banyak faktor sekaligus: mesin, tool, parameter potong, coolant, dan cara part dijepit. Untuk aluminium seperti AL6061, kesalahan yang paling sering terlihat adalah permukaan bergelombang, ukuran berubah setelah part dilepas, dan geram menempel di mata potong.</p>

<h2>Kecepatan potong dan feed</h2>
<p>Aluminium memungkinkan kecepatan potong yang tinggi, tetapi feed per gigi tetap harus cukup agar tool memotong, bukan menggosok. Feed yang terlalu kecil membuat panas menumpuk dan geram menempel. Titik awal yang aman selalu mengacu pada rekomendasi pembuat tool, lalu disesuaikan dengan suara potong dan bentuk geram di mesin.</p>

<h2>Pemilihan tool</h2>
<ul>
  <li>End mill 2 atau 3 flute dengan sudut helix besar untuk ruang buang geram yang lega.</li>
  <li>Coating yang sesuai untuk aluminium, atau tool tanpa coating dengan permukaan flute yang dipoles.</li>
  <li>Panjang tool sependek mungkin. Setiap penambahan panjang menurunkan kekakuan dan menambah getaran.</li>
</ul>

<h2>Coolant dan buang geram</h2>
<p>Geram yang tidak segera terbuang akan terpotong ulang dan merusak permukaan. Aliran coolant diarahkan tepat ke titik potong, atau dibantu udara bertekanan untuk kantong yang dalam. Konsentrasi coolant juga perlu dijaga; terlalu encer memicu karat dan geram lengket.</p>

<h2>Kekakuan fixture</h2>
<p>Part yang dijepit terlalu keras bisa terlihat benar saat di mesin, lalu melengkung kembali setelah dilepas. Sebaliknya, jepitan yang lemah membuat part bergetar. Fixture yang baik menopang part di dekat area potong, menjepit di bagian yang kaku, dan memakai gaya jepit secukupnya. Untuk part tipis, proses roughing dan finishing dipisah, dengan jepitan dikendurkan sedikit sebelum finishing.</p>

<h2>Urutan proses</h2>
<ol>
  <li>Roughing dengan sisa material merata untuk finishing.</li>
  <li>Beri waktu atau lepas-pasang ringan agar tegangan dalam part keluar.</li>
  <li>Finishing dengan tool tajam dan kedalaman kecil.</li>
  <li>Ukur setelah part kembali ke suhu ruang.</li>
</ol>
<p>Dengan urutan ini, ukuran akhir lebih stabil dan pekerjaan ulang bisa ditekan, terutama untuk part jig dan plate yang menuntut kerataan.</p>
'''),

('pick-to-light', 'Pick to light untuk poka-yoke perakitan', 'Otomasi',
 'real/ptl-install.jpg', False,
 'Cara kerja pick to light, komponen yang dibutuhkan, dan hal yang perlu diperhatikan saat memasangnya di rak komponen yang sudah ada.',
 '''
<p>Di stasiun perakitan dengan banyak varian produk, operator harus memilih part yang benar dari puluhan box. Kesalahan ambil jarang terjadi, tetapi setiap kejadian berarti produk harus dibongkar atau lolos ke pelanggan. Pick to light memandu operator dengan lampu di setiap lokasi part.</p>

<h2>Cara kerjanya</h2>
<ol>
  <li>Operator memindai barcode produk atau kartu kerja.</li>
  <li>Sistem menyalakan lampu di lokasi part yang dibutuhkan, lengkap dengan jumlahnya.</li>
  <li>Operator mengambil part lalu menekan tombol konfirmasi di modul lampu, atau sensor mendeteksi tangan masuk ke box.</li>
  <li>Jika operator mengambil dari lokasi yang salah, sistem memberi peringatan sebelum langkah berikutnya bisa dilanjutkan.</li>
</ol>

<h2>Komponen sistem</h2>
<ul>
  <li><strong>Modul lampu</strong> di setiap lokasi rak, dengan tombol konfirmasi dan kadang tampilan angka.</li>
  <li><strong>Pemindai barcode</strong> untuk memilih produk atau urutan kerja.</li>
  <li><strong>Panel kontrol dan HMI</strong> untuk mengatur daftar part per produk dan menampilkan status.</li>
  <li><strong>Kabel dan bracket</strong> yang mengikuti bentuk rak.</li>
</ul>

<h2>Memasang di rak yang sudah ada</h2>
<p>Sering kali rak dan box sudah terpasang dan dipakai setiap hari. Pemasangan dilakukan bertahap per rak agar produksi tetap berjalan. Bracket modul dibuat menyesuaikan profil rak, dan jalur kabel dirapikan agar tidak tersangkut saat box diganti. Setelah terpasang, setiap lokasi diuji satu per satu sesuai daftar part.</p>

<h2>Yang menentukan keberhasilan</h2>
<ul>
  <li>Data part per produk harus benar sejak awal; sistem hanya sebaik datanya.</li>
  <li>Lokasi box tidak boleh dipindah tanpa memperbarui sistem.</li>
  <li>Operator dilatih menggunakan tombol konfirmasi, bukan sekadar mengikuti lampu.</li>
</ul>

<p>Selain menekan salah ambil, pick to light mempercepat pelatihan operator baru dan memudahkan penambahan varian produk, karena perubahan cukup dilakukan di data, bukan di ingatan operator.</p>
'''),
]

def words(h):
    return len(re.sub('<[^>]+>', ' ', h).split())

extra = []
for i, (slug, title, cat, img, contain, summ, body) in enumerate(A):
    mins = max(2, round(words(body) / 200))
    others = [x for x in A if x[0] != slug][:3]
    other_html = '\n'.join(f'''      <a class="card card-hover flex flex-col" href="artikel-{o[0]}.html">
        <div class="media{' contain' if o[4] else ''} ratio-16-10"><img src="assets/img/{o[3]}" alt="" loading="lazy"></div>
        <div class="card-pad flex-1 flex flex-col{' border-t border-[#E6EAF0]' if o[4] else ''}"><p class="meta">{html.escape(o[2])}</p><h3 class="h-card mt-1 flex-1">{html.escape(o[1])}</h3><span class="link-arrow mt-4">Baca selengkapnya<span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></span></div>
      </a>''' for o in others)
    t = html.escape(title)
    frag = f'''<article>
  <header class="page-hero !pb-10">
    <div class="wrap max-w-[56rem]">
      <nav aria-label="Breadcrumb" class="body-sm"><a class="font-semibold text-[#001F4B] hover:underline underline-offset-4" href="artikel.html">Artikel</a><span aria-hidden="true" class="mx-2">/</span><span>{html.escape(cat)}</span></nav>
      <h1 class="h-display !text-[clamp(2rem,4vw,2.875rem)] mt-4">{t}</h1>
      <p class="lede">{html.escape(summ)}</p>
      <p class="body-sm mt-6">Tim Engineering PT Arasi Nusantara Perkasa · {mins} menit baca</p>
    </div>
  </header>
  <div class="wrap max-w-[56rem] pt-10">
    <figure class="media{' contain border border-[#E6EAF0]' if contain else ''} ratio-16-10 rounded-lg"><img src="assets/img/{img}" alt="{t}"></figure>
    <div class="prose-arasi mt-10">
{body.strip()}
    </div>
    <aside class="mt-14 rounded-lg bg-[#F5F7FA] border border-[#E6EAF0] p-6 md:p-8 flex flex-col md:flex-row md:items-center gap-5 justify-between">
      <div>
        <h2 class="h-card">Punya kasus serupa di lini Anda?</h2>
        <p class="body-sm mt-1">Kirim gambar atau ceritakan masalahnya. Tim kami bantu cari solusinya.</p>
      </div>
      <a class="btn btn-primary shrink-0" href="#kontak" data-quote="{t}" data-kategori="Lainnya">Diskusikan dengan tim</a>
    </aside>
  </div>
</article>

<section class="section" aria-labelledby="lain-judul">
  <div class="wrap">
    <div class="section-head-row">
      <h2 id="lain-judul" class="h-section">Artikel lainnya</h2>
      <a class="link-arrow" href="artikel.html">Semua artikel<span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
{other_html}
    </div>
  </div>
</section>
'''
    open(os.path.join(PAGES, f'artikel-{slug}.html'), 'w', encoding='utf-8').write(frag)
    extra.append({'id': f'artikel-{slug}', 'file': f'artikel-{slug}.html', 'active': 'artikel',
                  'title': f'{t} | PT Arasi Nusantara Perkasa', 'desc': html.escape(summ)})

json.dump(extra, open(os.path.join(HERE, 'pages_extra.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('artikel:', len(A))

# --- Halaman daftar artikel (artikel.html) dari data yang sama
f = A[0]
feat = f'''<section class="section" aria-labelledby="unggulan-judul">
  <div class="wrap">
    <h2 id="unggulan-judul" class="sr-only">Artikel unggulan</h2>
    <a class="card card-hover grid lg:grid-cols-2" href="artikel-{f[0]}.html">
      <div class="media{' contain' if f[4] else ''} ratio-16-10 lg:aspect-auto lg:min-h-[22rem] border-b lg:border-b-0 lg:border-r border-[#E6EAF0]"><img src="assets/img/{f[3]}" alt=""></div>
      <div class="card-pad lg:!p-10 flex flex-col justify-center">
        <p class="meta">{html.escape(f[2])}</p>
        <h3 class="h-section !text-[clamp(1.5rem,2.4vw,2rem)] mt-2">{html.escape(f[1])}</h3>
        <p class="body mt-4">{html.escape(f[5])}</p>
        <span class="btn btn-primary mt-8 self-start">Baca selengkapnya<span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></span>
      </div>
    </a>
  </div>
</section>
'''
cards = '\n'.join(f'''      <a class="card card-hover flex flex-col" href="artikel-{o[0]}.html">
        <div class="media{' contain' if o[4] else ''} ratio-16-10"><img src="assets/img/{o[3]}" alt="" loading="lazy"></div>
        <div class="card-pad flex-1 flex flex-col{' border-t border-[#E6EAF0]' if o[4] else ''}">
          <p class="meta">{html.escape(o[2])}</p>
          <h3 class="h-card mt-1">{html.escape(o[1])}</h3>
          <p class="body-sm mt-3 flex-1">{html.escape(o[5])}</p>
          <span class="link-arrow mt-5">Baca selengkapnya<span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></span>
        </div>
      </a>''' for o in A[1:])
listing = f'''<section class="page-hero">
  <div class="wrap">
    <h1 class="h-display">Artikel</h1>
    <p class="lede">Catatan teknis dari pengalaman tim engineering ARASI di lapangan: jig, otomasi, perawatan, dan machining.</p>
  </div>
</section>

{feat}
<section class="section bg-paper-2" aria-labelledby="semua-judul">
  <div class="wrap">
    <div class="section-head">
      <h2 id="semua-judul" class="h-section">Artikel Kami</h2>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
{cards}
    </div>
  </div>
</section>
'''
open(os.path.join(PAGES, 'artikel.html'), 'w', encoding='utf-8').write(listing)
print('listing ok')
