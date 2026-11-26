# PT Arasi Nusantara Perkasa

Situs company profile [arasinusa.co.id](https://arasinusa.co.id): jig & fixture,
machining, fabrikasi, integrasi otomasi, dan general supply industri di Cikarang.

HTML statis (Tailwind lewat CDN), di-hosting di Niagahoster (cPanel, server srv178).

## Struktur

```
arasi/
├── website/        Situs siap online. Isinya persis yang ada di public_html.
│   ├── *.html      Hasil build, jangan disunting langsung
│   ├── assets/     css, js, gambar, video
│   ├── .htaccess   HTTPS, URL tanpa .html, cache
│   └── sitemap.xml, robots.txt (dibuat build.py)
├── _src/           Sumber halaman
│   ├── build.py        head, header, form kontak, footer, sitemap
│   ├── slider.py       slider proyek otomasi (AGV, Robot Painting, Pick To Light)
│   ├── gen_produk.py   katalog produk     -> pages/produk.html
│   ├── gen_portofolio.py daftar proyek   -> pages/portofolio.html
│   ├── gen_artikel.py  semua artikel      -> pages/artikel*.html + pages_extra.json
│   └── pages/          isi <main> tiap halaman
├── bahan/          Bahan mentah dari client (tidak masuk git)
└── deploy/         Zip untuk upload manual (tidak masuk git)
```

## Mengubah isi lalu build

Jalankan dari folder `arasi`:

```bash
python _src/gen_produk.py
python _src/gen_portofolio.py
python _src/gen_artikel.py
python _src/build.py website
```

Cukup jalankan `gen_*` yang datanya diubah. `build.py` selalu dijalankan terakhir.

## Deploy

### Otomatis (GitHub Actions)

Push ke `main` menjalankan [`deploy.yml`](.github/workflows/deploy.yml): build ulang,
kirim `website/` ke server lewat SSH, lalu memastikan situs membalas versi yang baru.
Secrets yang dibutuhkan (Settings > Secrets and variables > Actions):

| Secret | Isi |
| --- | --- |
| `SSH_HOST` | `109.106.252.156` (IP server) |
| `SSH_PORT` | `65002` |
| `SSH_USERNAME` | Username cPanel |
| `SSH_PRIVATE_KEY` | Private key; public key-nya di-import dan di-Authorize di cPanel > SSH Access > Manage SSH Keys |
| `SSH_PASSPHRASE` | Kosongkan kalau key tanpa passphrase |
| `DEPLOY_PATH` | Opsional. Default `public_html` (atau `domains/arasinusa.co.id/public_html` kalau ada) |
| `OPS_ALERT_WEBHOOK_URL` | Webhook grup Telegram, sama dengan repo client lain |

### Manual (File Manager hPanel)

```bash
python -c "import shutil; shutil.make_archive('deploy/arasinusa-upload-public_html', 'zip', 'website')"
```

Upload zip-nya ke `public_html` lewat File Manager, lalu Extract di tempat. Pastikan
`index.html` ada langsung di `public_html`, bukan di subfolder.

## Pemantauan

Sama seperti repo client lain, memakai action dari `Marlblue/website-ops`:

- [`uptime.yml`](.github/workflows/uptime.yml): cek situs hidup tiap 30 menit
- [`domain.yml`](.github/workflows/domain.yml): pengingat masa berlaku domain
- [`cek-link.yml`](.github/workflows/cek-link.yml): link dan gambar rusak, tiap Senin

## Kontak resmi (dipakai di seluruh situs)

- Email: admin@arasinusa.co.id
- Telepon: (021) 897 74919
- Kantor: Ruko Lafenza Villa Mutiara Cikarang 1 Blok R4 No.36
- Workshop: Kp. Nambo RT011/RW008, Sukasejati, Cikarang Selatan
