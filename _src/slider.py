"""Slider foto/video kecil untuk kartu proyek. Dipakai gen_portofolio.py; potongan HTML-nya juga ditempel di pages/index.html dan pages/solusi.html.

Panggil `python _src/slider.py` untuk mencetak markup ketiga slider otomasi.
"""
import html

# (src, alt, fit, label)  fit: '' = cover, 'contain' = utuh dengan latar putih (gambar CAD),
# 'blur' = utuh di atas versi blur dirinya (foto tegak), 'pos:X% Y%' = cover dengan titik fokus. src .mp4 = video (poster = .jpg bernama sama di img/real).
SLIDES = {
    'robot-painting': [
        ('real/robot-painting-2.jpg', 'Robot painting kolaboratif di atas base stasiun kerja', '', ''),
        ('real/robot-painting-3.jpg', 'Robot painting terpasang di booth pengecatan', 'pos:78% 50%', ''),
        ('real/robot-painting-4.jpg', 'Robot painting di atas base beroda sebelum instalasi', 'contain', ''),
    ],
    'agv': [
        ('real/agv-unit.jpg', 'Unit AGV dengan panel layar dan tombol kontrol', '', ''),
        ('video/agv-run-2.mp4', 'Video AGV menarik troli bumper di jalur produksi', '', ''),
        ('video/agv-run-1.mp4', 'Video troli bumper yang ditarik AGV', '', ''),
    ],
    'pick-to-light': [
        ('real/ptl-before.jpg', 'Rak sebelum pick to light: operator mencari part di banyak lokasi', 'pos:100% 75%', 'Before'),
        ('real/ptl-after.jpg', 'Rak pick to light: operator dipandu lampu langsung ke lokasi part', 'pos:82% 60%', 'After'),
    ],
}


def slider(key, cls='ratio-4-3', extra_img_cls='', lazy=True):
    items = SLIDES[key]
    out = []
    for i, (src, alt, fit, label) in enumerate(items):
        a = html.escape(alt)
        lab = f'<span class="sl-tag">{label}</span>' if label else ''
        if src.endswith('.mp4'):
            poster = 'assets/img/real/' + src.split('/')[-1].replace('.mp4', '.jpg')
            body = f'<video src="assets/{src}" poster="{poster}" muted loop playsinline preload="none" disablepictureinpicture aria-label="{a}"></video>'
        else:
            ld = ' loading="lazy"' if (lazy or i) else ''
            ic = f' class="{extra_img_cls}"' if (extra_img_cls and i == 0) else ''
            st = f' style="object-position:{fit[4:]}"' if fit.startswith('pos:') else ''
            body = f'<img src="assets/img/{src}" alt="{a}"{ld}{ic}{st}>'
            if fit == 'blur':
                body = f'<img class="sl-bg" src="assets/img/{src}" alt="" aria-hidden="true"{ld}>' + body
        fc = {'contain': ' contain', 'blur': ' sl-fill'}.get(fit, '')
        out.append(f'<div class="slide{fc}" role="group" aria-roledescription="slide" aria-label="{i + 1} dari {len(items)}">{body}{lab}</div>')
    dots = ''.join(f'<button type="button" class="sl-dot" data-sl-go="{i}" aria-label="Slide {i + 1}"{" aria-current=\"true\"" if i == 0 else ""}></button>' for i in range(len(items)))
    return (f'<div class="media {cls} slider" data-slider aria-roledescription="carousel">'
            f'<div class="slides" tabindex="0">{"".join(out)}</div>'
            f'<button type="button" class="sl-btn sl-prev" data-sl-prev aria-label="Foto sebelumnya"><span class="material-symbols-outlined" aria-hidden="true">chevron_left</span></button>'
            f'<button type="button" class="sl-btn sl-next" data-sl-next aria-label="Foto berikutnya"><span class="material-symbols-outlined" aria-hidden="true">chevron_right</span></button>'
            f'<div class="sl-dots">{dots}</div></div>')


if __name__ == '__main__':
    for k in SLIDES:
        print(k, '\n', slider(k), '\n')
