# Sumber halaman v1

Halaman di `website/*.html` dirakit dari file di sini, supaya header, form kontak, dan footer sama di semua halaman.

- `pages/*.html`: isi `<main>` untuk beranda, solusi, tentang, dan artikel. Edit langsung di sini.
- `gen_produk.py`, `gen_portofolio.py`: data katalog produk dan daftar proyek. Edit datanya, lalu jalankan skripnya untuk menghasilkan `pages/produk.html` dan `pages/portofolio.html`.
- `gen_artikel.py`: isi semua artikel. Menghasilkan halaman daftar (`pages/artikel.html`), halaman detail (`pages/artikel-<slug>.html`), dan `pages_extra.json`.
- `build.py`: template head, header, form kontak, dan footer.

Cara build (jalankan dari folder `arasi`):

```
python _src/gen_produk.py
python _src/gen_portofolio.py
python _src/gen_artikel.py
python _src/build.py website
```
