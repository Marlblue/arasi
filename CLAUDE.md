# Catatan untuk Claude

Baca [README.md](README.md) dulu untuk peta folder dan cara deploy-nya. Berkas ini hanya
memuat hal yang khusus berlaku saat mengedit repo ini.

## Situs ini HTML statis, bukan Next.js

Berbeda dengan sdbi, kalih-signature, dan nawwaf_friends, di sini tidak ada Node, pnpm,
maupun build Next. Halaman di `website/` dirakit oleh skrip Python di `_src/`.

- **Jangan menyunting `website/*.html` langsung.** Berkas itu ditimpa setiap build. Isi
  `<main>` ada di `_src/pages/`, header/footer/form kontak di `_src/build.py`, data
  produk/portofolio/artikel di `_src/gen_*.py`.
- Gambar baru masuk ke `website/assets/img/` dan dirujuk dengan path relatif
  (`assets/img/...`). Link antarhalaman juga relatif dan memakai `.html`, supaya situs
  tetap jalan kalau dibuka langsung dari folder tanpa server.

## Gaya tulisan

Berlaku untuk semua yang kamu tulis di repo ini: komentar kode, pesan commit, dokumen,
teks yang dilihat pengunjung, dan jawaban di terminal.

- Bahasa Indonesia untuk teks yang dilihat pengunjung dan untuk komentar.
- **Komentar menjelaskan _kenapa_, bukan _apa_.**
- **Tanpa emoji dan emotikon.** Kalau butuh penanda status di keluaran skrip, pakai kata
  (`OK`, `GAGAL`, `LEWAT`) atau tanda ASCII biasa seperti `->`.
- **Jangan pakai tanda pisah panjang (em dash).** Pakai titik dua, koma, tanda kurung,
  atau pecah jadi dua kalimat.

## Sebelum menyatakan selesai

```bash
python _src/gen_produk.py && python _src/gen_portofolio.py && python _src/gen_artikel.py
python _src/build.py website
```

Lalu buka `website/index.html` di browser dan periksa halaman yang disentuh. Hasil build
di `website/` ikut di-commit: itulah yang dikirim `deploy.yml` ke server.

## Data yang masih menunggu client

- Nomor WhatsApp belum ada; tombol CTA masih memakai form `mailto:`.
- Nama di testimoni beranda berasal dari draf Stitch dan belum dikonfirmasi client.
