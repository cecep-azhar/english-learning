# Task Breakdown — English for Remote Worker

**Repo:** `/home/cecep/Projects/english-learning`
**Dokumen terkait:** [`notes/prd.md`](./prd.md) (v2.0)
**Versi:** 1.0
**Tanggal:** 3 Agustus 2026
**Basis audit:** commit `46b960b`

---

## Cara Membaca Dokumen Ini

Setiap task punya format yang sama:

| Field | Arti |
|---|---|
| **ID** | Kode unik (`A1`, `B2`, …). Dipakai di commit message: `fix(A1): ...` |
| **Prioritas** | P0–P4, lihat tabel di bawah |
| **Estimasi** | Jam kerja fokus, bukan hari kalender |
| **Depends on** | Task yang harus selesai duluan |
| **Files** | File yang akan disentuh |
| **Masalah** | Kenapa task ini ada |
| **Bukti** | Referensi `file:line` hasil audit — bisa diverifikasi sendiri |
| **Langkah** | Checklist implementasi |
| **Acceptance criteria** | Definisi "selesai". Kalau belum semua ✅, task belum selesai |
| **Verifikasi** | Perintah shell untuk membuktikan AC terpenuhi |

### Definisi Prioritas

| Level | Arti | Aturan |
|---|---|---|
| **P0** | Produk saat ini menjanjikan sesuatu yang tidak ada / tidak jalan | Kerjakan sekarang. Jangan kerjakan P1+ sebelum P0 habis |
| **P1** | Menghalangi validasi bisnis (bisa/tidaknya dapat uang) | Setelah P0 |
| **P2** | Higiene: dokumen, infra, observability | Sela-sela |
| **P3** | Rewrite backend Go — **hanya jalan kalau P1 terbukti** | Gated |
| **P4** | Growth & fitur lanjutan | Terakhir |

### Legend Status

`[ ]` belum · `[~]` sedang dikerjakan · `[x]` selesai · `[!]` terblokir · `[-]` dibatalkan

---

## 0. Ringkasan Eksekutif

Audit kode menemukan **jarak besar antara apa yang dijanjikan dan apa yang jalan**:

> Landing page menjual **11 kategori**. Kode hanya bisa menyajikan **1** (`software-engineering`).
> Audio hanya ada untuk **1** kategori itu juga.
> Dan Dockerfile bahkan **tidak mengirim** landing page, quiz, pricing, atau blog ke production.

Artinya: user yang datang dari landing page, klik "Mulai Belajar" di kategori mana pun, akan mendarat di aplikasi Software Engineering yang sama — tanpa pesan error, tanpa penjelasan. Ini bukan bug kosmetik; ini janji produk yang tidak terpenuhi.

**Konsekuensi untuk urutan kerja:** Semua rencana Go migration (P3) ditunda sampai P0 dan P1 selesai. Tidak ada gunanya me-rewrite backend untuk produk yang fitur intinya belum tersambung.

### Peta Epic

| Epic | Judul | Prioritas | Est. | Blocking? |
|---|---|---|---|---|
| **A** | Sambungkan 11 kategori ke aplikasi | P0 | 14 j | Ya — klaim utama produk |
| **B** | Perbaiki deployment pipeline | P0 | 5 j | Ya — hasil kerja tidak sampai production |
| **C** | Lengkapi audio 10 kategori | P1 | 8 j | Ya — skill "Listening" |
| **D** | Monetisasi manual (validasi pasar) | P1 | 10 j | Ya — gate untuk P3 |
| **E** | Konsistensi pricing, legal, refund | P1 | 7 j | Ya — syarat Mayar.id |
| **F** | Analytics & instrumentation | P2 | 6 j | KPI tidak terukur tanpa ini |
| **G** | Higiene repo & dokumentasi | P2 | 5 j | — |
| **H** | Backend Go: auth, DB, progress sync | P3 | 60 j | Gated oleh D |
| **I** | Otomasi pembayaran Mayar.id | P3 | 24 j | Gated oleh H |
| **J** | AI writing & speaking feedback | P4 | 32 j | Gated oleh I |
| **K** | Growth: PWA, SEO, community | P4 | 40 j | — |

**Total P0+P1+P2 ≈ 55 jam** (~2 minggu kerja part-time). Ini yang harus selesai sebelum keputusan besar apa pun.

### Jalur Kritis

```
A1 ──> A2 ──> A3 ──> A4 ──┐
                          ├──> B1 ──> B2 ──> [DEPLOY SEHAT]
C1 ──> C2 ─────────────────┘                      │
                                                  ▼
                                    E1 ──> E2 ──> D1 ──> D2 ──> D3
                                                          │
                                              [30 hari observasi]
                                                          │
                                                          ▼
                                        ┌── ≥20 pembeli? ──┐
                                       YA                 TIDAK
                                        │                   │
                                        ▼                   ▼
                                   Epic H (Go)      Pivot / iterasi konten
```

---

# EPIC A — P0: Sambungkan 11 Kategori ke Aplikasi

**Konteks.** Commit `46b960b` berjudul *"11 categories + admin panel + category selection"*. Isinya: 11 file JSON konten, admin panel, dan 11 kartu kategori di landing page. Yang **tidak** ada di commit itu: kode apa pun yang membuat aplikasi belajar membaca kategori. `index.html` dan `quiz.html` tidak berubah sama sekali.

Hasilnya, ada tiga sistem penamaan yang tidak saling cocok, dan tidak ada router di antaranya.

## Tabel Ketidakcocokan Slug (inti masalah)

| Kartu di landing (`href`) | `id` di `categories.json` | Nama file di `content/` | `id` di dalam file | Cocok? |
|---|---|---|---|---|
| `general-english` | `general` | `general.json` | `general` | ❌ slug |
| `business-english` | `business` | `business.json` | `business` | ❌ slug |
| `finance-english` | `finance` | `finance.json` | `finance` | ❌ slug |
| `administration` | `admin` | `admin.json` | `admin` | ❌ slug |
| `web-design` | `web-design` | `webdesign.json` | `webdesign` | ❌ file + id |
| `seo-specialist` | `seo` | `seo.json` | `seo` | ❌ slug |
| `graphic-design` | `design` | `graphic-design.json` | `graphic-design` | ❌ id manifest |
| `video-editing` | `video-editing` | `video-editing.json` | `video-editing` | ✅ |
| `virtual-assistant` | `virtual-assistant` | `virtual-assistant.json` | `virtual-assistant` | ✅ |
| `copywriting` | `copywriting` | `copywriting.json` | `copywriting` | ✅ |
| `software-engineering` | `software-engineering` | `software-engineering.json` | `software-engineering` | ✅ |

**Keputusan:** slug kanonik = `id` di `categories.json`, dengan dua koreksi (`design` → `graphic-design`, dan file `webdesign.json` → `web-design.json`). Semua tempat lain menyesuaikan.

### Slug Kanonik Final

```
general · business · finance · admin · web-design · seo
graphic-design · video-editing · virtual-assistant · copywriting · software-engineering
```

---

## A1 — Tetapkan slug kanonik & normalisasi file konten

| | |
|---|---|
| **ID** | A1 |
| **Prioritas** | P0 |
| **Estimasi** | 2 jam |
| **Depends on** | — |
| **Files** | `content/categories.json`, `content/webdesign.json`, `content/graphic-design.json`, `content/all-categories.json` |

**Masalah**
Tiga sumber penamaan berbeda. Tanpa satu slug kanonik, task A2–A4 tidak punya kontrak yang stabil untuk dikodekan.

**Bukti**
- `content/categories.json` → `id: "design"`, tapi file bernama `graphic-design.json` dengan `id: "graphic-design"` di dalamnya
- `content/categories.json` → `id: "web-design"`, tapi file bernama `webdesign.json` dengan `id: "webdesign"` di dalamnya

**Langkah**
- [ ] `git mv content/webdesign.json content/web-design.json`
- [ ] Di `content/web-design.json`, ubah `"id": "webdesign"` → `"id": "web-design"`
- [ ] Di `content/categories.json`, ubah entri `"id": "design"` → `"id": "graphic-design"`
- [ ] Regenerasi `content/all-categories.json` dari 11 file kategori supaya `id`-nya ikut terkoreksi (jangan edit manual — file 4.638 baris)
- [ ] Tambahkan field `"slug"` eksplisit di setiap entri `categories.json` (nilainya sama dengan `id`) supaya niatnya terbaca jelas oleh pembaca kode berikutnya

**Acceptance criteria**
- [ ] Untuk semua 11 kategori: nama file (tanpa `.json`) == `id` di dalam file == `id` di `categories.json`
- [ ] `all-categories.json` konsisten dengan 11 file individual (jumlah item dan `id` sama persis)
- [ ] Tidak ada file bernama `webdesign.json` tersisa

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
python3 - <<'EOF'
import json, glob, os
man = {c['id'] for c in json.load(open('content/categories.json'))['categories']}
files, ok = {}, True
for f in glob.glob('content/*.json'):
    b = os.path.basename(f)[:-5]
    if b in ('categories', 'all-categories'): continue
    d = json.load(open(f)); files[b] = d['id']
    if b != d['id']:
        print(f'MISMATCH file/id: {b} != {d["id"]}'); ok = False
if man != set(files):
    print('MISMATCH manifest:', man ^ set(files)); ok = False
print('A1 PASS' if ok else 'A1 FAIL')
EOF
```

---

## A2 — Bangun router kategori di aplikasi belajar

| | |
|---|---|
| **ID** | A2 |
| **Prioritas** | P0 |
| **Estimasi** | 5 jam |
| **Depends on** | A1 |
| **Files** | `index.html`, `quiz.html` |

**Masalah**
`index.html` mengambil `scripts.json` (120 item Software Engineering) tanpa pernah melihat query parameter. Query `?category=` diabaikan total. Semua kartu kategori mendarat di konten yang sama.

**Bukti**
- `index.html:558` → `fetch('scripts.json')` — hardcoded
- `quiz.html:3361` → `fetch('/scripts.json')` — hardcoded
- `grep -n "URLSearchParams\|location.search\|category" index.html` → **0 hasil**
- `nginx.conf` → `try_files $uri $uri/ /index.html`, jadi `/app` jatuh ke `index.html` tanpa error — kegagalan jadi tak terlihat

**Langkah**
- [ ] Buat modul bersama `resolveCategory()`:
  ```js
  const CANONICAL = ['general','business','finance','admin','web-design','seo',
                     'graphic-design','video-editing','virtual-assistant',
                     'copywriting','software-engineering'];
  const DEFAULT_CATEGORY = 'software-engineering';

  function resolveCategory() {
    const raw = new URLSearchParams(location.search).get('category');
    if (!raw) return { slug: DEFAULT_CATEGORY, wasInvalid: false };
    if (CANONICAL.includes(raw)) return { slug: raw, wasInvalid: false };
    return { slug: DEFAULT_CATEGORY, wasInvalid: true, attempted: raw };
  }
  ```
- [ ] Ganti fetch hardcoded jadi `fetch(\`/content/${slug}.json\`)`
- [ ] Tangani perbedaan bentuk data: `scripts.json` punya `{title, total_items, scripts}`; file kategori punya `{id, name, scripts}`. Buat adapter `normalizeContent(raw)` yang mengembalikan bentuk seragam
- [ ] Kalau slug tidak valid → fallback ke default **dan** tampilkan toast: `"Kategori tidak dikenal, menampilkan Software Engineering"`. Jangan gagal diam-diam
- [ ] Kalau fetch gagal (404/network) → tampilkan error state yang bisa dibaca user + tombol "Coba lagi", bukan halaman kosong
- [ ] Simpan slug aktif ke `sessionStorage` supaya navigasi `index.html` → `quiz.html` mempertahankan kategori
- [ ] Tampilkan nama + ikon kategori aktif di header aplikasi, supaya user tahu dia sedang di mana

**Acceptance criteria**
- [ ] `?category=copywriting` memuat 45 item copywriting, bukan software engineering
- [ ] Ke-11 slug kanonik memuat konten yang berbeda-beda
- [ ] Tanpa parameter → default `software-engineering` (backward compatible dengan bookmark lama)
- [ ] Slug tidak valid (`?category=xxx`) → fallback + toast terlihat, aplikasi tidak crash
- [ ] Nama kategori aktif terlihat di header
- [ ] Pindah dari `index.html` ke `quiz.html` tidak mereset kategori

**Verifikasi**
```bash
# Jalankan server lokal, lalu untuk tiap slug pastikan judul kategori berubah
cd /home/cecep/Projects/english-learning && python3 -m http.server 8080 &
for s in general business finance admin web-design seo graphic-design \
         video-editing virtual-assistant copywriting software-engineering; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "http://localhost:8080/content/$s.json")
  echo "$s -> HTTP $code"
done
# Semua harus 200. Lalu uji manual di browser untuk 3 slug + 1 slug invalid.
```

---

## A3 — Perbaiki link kategori di landing page

| | |
|---|---|
| **ID** | A3 |
| **Prioritas** | P0 |
| **Estimasi** | 1 jam |
| **Depends on** | A1 |
| **Files** | `landing.html` |

**Masalah**
5 dari 11 `href` memakai slug yang tidak ada di sistem mana pun.

**Bukti**
`landing.html:906,912,918,924,936` → `general-english`, `business-english`, `finance-english`, `administration`, `seo-specialist` — tidak satu pun cocok dengan `categories.json`.

**Langkah**
- [ ] Update 5 `href` bermasalah ke slug kanonik:

  | Baris | Dari | Ke |
  |---|---|---|
  | 906 | `/app?category=general-english` | `/app?category=general` |
  | 912 | `/app?category=business-english` | `/app?category=business` |
  | 918 | `/app?category=finance-english` | `/app?category=finance` |
  | 924 | `/app?category=administration` | `/app?category=admin` |
  | 936 | `/app?category=seo-specialist` | `/app?category=seo` |

- [ ] Verifikasi 6 sisanya sudah benar (`web-design`, `graphic-design`, `video-editing`, `virtual-assistant`, `copywriting`, `software-engineering`)
- [ ] **Rencana jangka menengah:** render kartu kategori dari `categories.json` alih-alih hardcode 11 blok HTML. Selama masih hardcode, masalah ini akan terulang setiap kali kategori ditambah. (Task terpisah: A6)

**Acceptance criteria**
- [ ] Semua 11 `href` memakai slug kanonik
- [ ] Tidak ada slug di `landing.html` yang absen dari `categories.json`

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
python3 - <<'EOF'
import json, re
canon = {c['id'] for c in json.load(open('content/categories.json'))['categories']}
found = set(re.findall(r'/app\?category=([a-z-]+)', open('landing.html').read()))
bad = found - canon
print('A3 PASS' if not bad and len(found) == 11 else f'A3 FAIL: {bad or f"hanya {len(found)} link"}')
EOF
```

---

## A4 — Tambahkan route `/app` di nginx

| | |
|---|---|
| **ID** | A4 |
| **Prioritas** | P0 |
| **Estimasi** | 1 jam |
| **Depends on** | A2 |
| **Files** | `nginx.conf` |

**Masalah**
Tidak ada route `/app`. Sekarang ia "bekerja" hanya karena `try_files` melempar semua yang tidak ketemu ke `index.html`. Fallback yang sama membuat semua typo URL diam-diam menampilkan aplikasi, sehingga 404 asli tidak pernah terlihat.

**Bukti**
`nginx.conf` → `location / { try_files $uri $uri/ /index.html; }`, tanpa blok `/app`.

**Langkah**
- [ ] Tambah route eksplisit:
  ```nginx
  location = /app     { try_files /index.html =404; }
  location = /        { try_files /landing.html =404; }
  location = /quiz    { try_files /quiz.html =404; }
  location = /pricing { try_files /pricing.html =404; }
  location = /admin   { try_files /admin.html =404; }
  ```
- [ ] Ubah fallback global jadi `=404`, bukan `/index.html`, supaya URL salah benar-benar 404
- [ ] Buat halaman `404.html` sederhana dengan link balik ke `/`
- [ ] Pastikan `/content/*.json` tercakup blok cache JSON yang sudah ada

**Acceptance criteria**
- [ ] `/` → landing page (bukan aplikasi)
- [ ] `/app` → aplikasi belajar
- [ ] `/quiz`, `/pricing`, `/admin` bisa diakses
- [ ] `/halaman-ngawur` → HTTP 404, bukan 200
- [ ] `nginx -t` lolos

**Verifikasi**
```bash
docker build -t el-test . && docker run --rm -d -p 8081:3000 --name el-test el-test
sleep 2
for p in / /app /quiz /pricing /admin /halaman-ngawur; do
  echo "$p -> $(curl -s -o /dev/null -w '%{http_code}' http://localhost:8081$p)"
done   # harapan: 200 200 200 200 200 404
docker rm -f el-test
```

---

## A5 — Gate kategori tanpa audio (jujur ke user)

| | |
|---|---|
| **ID** | A5 |
| **Prioritas** | P0 |
| **Estimasi** | 3 jam |
| **Depends on** | A2 |
| **Files** | `quiz.html`, `index.html`, `content/categories.json` |

**Masalah**
Sampai Epic C selesai, 10 kategori tidak punya audio. Menyajikan mode Listening yang setiap soalnya memunculkan toast `"Audio tidak tersedia"` lebih buruk daripada menyembunyikannya dengan penjelasan jujur.

**Bukti**
- `quiz.html:2517-2520` → `audio.onerror` hanya `showToast('Audio tidak tersedia', 'warning')`
- Folder `audio/` berisi 240 file, **semua bernama numerik** (`1.mp3` … `120_id.mp3`)
- Kategori baru memakai `num_id` string (`"copywriting_001"`) → `/audio/copywriting_001.mp3` → 404

**Langkah**
- [ ] Tambah field `"hasAudio": true|false` per kategori di `categories.json` (hanya `software-engineering` yang `true` saat ini)
- [ ] Kalau `hasAudio === false`: sembunyikan mode Listening, tampilkan badge *"Audio segera hadir"* pada kartu kategori
- [ ] Mode Reading, Vocabulary, Fill-in-blank tetap aktif (tidak butuh audio)
- [ ] Mode Speaking tetap aktif (pakai mikrofon, bukan playback)
- [ ] Tambah tombol *"Beri tahu saya saat audio siap"* → tampung email (bisa Google Form dulu). Ini sekaligus mengubah kekurangan jadi kanal akuisisi
- [ ] Setelah Epic C selesai, flip semua `hasAudio` jadi `true` dan hapus gate ini

**Acceptance criteria**
- [ ] Kategori tanpa audio tidak menampilkan mode Listening sama sekali
- [ ] Badge "Audio segera hadir" terlihat di landing + di dalam app
- [ ] Tidak ada toast `"Audio tidak tersedia"` yang muncul dalam pemakaian normal
- [ ] `software-engineering` tidak terpengaruh — Listening tetap jalan penuh

**Verifikasi**
```bash
# Manual: buka /app?category=copywriting
#  → mode Listening tidak ada, badge terlihat, tidak ada toast error
# Buka /app?category=software-engineering
#  → Listening ada dan audio berbunyi
```

---

## A6 — Render kartu kategori dari manifest (anti-regresi)

| | |
|---|---|
| **ID** | A6 |
| **Prioritas** | P0 |
| **Estimasi** | 2 jam |
| **Depends on** | A3 |
| **Files** | `landing.html` |

**Masalah**
11 kartu kategori ditulis tangan sebagai HTML statis (`landing.html:902-966`), termasuk ikon, warna, deskripsi, dan slug — semuanya duplikat dari `categories.json`. Duplikasi inilah penyebab langsung bug A3, dan akan menyebabkannya lagi.

**Langkah**
- [ ] Ganti 11 blok statis dengan satu `<template>` + loop yang membaca `content/categories.json`
- [ ] Ambil `icon`, `name`, `description`, `color`, `id` dari manifest
- [ ] Render badge `hasAudio` (dari A5) di loop yang sama
- [ ] Sediakan fallback SSR-friendly: kalau JS mati, tampilkan `<noscript>` berisi daftar link biasa (penting untuk SEO)

**Acceptance criteria**
- [ ] Menambah kategori ke-12 hanya butuh 1 file JSON baru + 1 entri manifest — **nol** perubahan HTML
- [ ] Halaman tetap punya link kategori yang bisa dirayapi crawler saat JS mati
- [ ] Tampilan visual identik dengan versi hardcode

---

# EPIC B — P0: Perbaiki Deployment Pipeline

## B1 — Dockerfile tidak mengirim sebagian besar aplikasi

| | |
|---|---|
| **ID** | B1 |
| **Prioritas** | P0 |
| **Estimasi** | 2 jam |
| **Depends on** | — |
| **Files** | `Dockerfile`, `.dockerignore` |

**Masalah**
**Ini kemungkinan bug paling mahal di repo.** Dockerfile hanya menyalin `index.html`, `scripts.json`, dan `audio/`. Semua hasil kerja dari tiga commit terakhir — landing page, pricing, quiz, admin panel, blog, dan seluruh folder `content/` — **tidak pernah masuk image production**.

Kalau `english.tool.biz.id` di-deploy dari Dockerfile ini, yang online adalah aplikasi satu-kategori versi lama. Landing page, halaman harga, dan 3 artikel blog yang dibuat di commit `d62feb2` tidak ada di internet.

**Bukti**
```dockerfile
COPY index.html   /usr/share/nginx/html/index.html
COPY scripts.json /usr/share/nginx/html/scripts.json
COPY audio/       /usr/share/nginx/html/audio/
```
Tidak ada `quiz.html`, `landing.html`, `pricing.html`, `admin.html`, `blog/`, `content/`.

**Langkah**
- [ ] Ganti daftar COPY selektif dengan salin-semua + `.dockerignore` yang ketat:
  ```dockerfile
  FROM nginx:alpine
  COPY nginx.conf /etc/nginx/nginx.conf
  COPY . /usr/share/nginx/html/
  EXPOSE 3000
  CMD ["nginx", "-g", "daemon off;"]
  ```
- [ ] Perketat `.dockerignore` — pola inklusi yang lupa diperbarui adalah akar masalah ini; pola eksklusi gagal ke arah yang lebih aman:
  ```
  .git
  .gitignore
  .dockerignore
  Dockerfile
  *.md
  notes/
  *.py
  pdf_content.txt
  .claude/
  .env*
  ```
- [ ] **Penting:** `admin.html` (73 KB) sekarang ikut ter-deploy dan terbuka untuk publik. Lihat B3 sebelum deploy
- [ ] Tambah `HEALTHCHECK` untuk deteksi image rusak lebih awal

**Acceptance criteria**
- [ ] `docker build` menghasilkan image yang menyajikan **semua** halaman: `/`, `/app`, `/quiz`, `/pricing`, `/admin`, `/blog/`
- [ ] Ke-11 file `content/*.json` bisa diambil dari container
- [ ] File Python, Markdown, dan `.git` **tidak** ada di dalam image
- [ ] Ukuran image tidak melonjak (perkiraan: ~15 MB + audio)

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
docker build -t el-verify . && docker run --rm -d -p 8082:3000 --name el-verify el-verify
sleep 2
echo "--- halaman ---"
for p in / /app /quiz /pricing /admin /blog/ /blog/interview-english-developer.html; do
  echo "$p -> $(curl -s -o /dev/null -w '%{http_code}' http://localhost:8082$p)"
done
echo "--- konten ---"
for s in general business finance admin web-design seo graphic-design \
         video-editing virtual-assistant copywriting software-engineering; do
  echo "$s -> $(curl -s -o /dev/null -w '%{http_code}' http://localhost:8082/content/$s.json)"
done
echo "--- tidak boleh bocor ---"
docker exec el-verify sh -c 'ls /usr/share/nginx/html/*.py /usr/share/nginx/html/*.md 2>&1 | head -3'
docker rm -f el-verify
```

---

## B2 — Selaraskan domain di seluruh repo

| | |
|---|---|
| **ID** | B2 |
| **Prioritas** | P0 |
| **Estimasi** | 1 jam |
| **Depends on** | — |
| **Files** | `PRD.md` (lama), `notes/prd.md`, semua HTML |

**Masalah**
Dua domain hidup berdampingan. Yang paling berbahaya: config Cloudflare Tunnel di dokumen masih menunjuk hostname lama, jadi menyalinnya saat deploy akan mengarahkan traffic ke tempat yang salah.

**Bukti**
```
15× english.tool.biz.id   (HTML — hasil rebrand commit 676d025)
 4× english.ypc.my.id     (PRD.md — termasuk config tunnel & structured data)
```

**Langkah**
- [ ] Tetapkan `english.tool.biz.id` sebagai domain kanonik
- [ ] Ganti semua `english.ypc.my.id` yang tersisa
- [ ] Update `ingress.hostname` di config Cloudflare Tunnel
- [ ] Update `og:url` dan JSON-LD `url` di semua halaman
- [ ] Tambah `<link rel="canonical">` di setiap halaman
- [ ] Kalau domain lama masih ada DNS-nya, pasang redirect 301 → domain baru (jaga link equity SEO)

**Acceptance criteria**
- [ ] `grep -r "ypc.my.id" .` → nol hasil (kecuali catatan histori di `notes/`)
- [ ] Semua `og:url`, canonical, dan JSON-LD memakai `english.tool.biz.id`

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
n=$(grep -r "ypc\.my\.id" --exclude-dir=.git --exclude-dir=notes . | wc -l)
echo "sisa referensi domain lama: $n"; [ "$n" -eq 0 ] && echo "B2 PASS" || echo "B2 FAIL"
```

---

## B3 — Amankan admin panel sebelum ter-deploy publik

| | |
|---|---|
| **ID** | B3 |
| **Prioritas** | P0 |
| **Estimasi** | 2 jam |
| **Depends on** | B1 |
| **Files** | `nginx.conf`, `Dockerfile`, `admin.html` |

**Masalah**
Setelah B1, `admin.html` (73 KB) ikut terkirim ke production. Ini file statis tanpa autentikasi apa pun — siapa pun yang menebak `/admin` bisa membukanya. Perbaikan B1 secara tidak sengaja menciptakan lubang ini, jadi keduanya harus dirilis bersamaan.

**Langkah**
- [ ] Pilih salah satu (rekomendasi: opsi 1 untuk sekarang):
  1. **Jangan deploy** — tambah `admin.html` ke `.dockerignore`, pakai hanya secara lokal
  2. **Basic auth nginx** — `auth_basic` + file `.htpasswd` via secret
  3. **Cloudflare Access** — gratis untuk tim kecil, SSO, tanpa kredensial di repo
- [ ] Kalau di-deploy: tambah `X-Robots-Tag: noindex, nofollow` pada route `/admin`
- [ ] Tambah `Disallow: /admin` di `robots.txt`
- [ ] Audit `admin.html` — pastikan tidak ada API key/token yang tertanam di dalamnya

**Acceptance criteria**
- [ ] `/admin` di production tidak bisa diakses anonim (atau tidak ada sama sekali)
- [ ] Tidak ada kredensial hardcoded di `admin.html`
- [ ] `robots.txt` melarang `/admin`

**Verifikasi**
```bash
# Opsi 1: harus 404
curl -s -o /dev/null -w '%{http_code}\n' http://localhost:8082/admin
# Opsi 2: harus 401 tanpa kredensial
grep -inE "api[_-]?key|secret|token|password" admin.html | head
```

---

# EPIC C — P1: Lengkapi Audio 10 Kategori

## C1 — Perbaiki `generate_audio.py`

| | |
|---|---|
| **ID** | C1 |
| **Prioritas** | P1 |
| **Estimasi** | 3 jam |
| **Depends on** | A1 |
| **Files** | `generate_audio.py` |

**Masalah**
Script memakai path absolut yang salah dan hanya membaca `scripts.json`. Dijalankan apa adanya, ia akan gagal (direktori tidak ada) atau tidak menghasilkan apa-apa.

**Bukti**
```python
AUDIO_DIR    = "/home/cecep/english-learning/audio"    # repo asli: /home/cecep/Projects/english-learning
SCRIPTS_FILE = "/home/cecep/english-learning/scripts.json"  # hanya 1 kategori
```

**Langkah**
- [ ] Ganti path absolut jadi relatif terhadap lokasi script: `Path(__file__).parent`
- [ ] Terima argumen CLI: `--category <slug>` atau `--all`
- [ ] Iterasi `content/*.json`, bukan hanya `scripts.json`
- [ ] Pertahankan logika skip-jika-sudah-ada (sudah benar, jangan diubah)
- [ ] Perbaiki pesan progress yang salah hitung di baris `print(f"Generating {len(tasks)} ...")` — ekspresi `len([t for t in tasks if t])` menghitung coroutine, selalu sama dengan `len(tasks)`, jadi angkanya tidak bermakna
- [ ] Tambah retry dengan backoff — `edge-tts` sesekali gagal karena rate limit
- [ ] Tulis manifest hasil ke `audio/manifest.json` supaya frontend bisa cek ketersediaan tanpa menembak 404

**Acceptance criteria**
- [ ] `python3 generate_audio.py --category copywriting` menghasilkan 90 file (45 EN + 45 ID)
- [ ] Jalan lagi = nol file baru (idempoten)
- [ ] Tidak ada path absolut tersisa di script
- [ ] Kegagalan per-file tidak menghentikan seluruh batch

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
grep -c "/home/cecep/english-learning" generate_audio.py   # harus 0
python3 generate_audio.py --category copywriting
ls audio/copywriting_*.mp3 | wc -l                          # harus 90
python3 generate_audio.py --category copywriting            # harus "Nothing to generate"
```

---

## C2 — Generate 902 file audio yang hilang

| | |
|---|---|
| **ID** | C2 |
| **Prioritas** | P1 |
| **Estimasi** | 4 jam (sebagian besar waktu tunggu) |
| **Depends on** | C1 |
| **Files** | `audio/` |

**Masalah**
571 item konten × 2 bahasa = 1.142 file dibutuhkan. Hanya 240 yang ada. **902 file hilang.**

**Inventaris**

| Kategori | Item | Audio dibutuhkan | Status |
|---|---:|---:|---|
| `software-engineering` | 120 | 240 | ✅ ada |
| `general` | 46 | 92 | ❌ |
| `business` | 45 | 90 | ❌ |
| `finance` | 45 | 90 | ❌ |
| `admin` | 45 | 90 | ❌ |
| `web-design` | 45 | 90 | ❌ |
| `seo` | 45 | 90 | ❌ |
| `graphic-design` | 45 | 90 | ❌ |
| `video-editing` | 45 | 90 | ❌ |
| `virtual-assistant` | 45 | 90 | ❌ |
| `copywriting` | 45 | 90 | ❌ |
| **TOTAL** | **571** | **1.142** | **240 ada / 902 hilang** |

**Estimasi ukuran:** 240 file = 7,2 MB (~30 KB/file). 902 file ≈ **27 MB**, total repo audio ≈ **34 MB**. Masih wajar untuk git, tapi lihat catatan Git LFS di G3.

**Langkah**
- [ ] Jalankan `python3 generate_audio.py --all`
- [ ] QA sampel: dengarkan 3 file acak per kategori — cek pengucapan istilah teknis (`API`, `SEO`, `UI/UX`, `CTA`) yang sering dibaca aneh oleh TTS
- [ ] Untuk istilah yang salah baca, tambahkan override SSML atau ejaan fonetik di file konten
- [ ] Verifikasi tidak ada file 0-byte (indikasi generate gagal separuh)
- [ ] Update `hasAudio: true` untuk semua kategori di `categories.json` (membalik gate A5)
- [ ] Kalau ukuran repo jadi masalah, pertimbangkan pindah audio ke Cloudflare R2 (gratis untuk volume ini)

**Acceptance criteria**
- [ ] `ls audio/*.mp3 | wc -l` == 1142
- [ ] Setiap `num_id` di setiap file kategori punya `{num_id}.mp3` **dan** `{num_id}_id.mp3`
- [ ] Tidak ada file 0-byte
- [ ] Mode Listening jalan di ke-11 kategori
- [ ] Gate A5 dihapus

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
python3 - <<'EOF'
import json, glob, os
missing, empty = [], []
for f in glob.glob('content/*.json'):
    b = os.path.basename(f)
    if b in ('categories.json', 'all-categories.json'): continue
    for s in json.load(open(f))['scripts']:
        for p in (f"audio/{s['num_id']}.mp3", f"audio/{s['num_id']}_id.mp3"):
            if not os.path.exists(p): missing.append(p)
            elif os.path.getsize(p) == 0: empty.append(p)
print(f'hilang: {len(missing)} | kosong: {len(empty)}')
for p in missing[:5]: print('  -', p)
print('C2 PASS' if not missing and not empty else 'C2 FAIL')
EOF
```

---

## C3 — Fallback `speechSynthesis` (jaring pengaman)

| | |
|---|---|
| **ID** | C3 |
| **Prioritas** | P1 |
| **Estimasi** | 1 jam |
| **Depends on** | — |
| **Files** | `quiz.html`, `index.html` |

**Masalah**
Meski C2 selesai, satu file rusak atau CDN meleset tetap membuat soal Listening tidak bisa dikerjakan. Web Speech Synthesis API tersedia gratis di semua browser modern dan bisa jadi jaring pengaman.

**Catatan:** `speechSynthesis` (text-to-speech, untuk C3) berbeda dari `SpeechRecognition` (speech-to-text, dipakai modul Speaking). Yang pertama didukung luas termasuk Safari iOS; yang kedua tidak — lihat risiko R-01 di PRD.

**Langkah**
- [ ] Di `playAudio` (`quiz.html:2511`), ganti toast error dengan fallback:
  ```js
  audio.onerror = () => {
    btn.classList.remove('playing');
    if ('speechSynthesis' in window) {
      const u = new SpeechSynthesisUtterance(text);
      u.lang = src.includes('_id') ? 'id-ID' : 'en-US';
      u.rate = 0.9;
      u.onend = () => btn.classList.remove('playing');
      speechSynthesis.speak(u);
      showToast('Memakai suara sintetis', 'info');
    } else {
      showToast('Audio tidak tersedia', 'warning');
    }
  };
  ```
- [ ] Teruskan teks sumber ke `playAudio` (saat ini hanya menerima URL)
- [ ] Pastikan `speechSynthesis.cancel()` dipanggil saat pindah soal, agar suara tidak menumpuk

**Acceptance criteria**
- [ ] Menghapus satu file mp3 → soal Listening tetap bisa dikerjakan lewat suara sintetis
- [ ] Pindah soal cepat tidak menyebabkan dua suara berbunyi bersamaan
- [ ] Fallback memilih bahasa yang benar (ID vs EN)

---

# EPIC D — P1: Monetisasi Manual (Validasi Pasar)

> **Prinsip epic ini:** buktikan orang mau membayar **sebelum** membangun backend Go 60 jam. Alur manual di bawah bisa jalan dalam hitungan hari dan menjawab satu-satunya pertanyaan yang penting: *apakah ada yang membeli?*

## D1 — Payment link Mayar.id + unlock manual

| | |
|---|---|
| **ID** | D1 |
| **Prioritas** | P1 |
| **Estimasi** | 4 jam |
| **Depends on** | E1, E2 |
| **Files** | `pricing.html` |

**Masalah**
Tidak ada jalur pembayaran sama sekali. Tombol di halaman harga tidak terhubung ke mana pun.

**Langkah**
- [ ] Buat 2 payment link statis di dashboard Mayar.id (Premium bulanan, Lifetime) — **tanpa integrasi API**
- [ ] Sambungkan tombol pricing ke link tersebut
- [ ] Setelah bayar, redirect ke `/thank-you.html` yang menjelaskan: kode akses dikirim via email dalam ≤ 24 jam
- [ ] Kirim kode unlock manual (sekali sehari cukup di fase ini)
- [ ] Implementasi gate sisi klien: kode disimpan di `localStorage`, membuka semua kategori

  > **Sadari batasannya:** gate klien bisa dibobol siapa pun yang membuka DevTools. Itu **dapat diterima** di fase ini — tujuannya mengukur *willingness to pay*, bukan mencegah pembajakan. Penegakan sungguhan datang bersama Epic H.

- [ ] Catat setiap penjualan di spreadsheet: tanggal, paket, sumber traffic, email

**Acceptance criteria**
- [ ] User bisa menyelesaikan pembayaran ujung-ke-ujung
- [ ] Kode unlock membuka konten premium
- [ ] Setiap transaksi tercatat manual
- [ ] Halaman thank-you menyebut jelas SLA 24 jam

---

## D2 — Definisikan ulang batas free tier

| | |
|---|---|
| **ID** | D2 |
| **Prioritas** | P1 |
| **Estimasi** | 3 jam |
| **Depends on** | A2 |
| **Files** | `quiz.html`, `index.html`, `pricing.html`, `notes/prd.md` |

**Masalah**
Definisi free tier sudah usang dan bertentangan antar dokumen:

| Sumber | Klaim free tier |
|---|---|
| `PRD.md` (lama) | "3 dari 10 chapter", vocabulary 10 kata |
| `pricing.html:810-826` | "5 Lesson dasar", vocabulary limit 50 kata |
| Kode | Tidak ada gating sama sekali — semua terbuka |

Tidak satu pun menyebut 11 kategori, karena semuanya ditulis sebelum kategori ada.

**Langkah**
- [ ] Tetapkan aturan baru berbasis kategori:
  - **Gratis:** kategori `general` penuh + 1 kategori pilihan user (dikunci setelah dipilih) + vocabulary 50 kata + Listening/Reading tanpa batas di kategori yang terbuka
  - **Premium:** ke-11 kategori, vocabulary penuh, Speaking tanpa batas, AI writing (saat tersedia)
- [ ] Implementasi gate di `resolveCategory()` — kategori terkunci → tampilkan paywall, bukan konten
- [ ] Selaraskan `pricing.html` dengan aturan yang sama persis
- [ ] Selaraskan `notes/prd.md` bagian 7
- [ ] Paywall harus menampilkan pratinjau (3 kalimat pertama) sebelum mengunci — konversi jauh lebih baik daripada tembok buta

**Acceptance criteria**
- [ ] Aturan free tier **identik** di kode, pricing page, dan PRD
- [ ] Kategori terkunci menampilkan paywall dengan pratinjau
- [ ] Pilihan kategori gratis persisten di `localStorage`
- [ ] `general` selalu terbuka

---

## D3 — Gerbang keputusan: lanjut ke Go atau tidak

| | |
|---|---|
| **ID** | D3 |
| **Prioritas** | P1 |
| **Estimasi** | 2 jam (analisis) |
| **Depends on** | D1, D2, F1 — **+ 30 hari data** |
| **Files** | `notes/prd.md` |

**Masalah**
Rencana asli mengalokasikan 3 minggu untuk rewrite Go **sebelum** ada bukti orang mau bayar. Task ini memasang gerbang eksplisit supaya keputusan itu diambil berdasarkan data, bukan momentum.

**Langkah**
- [ ] Jalankan D1+D2 selama 30 hari penuh
- [ ] Kumpulkan: pengunjung unik, pendaftar, pembeli, konversi, sumber traffic, retensi D7
- [ ] Evaluasi terhadap ambang di bawah:

| Hasil 30 hari | Keputusan |
|---|---|
| **≥ 20 pembeli** | Lanjut Epic H. Permintaan terbukti; backend jadi kebutuhan nyata |
| **5–19 pembeli** | Tahan. Iterasi harga/positioning/konten 30 hari lagi, ukur ulang |
| **< 5 pembeli** | Jangan bangun backend. Masalahnya di permintaan atau distribusi, bukan teknologi. Wawancarai 10 user yang tidak membeli sebelum memutuskan apa pun |

- [ ] Tulis keputusannya + alasannya di `notes/prd.md` §16 (Decision Log), bukan hanya diputuskan dalam hati

**Acceptance criteria**
- [ ] Keputusan tercatat dengan angka pendukung
- [ ] Kalau "jangan bangun", Epic H ditandai `[-]` dibatalkan, bukan dibiarkan menggantung

---

# EPIC E — P1: Konsistensi Pricing, Legal, Refund

## E1 — Perbaiki kewajiban mentoring seumur hidup pada paket Lifetime

| | |
|---|---|
| **ID** | E1 |
| **Prioritas** | P1 |
| **Estimasi** | 2 jam |
| **Depends on** | — |
| **Files** | `pricing.html`, `notes/prd.md` |

**Masalah**
**Ini masalah bisnis, bukan bug teknis, dan cukup serius.**

`pricing.html` menjual paket **Lifetime seharga Rp 399.000 sekali bayar** yang mencakup **"1-on-1 Mentoring (2x/bulan)"**. Bacalah secara harfiah: satu pembayaran Rp 399.000 memberi hak atas 24 sesi mentoring per tahun, selamanya.

Kalau satu sesi bernilai Rp 100.000 dari waktumu, satu pembeli menghabiskan nilai paketnya dalam **2 bulan** — lalu terus menagih selamanya. 100 pembeli Lifetime = 2.400 sesi mentoring per tahun, sekitar 3 sesi setiap hari kerja tanpa henti. Ini bukan produk yang bisa diskalakan; ini kewajiban tak terbatas.

Ada pula konflik dengan PRD lama: di sana mentoring hanya ada di paket **Course Bundle Rp 499.000**, sedangkan Lifetime Rp 399.000 tidak menyebut mentoring. Halaman harga dan PRD menjual dua produk berbeda dengan nama yang sama.

**Bukti**
- `pricing.html:858` → `Rp 399.000 /sekali bayar`
- `pricing.html` daftar fitur Lifetime → `1-on-1 Mentoring (2x/bulan)`
- `PRD.md:309-320` → Lifetime **tanpa** mentoring; mentoring hanya di Course Bundle

**Langkah**
- [ ] Pilih satu perbaikan (rekomendasi: opsi 1):
  1. **Batasi kuotanya** — "1-on-1 Mentoring (2x/bulan, **3 bulan pertama**)". Jelas, terbatas, tetap menarik
  2. **Pindahkan** mentoring ke Course Bundle Rp 499.000, samakan dengan PRD
  3. **Naikkan harga** Lifetime agar sepadan dengan mentoring tak terbatas — tapi tidak ada harga yang benar-benar menutup kewajiban tanpa batas
- [ ] Terapkan ke `pricing.html`, `notes/prd.md`, dan semua materi marketing serentak
- [ ] **Kalau sudah ada yang membeli dengan janji lama, hormati janji itu.** Ubah hanya untuk pembeli baru
- [ ] Tambah "Fair use" di ToS: batas rescheduling, kebijakan tidak hadir, masa berlaku kuota

**Acceptance criteria**
- [ ] Tidak ada janji layanan manusia tanpa batas di paket bayar-sekali mana pun
- [ ] Fitur paket identik antara `pricing.html` dan `notes/prd.md`
- [ ] Pembeli lama (kalau ada) tercatat dan dihormati haknya

---

## E2 — Halaman legal: ToS, Privacy, Refund

| | |
|---|---|
| **ID** | E2 |
| **Prioritas** | P1 |
| **Estimasi** | 4 jam |
| **Depends on** | — |
| **Files** | `terms.html`, `privacy.html`, `refund.html` (baru) |

**Masalah**
Payment gateway Indonesia termasuk Mayar.id umumnya mensyaratkan ToS, kebijakan privasi, dan kebijakan refund yang bisa diakses publik sebelum akun merchant disetujui. Tidak satu pun ada. **Ini akan memblokir D1**, jadi kerjakan lebih dulu.

Ada juga isu data pribadi yang nyata: modul Speaking merekam suara user. Rekaman suara adalah data pribadi. Skema database di PRD lama punya kolom `speaking_practices.audio_url` untuk menyimpannya, tanpa satu kata pun tentang retensi, persetujuan, atau penghapusan.

**Langkah**
- [ ] `terms.html` — layanan, kewajiban user, batasan tanggung jawab, klausa perubahan harga
- [ ] `privacy.html` — data yang dikumpulkan, dasar hukum, retensi, hak user, kontak. **Wajib menyebut rekaman suara secara eksplisit:**
  - Apakah audio dikirim ke server atau diproses di perangkat? (Saat ini: di perangkat, lewat Web Speech API)
  - Kalau nanti disimpan: berapa lama, untuk apa, cara menghapus
  - Sikap default yang direkomendasikan: **jangan simpan audio mentah sama sekali**. Simpan transkrip + skor saja. Ini menghilangkan seluruh kelas kewajiban hukum sekaligus
- [ ] `refund.html` — jendela refund (rekomendasi: 7 hari tanpa syarat), cara mengajukan, SLA proses
- [ ] Tautkan ketiganya dari footer semua halaman
- [ ] Sesuaikan dengan UU PDP Indonesia (UU 27/2022) — konsultasikan bila ragu

**Acceptance criteria**
- [ ] Tiga halaman ada, tertaut dari footer setiap halaman
- [ ] Kebijakan privasi menangani rekaman suara secara eksplisit
- [ ] Kebijakan refund menyebut jendela waktu dan proses yang konkret
- [ ] Akun merchant Mayar.id disetujui

---

## E3 — Selaraskan konten pricing page dengan realitas

| | |
|---|---|
| **ID** | E3 |
| **Prioritas** | P1 |
| **Estimasi** | 1 jam |
| **Depends on** | D2, E1 |
| **Files** | `pricing.html` |

**Masalah**
Halaman harga menjanjikan "50+ Lesson lengkap" dan "Certificate of completion". Sistem sertifikat belum ada. Penghitungan "lesson" tidak cocok dengan struktur kategori mana pun.

**Langkah**
- [ ] Ganti hitungan lesson dengan angka nyata: **11 kategori, 571 latihan**
- [ ] Tandai fitur yang belum ada sebagai *"Segera hadir"* — jangan jual sebagai tersedia
- [ ] Hapus "Certificate" dari daftar sampai benar-benar ada (atau tandai coming soon dengan estimasi)
- [ ] Samakan angka vocabulary dengan implementasi sebenarnya

**Acceptance criteria**
- [ ] Setiap fitur di pricing page benar-benar ada, atau bertanda "Segera hadir"
- [ ] Semua angka cocok dengan konten nyata

---

# EPIC F — P2: Analytics & Instrumentation

## F1 — Pasang analytics dasar

| | |
|---|---|
| **ID** | F1 |
| **Prioritas** | P2 |
| **Estimasi** | 3 jam |
| **Depends on** | B1 |
| **Files** | semua HTML |

**Masalah**
PRD lama menargetkan retensi D7, NPS, dan konversi — tanpa satu pun alat untuk mengukurnya. Target yang tidak terukur bukan target.

**Langkah**
- [ ] Pasang analytics yang ramah privasi (Plausible / Umami self-hosted — hindari GA4, cookie banner-nya menambah beban legal)
- [ ] Lacak event yang benar-benar menjawab pertanyaan bisnis:

  | Event | Properti | Menjawab |
  |---|---|---|
  | `category_selected` | slug | Kategori mana yang diminati? |
  | `lesson_started` | slug, mode | Mode mana yang dipakai? |
  | `lesson_completed` | slug, mode, skor | Apakah orang menyelesaikan? |
  | `paywall_viewed` | slug | Di mana orang membentur batas? |
  | `checkout_clicked` | paket | Berapa yang berniat bayar? |
  | `purchase_completed` | paket, nominal | Berapa yang benar-benar bayar? |
  | `audio_fallback_used` | num_id | File audio mana yang bermasalah? |

- [ ] Buat dashboard funnel: kunjungan → pilih kategori → mulai → selesai → paywall → checkout → beli
- [ ] Tambahkan `<noscript>` pixel supaya pemblokir JS tetap terhitung kasar

**Acceptance criteria**
- [ ] Semua 7 event terkirim dan terlihat di dashboard
- [ ] Funnel bisa dibaca ujung-ke-ujung
- [ ] Tidak ada PII yang terkirim ke analytics

---

## F2 — Error tracking

| | |
|---|---|
| **ID** | F2 |
| **Prioritas** | P2 |
| **Estimasi** | 2 jam |
| **Depends on** | F1 |

**Masalah**
Tidak ada visibilitas atas error di sisi klien. Bug A2 (kategori tidak tersambung) bisa hidup berbulan-bulan tanpa terdeteksi justru karena gagalnya diam-diam.

**Langkah**
- [ ] Pasang Sentry (tier gratis) atau `window.onerror` handler sederhana yang mengirim ke endpoint sendiri
- [ ] Lacak: JS error, audio 404, kegagalan fetch konten, error izin mikrofon
- [ ] Pasang alert untuk lonjakan error rate

**Acceptance criteria**
- [ ] JS error muncul di dashboard dengan stack trace
- [ ] Audio 404 terlacak per `num_id`

---

## F3 — Kumpulkan feedback kualitatif

| | |
|---|---|
| **ID** | F3 |
| **Prioritas** | P2 |
| **Estimasi** | 1 jam |
| **Depends on** | — |

**Langkah**
- [ ] Pasang widget feedback satu klik (👍/👎 + komentar opsional) di akhir setiap lesson
- [ ] Survei NPS setelah lesson ke-5 (bukan lesson pertama — terlalu dini)
- [ ] Kanal kontak yang terlihat jelas (WhatsApp/email) di footer

**Acceptance criteria**
- [ ] Feedback tersimpan dan bisa dibaca
- [ ] NPS punya jalur pengumpulan nyata, bukan sekadar angka di PRD

---

# EPIC G — P2: Higiene Repo & Dokumentasi

## G1 — Perbaiki `generate_content.py`

| | |
|---|---|
| **ID** | G1 |
| **Prioritas** | P2 |
| **Estimasi** | 2 jam |
| **Files** | `generate_content.py` |

**Masalah**
Script menulis ke `/tmp/english-learning/content` — di luar repo, dan hilang saat reboot. Konten yang ada di `content/` jelas disalin manual sekali, artinya script dan repo bisa (dan akan) berbeda diam-diam.

Script ini juga 93 KB berisi konten inline, bukan generator sungguhan — ia hanya cetakan data yang di-hardcode.

**Bukti**
`generate_content.py:6` → `OUTPUT_DIR = "/tmp/english-learning/content"`

**Langkah**
- [ ] Ganti `OUTPUT_DIR` jadi relatif: `Path(__file__).parent / "content"`
- [ ] Tambah `--dry-run` agar bisa membandingkan tanpa menimpa
- [ ] Tambah pengecekan: peringatkan kalau file target sudah ada dan berbeda
- [ ] Pertimbangkan memisahkan data konten ke file YAML/JSON terpisah, agar script tinggal jadi transformer tipis

**Acceptance criteria**
- [ ] Script menulis ke `content/` di dalam repo
- [ ] `--dry-run` melaporkan perbedaan tanpa menulis
- [ ] Menjalankan script pada repo bersih menghasilkan nol perubahan git

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
python3 generate_content.py --dry-run
git status --porcelain content/   # harus kosong
```

---

## G2 — Buat `CLAUDE.md`

| | |
|---|---|
| **ID** | G2 |
| **Prioritas** | P2 |
| **Estimasi** | 1 jam |
| **Files** | `CLAUDE.md` (baru) |

**Langkah**
- [ ] Dokumentasikan: layout repo, alur build/deploy, aturan slug kanonik (A1), pipeline audio, dan hal-hal yang mudah menjebak
- [ ] Sebutkan eksplisit: "`content/*.json` adalah sumber kebenaran konten; `scripts.json` peninggalan lama yang setara `content/software-engineering.json`"
- [ ] Catat: kartu kategori harus dirender dari manifest, jangan pernah di-hardcode (pelajaran dari A3/A6)

**Acceptance criteria**
- [ ] `CLAUDE.md` ada dan menjelaskan aturan slug + pipeline audio

---

## G3 — Keputusan penyimpanan aset audio

| | |
|---|---|
| **ID** | G3 |
| **Prioritas** | P2 |
| **Estimasi** | 2 jam |
| **Depends on** | C2 |

**Masalah**
Setelah C2, repo memuat ~1.142 file MP3 (~34 MB). Binary di git memperlambat clone dan tidak pernah bisa dihapus dari histori.

**Langkah**
- [ ] Pilih:
  1. **Biarkan di git** — paling sederhana, 34 MB masih bisa ditoleransi
  2. **Git LFS** — repo tetap ramping, tapi menambah langkah setup
  3. **Cloudflare R2** — audio keluar dari repo sepenuhnya, disajikan dari CDN, gratis pada volume ini. Terbaik kalau audio akan terus bertambah
- [ ] Kalau pilih R2: update `playAudio` agar memakai base URL yang bisa dikonfigurasi
- [ ] Dokumentasikan keputusannya di `CLAUDE.md`

**Acceptance criteria**
- [ ] Keputusan diambil dan didokumentasikan
- [ ] `git clone` selesai dalam waktu yang wajar

---

## G4 — Pensiunkan `PRD.md` lama & `scripts.json`

| | |
|---|---|
| **ID** | G4 |
| **Prioritas** | P2 |
| **Estimasi** | 1 jam |
| **Depends on** | A2, B2 |

**Masalah**
`PRD.md` di root sudah digantikan `notes/prd.md`. Dua PRD yang berbeda isi akan selalu berakhir dengan orang membaca yang salah.

`scripts.json` (120 item) duplikat dari `content/software-engineering.json` (120 item). Dua sumber kebenaran untuk data yang sama.

**Langkah**
- [ ] Hapus `PRD.md` root **setelah** memastikan `notes/prd.md` mencakup semuanya (konfirmasi dulu ke pemilik repo sebelum menghapus)
- [ ] Verifikasi `scripts.json` == `content/software-engineering.json` secara isi
- [ ] Setelah A2 selesai, hapus `scripts.json` dan semua referensinya
- [ ] Simpan redirect/catatan di `CLAUDE.md` untuk yang mencari file lama

**Acceptance criteria**
- [ ] Hanya ada satu PRD di repo
- [ ] Hanya ada satu sumber konten software engineering
- [ ] Tidak ada kode yang masih mereferensi `scripts.json`

**Verifikasi**
```bash
cd /home/cecep/Projects/english-learning
python3 -c "
import json
a=json.load(open('scripts.json'))['scripts']
b=json.load(open('content/software-engineering.json'))['scripts']
print('identik' if a==b else f'BEDA: {len(a)} vs {len(b)} item')
"
grep -rn "scripts.json" --include="*.html" . | grep -v notes/
```

---

# EPIC H — P3: Backend Go (GATED oleh D3)

> ⚠️ **Jangan mulai epic ini sebelum D3 memberi lampu hijau.** Sekitar 60 jam kerja tanpa validasi permintaan adalah risiko terbesar dalam rencana ini.

Ringkasan task (rincian menyusul saat gerbang terbuka):

| ID | Task | Est. |
|---|---|---|
| H1 | Scaffold proyek Go, konfigurasi, Docker Compose | 6 j |
| H2 | Skema DB + migrasi (lihat PRD §11 — perhatikan perbaikan skemanya) | 6 j |
| H3 | Auth: register/login/refresh, hashing argon2id, tabel `refresh_tokens` | 12 j |
| H4 | Sajikan konten dari Go, pertahankan URL kategori yang sudah ada | 8 j |
| H5 | API progress + strategi resolusi konflik (lihat PRD §11.4) | 10 j |
| H6 | Migrasi progress `localStorage` → akun server | 6 j |
| H7 | Rate limiting berbasis Redis | 4 j |
| H8 | Testing + observability | 8 j |

**Prasyarat sebelum H1:**
- [ ] D3 memutuskan "lanjut"
- [ ] Strategi resolusi konflik progress ditulis dan disetujui — **tanpa ini, H5 akan menghasilkan kehilangan data**
- [ ] Rencana migrasi user existing selesai (H6 harus dirancang bersama H3, bukan setelahnya)

---

# EPIC I — P3: Otomasi Pembayaran Mayar.id (GATED oleh H)

| ID | Task | Est. |
|---|---|---|
| I1 | Pembuatan invoice via API | 6 j |
| I2 | Handler webhook **dengan idempotensi** — lihat PRD §11.5 | 8 j |
| I3 | Lifecycle langganan (aktivasi, kedaluwarsa, pembatalan) | 6 j |
| I4 | Alur refund | 4 j |

**Dua hal yang wajib diperbaiki dari desain lama (detail di PRD §11.5):**
1. Jangan pernah percaya `user_id` dari body webhook — resolusi harus lewat `mayar_invoice_id` ke record `payments` sendiri
2. Webhook **harus** idempoten — Mayar melakukan retry; tanpa penjagaan, premium teraktivasi berkali-kali

---

# EPIC J — P4: AI Writing & Speaking Feedback (GATED oleh I)

| ID | Task | Est. |
|---|---|---|
| J1 | Layer proxy AI + akuntansi token | 8 j |
| J2 | Modul writing + rubrik penilaian | 10 j |
| J3 | Feedback speaking berbasis AI | 8 j |
| J4 | Kontrol biaya, budget cap, degradasi anggun | 6 j |

**Catatan model (per Agustus 2026):** rencana lama menyebut `claude-3-haiku`, yang sudah lawas. Gunakan **Claude Haiku 4.5** (`claude-haiku-4-5-20251001`). Jangan bangun model biaya di atas model "gratis" OpenRouter — tier gratis bisa dibatasi atau dihapus tanpa pemberitahuan, dan seluruh proyeksi biaya ikut runtuh.

---

# EPIC K — P4: Growth

| ID | Task | Est. |
|---|---|---|
| K1 | PWA: manifest, service worker, offline | 10 j |
| K2 | Landing page per kategori (11 halaman SEO) | 12 j |
| K3 | Sitemap.xml, robots.txt, structured data | 4 j |
| K4 | Perluasan konten blog | 8 j |
| K5 | Leaderboard & fitur sosial | 6 j |

---

# Lampiran

## A. Peta File

| Path | Peran | Ukuran | Catatan |
|---|---|---|---|
| `landing.html` | Halaman marketing | 45 KB | Kartu kategori hardcode (A6) |
| `index.html` | Aplikasi belajar | 43 KB | Fetch hardcode (A2) |
| `quiz.html` | Mesin kuis + speaking | 145 KB | Berisi ribuan baris JS inline |
| `pricing.html` | Halaman harga | 41 KB | Konflik dengan PRD (E1, E3) |
| `admin.html` | Admin panel | 74 KB | Tanpa auth (B3) |
| `blog/` | 3 artikel + index | — | Tidak ter-deploy sebelum B1 |
| `content/*.json` | 11 kategori, 571 item | — | Sumber kebenaran konten |
| `scripts.json` | Software engineering lama | 28 KB | Duplikat (G4) |
| `audio/` | 240 MP3 | 7,2 MB | Butuh 902 lagi (C2) |
| `generate_audio.py` | Generator TTS | 2,5 KB | Path rusak (C1) |
| `generate_content.py` | Generator konten | 93 KB | Menulis ke `/tmp` (G1) |
| `nginx.conf` | Config web server | 2,2 KB | Tanpa route eksplisit (A4) |
| `Dockerfile` | Definisi image | 301 B | Kehilangan mayoritas file (B1) |

## B. Skrip Audit Cepat

Simpan sebagai `notes/audit.sh` dan jalankan sebelum setiap deploy:

```bash
#!/usr/bin/env bash
# Audit kesehatan repo — jalankan dari root proyek
cd "$(dirname "$0")/.." || exit 1
echo "=== 1. Konsistensi slug ==="
python3 - <<'EOF'
import json, glob, os
man = {c['id'] for c in json.load(open('content/categories.json'))['categories']}
files = {}
for f in glob.glob('content/*.json'):
    b = os.path.basename(f)[:-5]
    if b in ('categories', 'all-categories'): continue
    files[b] = json.load(open(f))['id']
bad = [f'{k}!={v}' for k, v in files.items() if k != v]
print('  file vs id :', 'OK' if not bad else bad)
print('  manifest   :', 'OK' if man == set(files) else man ^ set(files))
EOF

echo "=== 2. Link landing page ==="
python3 - <<'EOF'
import json, re
canon = {c['id'] for c in json.load(open('content/categories.json'))['categories']}
found = set(re.findall(r'/app\?category=([a-z-]+)', open('landing.html').read()))
print('  link rusak :', found - canon or 'OK')
print('  jumlah     :', f'{len(found)}/11')
EOF

echo "=== 3. Cakupan audio ==="
python3 - <<'EOF'
import json, glob, os
miss = 0
for f in glob.glob('content/*.json'):
    if os.path.basename(f) in ('categories.json', 'all-categories.json'): continue
    for s in json.load(open(f))['scripts']:
        miss += sum(not os.path.exists(f"audio/{s['num_id']}{sfx}.mp3") for sfx in ('', '_id'))
print('  file hilang:', miss)
EOF

echo "=== 4. Kelengkapan Docker ==="
for f in quiz.html landing.html pricing.html content blog; do
  grep -q "$f" Dockerfile || grep -qE '^COPY \. ' Dockerfile \
    && echo "  $f: OK" || echo "  $f: HILANG dari image"
done

echo "=== 5. Konsistensi domain ==="
echo "  ypc.my.id tersisa: $(grep -r 'ypc\.my\.id' --exclude-dir=.git --exclude-dir=notes . 2>/dev/null | wc -l)"
```

## C. Konvensi Commit

```
<tipe>(<task-id>): <ringkasan>

fix(A2):  sambungkan router kategori ke content/*.json
feat(D1): payment link Mayar + unlock manual
docs(G2): tambah CLAUDE.md dengan aturan slug
chore(B1): kirim semua halaman ke image Docker
```

## D. Ringkasan Temuan Audit

| # | Temuan | Bukti | Task |
|---|---|---|---|
| 1 | 11 kategori tidak tersambung ke aplikasi | `index.html:558`, nol `URLSearchParams` | A2 |
| 2 | 5 slug landing tidak ada di sistem mana pun | `landing.html:906-936` | A3 |
| 3 | Tiga skema penamaan yang saling bentrok | `categories.json` vs nama file vs `id` | A1 |
| 4 | Dockerfile kehilangan sebagian besar aplikasi | `Dockerfile` — hanya 3 COPY | B1 |
| 5 | 902 file audio hilang | 240 ada, 1.142 dibutuhkan | C2 |
| 6 | Kegagalan audio hanya jadi toast | `quiz.html:2517` | A5, C3 |
| 7 | Lifetime Rp399k janji mentoring selamanya | `pricing.html:858` | E1 |
| 8 | Free tier bertentangan di 3 tempat | PRD vs pricing vs kode | D2 |
| 9 | Admin panel tanpa autentikasi | `admin.html` | B3 |
| 10 | Domain tidak konsisten | 15 vs 4 referensi | B2 |
| 11 | Path generator rusak | `generate_audio.py:12-13` | C1 |
| 12 | Generator konten menulis ke `/tmp` | `generate_content.py:6` | G1 |
| 13 | Nol analytics untuk KPI yang ditargetkan | tidak ada tracking | F1 |
| 14 | Tidak ada halaman legal (blocker Mayar) | tidak ada file | E2 |
| 15 | Fallback nginx menyembunyikan 404 | `nginx.conf` | A4 |

---

*Disusun berdasarkan audit kode pada commit `46b960b`, 3 Agustus 2026.*
*Setiap klaim dalam dokumen ini bisa diverifikasi lewat perintah yang disertakan.*
