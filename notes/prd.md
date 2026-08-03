# PRD: English for Remote Worker

**Domain:** english.tool.biz.id
**Author:** Cecep Saeful Azhar Hidayat, ST — FathForce Academy
**Versi:** 2.0
**Tanggal:** 3 Agustus 2026
**Menggantikan:** `PRD.md` v1.0 (Juli 2026)
**Dokumen terkait:** [`notes/task.md`](./task.md) — backlog implementasi

---

## Changelog v1.0 → v2.0

Versi ini ditulis ulang setelah audit kode pada commit `46b960b`. Perubahan utama:

| # | Perubahan | Alasan |
|---|---|---|
| 1 | Status produk ditulis ulang sesuai hasil audit | v1.0 mengklaim fitur yang belum tersambung di kode |
| 2 | Domain diseragamkan ke `english.tool.biz.id` | v1.0 masih memakai `english.ypc.my.id` |
| 3 | Roadmap dibalik: monetisasi **sebelum** rewrite Go | Rewrite 60 jam tanpa validasi permintaan adalah risiko terbesar |
| 4 | Semua statistik pasar ditandai eksplisit sebagai asumsi | v1.0 menyajikannya sebagai fakta tanpa sumber |
| 5 | Target KPI diturunkan ke angka yang bisa dipertanggungjawabkan | D7 50% dan LTV:CAC 30:1 tidak realistis |
| 6 | Ditambah: user story + acceptance criteria | v1.0 hanya punya daftar fitur, tidak bisa di-review |
| 7 | Ditambah: risk register, rencana analytics, bagian legal | Tidak ada di v1.0 sama sekali |
| 8 | Skema database diperbaiki: idempotensi, satu sumber kebenaran, kategori | v1.0 punya lubang keamanan webhook dan tiga sumber status langganan |
| 9 | Model AI dan biaya dikoreksi | v1.0 memakai model usang dan angka biaya yang terlalu rendah ~4× |
| 10 | Perbandingan Go vs React ditulis ulang jujur | Klaim "~0 KB JS" tidak benar untuk produk ini |
| 11 | Paket Lifetime diperbaiki | v1.0 vs pricing page menjual dua produk berbeda dengan nama sama |
| 12 | Ditambah: Decision Log | Supaya keputusan besar punya jejak dan alasan |

---

## Daftar Isi

1. [Ringkasan Eksekutif](#1-ringkasan-eksekutif)
2. [Status Nyata Produk](#2-status-nyata-produk)
3. [Masalah & Target Pasar](#3-masalah--target-pasar)
4. [Positioning & Kompetitor](#4-positioning--kompetitor)
5. [Prinsip Produk](#5-prinsip-produk)
6. [User Story & Acceptance Criteria](#6-user-story--acceptance-criteria)
7. [Arsitektur](#7-arsitektur)
8. [Roadmap](#8-roadmap)
9. [Monetisasi](#9-monetisasi)
10. [Strategi SEO](#10-strategi-seo)
11. [Integrasi AI](#11-integrasi-ai)
12. [Skema Database](#12-skema-database)
13. [Analytics & Instrumentation](#13-analytics--instrumentation)
14. [Legal, Privasi, dan Data](#14-legal-privasi-dan-data)
15. [Risk Register](#15-risk-register)
16. [Success Metrics](#16-success-metrics)
17. [Open Questions](#17-open-questions)
18. [Decision Log](#18-decision-log)

---

## 1. Ringkasan Eksekutif

### Apa

Platform belajar bahasa Inggris untuk pekerja remote Indonesia, dengan konten spesifik per profesi — bukan bahasa Inggris generik.

### Untuk Siapa

Profesional Indonesia usia 22–35 yang ingin bekerja remote untuk perusahaan luar negeri, dan terhambat oleh kemampuan bahasa Inggris. Awalnya ditargetkan untuk developer; sekarang mencakup 11 profesi (lihat §3).

### Bagaimana

Empat skill inti, dilatih dengan skenario kerja nyata:

| Skill | Mekanisme | Status |
|---|---|---|
| 🎧 Listening | Audio TTS + kuis pemahaman | ⚠️ Jalan di 1 dari 11 kategori |
| 📖 Reading | Kuis pemahaman berbasis konteks | ✅ Jalan |
| 🎤 Speaking | Web Speech API + skor kemiripan | ✅ Jalan (Chrome/Android) |
| ✍️ Writing | Penilaian AI | ❌ Belum ada |

### Keunggulan

- **Konten per profesi** — copywriter belajar bahasa Inggris copywriting, bukan "at the airport"
- **Skenario kerja nyata** — interview, standup, client call, negosiasi
- **UI Indonesia, konten Inggris** — menurunkan hambatan masuk
- **Harga terjangkau** — Rp 99.000/bulan vs Rp 2–5 juta/bulan kursus konvensional

### Keadaan Saat Ini, Tanpa Bumbu

Konten untuk 11 kategori sudah ditulis (571 latihan). Aplikasi belajarnya **belum bisa menyajikan kategori mana pun kecuali satu**. Landing page menjual 11; kode mengirim 1. Prioritas nomor satu adalah menutup jarak itu — bukan menambah fitur.

---

## 2. Status Nyata Produk

> Bagian ini adalah hasil audit kode, bukan aspirasi. Setiap baris bisa diverifikasi lewat perintah di [`notes/task.md`](./task.md) Lampiran B.

### Yang Benar-Benar Jalan

| Kemampuan | Bukti |
|---|---|
| Kuis listening, reading, vocabulary, fill-in-blank | `quiz.html` — jalan penuh untuk kategori `software-engineering` |
| Modul speaking (Web Speech API, skor, free talk 30 detik, simulator percakapan) | `quiz.html` — jalan di browser yang mendukung `SpeechRecognition` |
| Progress tracking lokal (XP, streak, level) | `localStorage`: `quiz_progress`, `quiz_leaderboard` |
| Audio TTS dua bahasa untuk 120 latihan | 240 file di `audio/` |
| Landing page, halaman harga, 3 artikel blog | `landing.html`, `pricing.html`, `blog/` |
| Admin panel (konten + pengaturan) | `admin.html` — tanpa autentikasi |

### Yang Ada Tapi Belum Tersambung

| Aset | Masalah |
|---|---|
| Konten 11 kategori (571 latihan) | Aplikasi hanya fetch `scripts.json`; parameter `?category=` diabaikan total |
| 11 kartu kategori di landing page | 5 dari 11 slug tidak ada di sistem mana pun |
| Halaman quiz, pricing, admin, blog | Tidak disalin ke image Docker — tidak sampai production |

### Yang Belum Ada Sama Sekali

Akun user · sinkronisasi lintas perangkat · pembayaran · gating premium · modul writing · sertifikat · analytics · halaman legal · backend

### Inventaris Konten

| Kategori | Slug | Latihan | Audio |
|---|---|---:|:---:|
| General English | `general` | 46 | ❌ |
| Business English | `business` | 45 | ❌ |
| Finance English | `finance` | 45 | ❌ |
| Administration | `admin` | 45 | ❌ |
| Web Design | `web-design` | 45 | ❌ |
| SEO Specialist | `seo` | 45 | ❌ |
| Graphic Design | `graphic-design` | 45 | ❌ |
| Video Editing | `video-editing` | 45 | ❌ |
| Virtual Assistant | `virtual-assistant` | 45 | ❌ |
| Copywriting | `copywriting` | 45 | ❌ |
| Software Engineering | `software-engineering` | 120 | ✅ |
| **Total** | | **571** | **1 dari 11** |

**Cakupan audio: 240 dari 1.142 file yang dibutuhkan (21%).**

---

## 3. Masalah & Target Pasar

### Pernyataan Masalah

> Profesional Indonesia yang secara teknis mampu bekerja remote untuk perusahaan luar negeri sering gagal di tahap interview dan komunikasi harian berbahasa Inggris. Bahan belajar yang tersedia bersifat generik — mengajarkan bahasa Inggris untuk turis, bukan untuk standup meeting, code review, atau negosiasi dengan klien.

### Persona Utama

```
Usia            : 22–35
Pekerjaan       : Developer, designer, copywriter, VA, video editor, SEO
Penghasilan     : Rp 5–15 juta/bulan (pasar lokal)
Target          : Pekerjaan remote $1.000–3.000/bulan
Hambatan        : Tidak percaya diri berbahasa Inggris di konteks profesional
Perangkat       : Mobile-first, mayoritas Android
Waktu belajar   : 10–20 menit/hari, tidak teratur
```

### ⚠️ Asumsi Pasar — Belum Tervalidasi

Angka di bawah ini **adalah asumsi kerja, bukan fakta terverifikasi.** v1.0 menyajikannya sebagai data; itu keliru. Semuanya harus divalidasi sebelum dijadikan dasar keputusan besar.

| Asumsi | Nilai kerja | Cara memvalidasi |
|---|---|---|
| Profesional Indonesia yang mengincar kerja remote | ~150.000 | Data LinkedIn Indonesia, ukuran komunitas remote-work, survei industri |
| Persentase yang gagal di tahap bahasa Inggris | Tinggi (kualitatif) | Wawancari 20 orang; tanyakan pengalaman interview mereka |
| Kesediaan membayar Rp 99.000/bulan | Belum diketahui | **Epic D di `task.md` menjawab ini secara langsung** |
| Tidak ada kompetitor yang fokus "Inggris + konteks profesi" | Belum diketahui | Riset kompetitor selama 2 jam sebelum menaikkan skala marketing |

**Aturan yang mengikat:** jangan pernah mengutip angka ini ke investor, mitra, atau materi marketing sebelum divalidasi. Kalau harus menyebut ukuran pasar, sebutkan sebagai estimasi beserta metodenya.

### Ukuran Pasar (Perhitungan Ilustratif)

```
150.000 target             × 5% bisa dijangkau tahun pertama =  7.500 pengunjung
  7.500 pengunjung         × 20% mendaftar                   =  1.500 pendaftar
  1.500 pendaftar          × 1–3% konversi berbayar          =  15–45 pembeli/tahun
```

Ini **skenario, bukan proyeksi.** Yang mengubahnya dari skenario jadi angka nyata adalah data 30 hari dari Epic D.

---

## 4. Positioning & Kompetitor

### Pernyataan Positioning

> Untuk profesional Indonesia yang mengejar pekerjaan remote internasional, English for Remote Worker adalah platform latihan bahasa Inggris yang mengajarkan bahasa spesifik profesi mereka — bukan bahasa Inggris umum — sehingga mereka bisa berlatih persis kalimat yang akan dipakai di interview dan pekerjaan harian.

### Lanskap Kompetitif

| Kompetitor | Kekuatan | Celah yang kita isi |
|---|---|---|
| Duolingo | Gratis, gamifikasi kuat, retensi tinggi | Bahasa Inggris umum; tidak ada konteks profesional |
| Cakap / Bahaso | Lokal, ada guru manusia | Mahal; berbasis jadwal; belum spesifik profesi |
| English First | Merek kuat, kelas offline | Rp 2–5jt/bulan; terikat lokasi |
| Coursera / Udemy | Konten mendalam | Pasif; hampir tidak ada latihan speaking |
| YouTube | Gratis, melimpah | Tanpa struktur, tanpa umpan balik, tanpa progres |

### Kejujuran soal Keunggulan

Yang benar-benar sulit ditiru: **konten per profesi + speaking + harga terjangkau + UI Indonesia** sekaligus. Masing-masing komponen mudah ditiru sendirian. Keunggulan sesungguhnya lahir dari eksekusi dan kedekatan dengan komunitas — bukan dari teknologi.

---

## 5. Prinsip Produk

Prinsip ini menyelesaikan perdebatan sebelum terjadi. Kalau sebuah keputusan melanggarnya, keputusan itu butuh alasan tertulis di Decision Log.

1. **Jangan jual yang belum jalan.** Fitur di landing page dan halaman harga harus benar-benar berfungsi, atau bertanda "Segera hadir".
2. **Gagal dengan berisik, bukan diam-diam.** Bug kategori bisa hidup berbulan-bulan justru karena gagalnya senyap. Error harus terlihat.
3. **Validasi sebelum bangun.** Pekerjaan besar butuh bukti permintaan lebih dulu. Kode adalah bagian termahal, bukan termurah.
4. **Satu sumber kebenaran.** Setiap data — slug kategori, status langganan, definisi free tier — hidup di satu tempat.
5. **Sederhana dulu, otomatis belakangan.** Pembayaran manual yang jalan minggu ini mengalahkan pembayaran otomatis yang jalan dua bulan lagi.
6. **Mobile-first, sungguhan.** Mayoritas pengguna memakai Android kelas menengah dengan koneksi tidak stabil. Setiap keputusan performa diukur di sana.

---

## 6. User Story & Acceptance Criteria

> v1.0 hanya berisi daftar fitur bercentang, yang tidak bisa di-review. Bagian ini menetapkan definisi "selesai" per fitur.

### 6.1 Memilih Kategori

> Sebagai pekerja remote, saya ingin memilih kategori profesi saya, supaya yang saya pelajari relevan dengan pekerjaan nyata saya.

**Acceptance criteria**
- [ ] Landing page menampilkan 11 kategori dengan nama, ikon, deskripsi
- [ ] Klik kategori membuka aplikasi belajar **dengan konten kategori itu**
- [ ] Kategori aktif terlihat jelas di dalam aplikasi
- [ ] Pindah halaman di dalam app tidak mereset kategori
- [ ] Slug tidak valid → fallback + pesan yang bisa dibaca (bukan gagal diam-diam)
- [ ] Tanpa parameter → default `software-engineering`
- [ ] Kategori tanpa audio menampilkan badge "Audio segera hadir"

### 6.2 Latihan Listening

> Sebagai pembelajar, saya ingin mendengar bahasa Inggris profesional dan menguji pemahaman saya, supaya saya bisa mengikuti meeting berbahasa Inggris.

**Acceptance criteria**
- [ ] Setiap latihan punya audio Inggris dan Indonesia
- [ ] Tombol putar menampilkan status (playing/idle)
- [ ] Kalau audio gagal, `speechSynthesis` mengambil alih — soal tetap bisa dikerjakan
- [ ] Skor kuis tersimpan ke progres
- [ ] Mode Listening disembunyikan (bukan rusak) untuk kategori tanpa audio

### 6.3 Latihan Speaking

> Sebagai pembelajar, saya ingin mengucapkan kalimat dan mendapat skor, supaya saya percaya diri berbicara.

**Acceptance criteria**
- [ ] Izin mikrofon diminta dengan penjelasan sebelum prompt browser
- [ ] Skor kemiripan kata per kata ditampilkan
- [ ] Free talk 30 detik berfungsi
- [ ] **Browser tanpa `SpeechRecognition` (Safari iOS) menampilkan pesan jelas + alternatif**, bukan tombol yang tidak berfungsi
- [ ] Audio diproses di perangkat; tidak ada yang dikirim ke server (lihat §14)

### 6.4 Progres Belajar

> Sebagai pembelajar, saya ingin melihat kemajuan saya, supaya saya termotivasi kembali besok.

**Acceptance criteria**
- [ ] XP, streak, dan level terlihat di layar utama
- [ ] Progres dipisahkan **per kategori** — belajar copywriting tidak menaikkan progres SEO
- [ ] Progres bertahan setelah browser ditutup
- [ ] Streak putus setelah melewatkan satu hari penuh, bukan satu sesi

### 6.5 Berlangganan Premium

> Sebagai pembelajar serius, saya ingin membeli akses penuh, supaya saya bisa mengakses semua kategori.

**Acceptance criteria**
- [ ] Halaman harga menampilkan fitur yang benar-benar ada
- [ ] Pembayaran bisa diselesaikan ujung-ke-ujung
- [ ] Setelah bayar, user tahu persis kapan akses aktif (SLA tertulis)
- [ ] Konten terkunci menampilkan **pratinjau** sebelum paywall
- [ ] Kebijakan refund bisa diakses sebelum membayar

### 6.6 Sinkronisasi Progres *(Epic H — gated)*

> Sebagai pembelajar yang punya HP dan laptop, saya ingin progres saya sama di keduanya.

**Acceptance criteria**
- [ ] Daftar/masuk berfungsi
- [ ] Progres `localStorage` yang sudah ada **dimigrasikan** ke akun pada login pertama, tidak hilang
- [ ] **Aturan konflik ditulis dan diterapkan** — lihat §7.4. Tanpa ini, fitur ini menghilangkan data user
- [ ] Berfungsi offline; sinkron saat koneksi kembali

---

## 7. Arsitektur

### 7.1 Saat Ini — Statis

```
Cloudflare Tunnel → Nginx (Docker) → HTML/CSS/JS statis
                                      ├── content/*.json   (11 kategori, 571 latihan)
                                      ├── audio/*.mp3      (240 file)
                                      └── localStorage     (progres, per-perangkat)
```

**Kelebihan:** nol biaya server, nol operasional, cepat, tidak bisa "down" selain nginx-nya.
**Kekurangan:** tidak ada akun, tidak ada sinkronisasi, tidak ada gating yang bisa ditegakkan, tidak ada analytics sisi server.

### 7.2 Target — Fullstack Go *(hanya kalau D3 lolos)*

```
┌────────────────────────────────────────────────┐
│ KLIEN                                          │
│ HTML + HTMX + JS (speech, audio, timer, kuis)  │
└─────────────────┬──────────────────────────────┘
                  │ HTTP / HX-Request
┌─────────────────▼──────────────────────────────┐
│ GO SERVER (Echo)                               │
│  Handler · Middleware (auth, rate limit)       │
│  Template (html/template) · Proxy AI           │
├────────────────────────────────────────────────┤
│ SERVICE                                        │
│  Auth · Progress · Payment · AI · Content      │
├────────────────────────────────────────────────┤
│ DATA                                           │
│  PostgreSQL (user, progres, pembayaran)        │
│  Redis (sesi, rate limit, counter)             │
├────────────────────────────────────────────────┤
│ EKSTERNAL                                      │
│  Mayar.id · OpenRouter/Anthropic · Cloudflare  │
└────────────────────────────────────────────────┘
```

### 7.3 Kenapa Go + HTMX — Penilaian Jujur

> v1.0 mengklaim "~0 KB JS" untuk Go+HTMX dibanding "200+ KB" untuk React. **Itu tidak benar untuk produk ini.** `quiz.html` saja 145 KB, berisi ribuan baris JS untuk Web Speech API, playback audio, timer, dan scoring. Produk ini secara inheren JS-heavy di sisi klien.

Framing yang sebenarnya:

| Faktor | Go + HTMX | Next.js | Catatan jujur |
|---|---|---|---|
| JS yang tetap dibutuhkan | ~50–100 KB | ~200 KB | Speech/audio/timer wajib JS di kedua opsi |
| SEO | Server-render langsung | Butuh setup SSR | Keunggulan nyata untuk halaman kategori |
| Memori server | ~10–20 MB | ~100+ MB | Nyata; penting untuk VPS kecil |
| Waktu build | Detik | Puluhan detik | Nyata |
| Kurva belajar penulis | Rendah (sudah Go) | Lebih tinggi | **Ini alasan yang paling menentukan** |
| Ekosistem | Lebih kecil | Jauh lebih besar | Kekurangan nyata Go |

**Keputusan:** Go + HTMX, karena penulisnya sudah produktif di Go dan produk ini punya tim satu orang. Tapi keputusan ini diambil karena **kecocokan tim**, bukan karena keunggulan teknis mutlak. Klaim "0 KB JS" ditarik.

### 7.4 Resolusi Konflik Progres *(harus diputuskan sebelum H5 dimulai)*

Ketika progres lokal dan progres server berbeda, sistem harus punya aturan. Tanpa ini, sinkronisasi akan menghapus pekerjaan user.

**Aturan yang diusulkan — merge per-field, bukan last-write-wins:**

| Field | Aturan | Alasan |
|---|---|---|
| `best_score` | Ambil nilai tertinggi | Nilai terbaik tidak boleh turun karena sinkronisasi |
| `total_attempts` | Jumlahkan keduanya | Percobaan di dua perangkat sama-sama nyata |
| `completed` | Benar kalau salah satu benar | Sudah selesai tetap selesai |
| `total_xp` | Ambil tertinggi, **jangan dijumlah** | Penjumlahan bisa dieksploitasi dengan reset localStorage |
| `streak_count` | Hitung ulang dari `last_practiced_at` | Satu-satunya nilai yang tidak ambigu |
| `last_practiced_at` | Ambil yang paling baru | — |

**Last-write-wins ditolak secara eksplisit** — user yang belajar offline di HP lalu membuka laptop akan kehilangan sesi HP-nya.

---

## 8. Roadmap

### Prinsip Urutan

v1.0 menempatkan rewrite Go (~60 jam) di Fase 3 dan monetisasi di Fase 4 — artinya pekerjaan paling mahal dikerjakan sebelum ada bukti orang mau bayar. **Urutan itu dibalik.**

```
Fase 0  Perbaiki janji yang belum terpenuhi   ← SEKARANG
Fase 1  Validasi kemauan membayar (manual)
        ══════ GERBANG KEPUTUSAN ══════
Fase 2  Backend Go (hanya kalau gerbang lolos)
Fase 3  Otomasi pembayaran + AI
Fase 4  Growth
```

### Fase 0 — Perbaiki Janji yang Belum Terpenuhi · P0

**Tujuan:** produk melakukan apa yang sudah dijanjikan halaman depannya.

| Hasil | Epic |
|---|---|
| 11 kategori benar-benar bisa dipakai | A |
| Deployment mengirim seluruh aplikasi | B |
| Admin panel diamankan | B3 |
| Audio lengkap untuk 11 kategori | C |
| Domain konsisten | B2 |

**Definisi selesai:** setiap kartu kategori di landing page membuka konten yang berbeda dan benar, di production.

### Fase 1 — Validasi · P1

**Tujuan:** jawab satu pertanyaan — *apakah ada yang mau membayar?*

| Hasil | Epic |
|---|---|
| Halaman legal (syarat Mayar) | E2 |
| Paket Lifetime diperbaiki | E1 |
| Pembayaran manual jalan | D1 |
| Free tier terdefinisi konsisten | D2 |
| Analytics terpasang | F |
| **30 hari data terkumpul** | D3 |

**Definisi selesai:** ada 30 hari data konversi nyata dan keputusan tertulis di §18.

### 🚦 Gerbang Keputusan

| Hasil 30 hari | Keputusan |
|---|---|
| **≥ 20 pembeli** | Lanjut Fase 2 |
| **5–19 pembeli** | Tahan. Iterasi harga/konten/distribusi 30 hari lagi |
| **< 5 pembeli** | **Jangan bangun backend.** Wawancarai 10 non-pembeli dulu |

### Fase 2 — Backend · P3 *(gated)*

Auth, PostgreSQL, sinkronisasi progres, gating premium yang bisa ditegakkan, migrasi user existing. Prasyarat: §7.4 disetujui.

### Fase 3 — Otomasi & AI · P4

Otomasi Mayar.id (dengan idempotensi), modul writing dengan penilaian AI, feedback speaking, sertifikat.

### Fase 4 — Growth · P4

PWA, landing page per kategori, perluasan blog, leaderboard, fitur komunitas.

### Estimasi Waktu

| Fase | Estimasi | Blocking? |
|---|---|---|
| Fase 0 | ~27 jam | Ya |
| Fase 1 | ~28 jam + 30 hari observasi | Ya |
| Fase 2 | ~60 jam | Gated |
| Fase 3 | ~56 jam | Gated |
| Fase 4 | ~40 jam | — |

**Fase 0 + 1 ≈ 55 jam.** Itu seluruh pekerjaan yang harus selesai sebelum keputusan besar berikutnya.

---

## 9. Monetisasi

### Model: Freemium

### Free Tier

| Yang didapat | Batas |
|---|---|
| Kategori `general` | Penuh |
| Satu kategori pilihan | Penuh (dikunci setelah dipilih) |
| Listening, Reading, Fill-in-blank | Tanpa batas, di kategori yang terbuka |
| Vocabulary | 50 kata |
| Speaking | 10 latihan/hari |
| Writing (AI) | ❌ |
| Sinkronisasi progres | ❌ (Fase 2) |

**Kenapa "satu kategori pilihan"?** Memberi nilai nyata yang cukup untuk membentuk kebiasaan, sekaligus menciptakan alasan konkret untuk upgrade: user yang pindah profesi atau ingin melebar membentur batas dengan cara yang masuk akal, bukan sewenang-wenang.

### Premium — Rp 99.000/bulan

Semua 11 kategori · vocabulary penuh · speaking tanpa batas · writing AI 20/hari *(saat tersedia)* · sinkronisasi progres · dukungan prioritas

### Lifetime — Rp 399.000 sekali bayar

Semua fitur Premium, selamanya · akses awal fitur baru · sertifikat penyelesaian

> **⚠️ Koreksi dari v1.0.** Halaman harga menjanjikan **"1-on-1 Mentoring (2x/bulan)"** pada paket Lifetime Rp 399.000 sekali bayar. Dibaca harfiah, itu 24 sesi mentoring per tahun, selamanya, dari satu pembayaran. Seratus pembeli berarti 2.400 sesi per tahun — sekitar 3 sesi setiap hari kerja tanpa henti. Itu kewajiban tak terbatas, bukan produk yang bisa diskalakan.
>
> **Perbaikan:** mentoring dibatasi **2×/bulan selama 3 bulan pertama**, lalu berhenti. Pembeli yang sudah terlanjur membeli dengan janji lama tetap dihormati haknya; perubahan hanya berlaku untuk pembeli baru.

### Course Bundle — Rp 499.000

Lifetime + 4× group coaching (Zoom) + grup WhatsApp + 1× sesi speaking 1-on-1

### Logika Harga

| Paket | Pembanding |
|---|---|
| Rp 99.000/bulan | Kurang dari satu jam tarif freelance |
| Rp 399.000 lifetime | Setara 4 bulan premium |
| Rp 499.000 bundle | ~1/10 harga bootcamp |

### Skenario Pendapatan

> **Ini skenario untuk perencanaan, bukan proyeksi.** v1.0 memproyeksikan 100.000 user gratis pada bulan 24 — dua per tiga dari seluruh segmen yang didefinisikannya sendiri. Angka di bawah lebih konservatif dan tetap harus divalidasi oleh Epic D.

| Bulan | Pengunjung/bln | Pendaftar | Pembeli (1,5%) | Pendapatan/bln |
|---|---:|---:|---:|---:|
| 3 | 800 | 160 | 2 | Rp 200rb |
| 6 | 3.000 | 600 | 9 | Rp 900rb |
| 12 | 10.000 | 2.000 | 30 | Rp 3jt |
| 24 | 30.000 | 6.000 | 90 | Rp 9jt |

**Yang paling menentukan bukan konversi, tapi distribusi.** Konversi 1,5% cukup standar; mendatangkan 10.000 pengunjung per bulan adalah bagian yang sulit. Strategi distribusi butuh perhatian setara strategi produk — lihat §17.

---

## 10. Strategi SEO

### Target Keyword

| Keyword | Volume/bln* | Kesulitan |
|---|---:|---|
| belajar speaking inggris online | 3.600 | Sedang |
| belajar bahasa inggris untuk programmer | 2.400 | Rendah |
| english for developers | 1.900 | Sedang |
| bahasa inggris teknologi | 1.600 | Rendah |
| english for remote work | 1.200 | Rendah |
| remote developer english | 880 | Rendah |
| interview bahasa inggris programmer | 720 | Rendah |
| **Total volume head term** | **~12.300** | |

\* *Sumber alat belum dicatat di v1.0. Verifikasi ulang dan catat sumbernya sebelum dipakai untuk perencanaan.*

### ⚠️ Koreksi Konsistensi

v1.0 menargetkan **30.000 traffic organik pada bulan 12** dari daftar keyword yang total volumenya hanya ~12.300/bulan. Itu tidak konsisten secara aritmetika.

**Target yang direvisi:**

| Bulan | Organik/bln | Dari mana |
|---|---:|---|
| 3 | 300 | Head term mulai naik |
| 6 | 1.500 | Head term + long-tail awal |
| 12 | 5.000 | Head term matang + 11 halaman kategori + blog |
| 24 | 12.000 | Long-tail dominan |

Angka di atas mengasumsikan **penangkapan 25–30% head term** ditambah kontribusi long-tail yang tumbuh dari halaman kategori dan blog. Melampaui ~15.000/bulan memerlukan strategi long-tail terpisah yang belum ditulis.

### Technical SEO

- [ ] Server-side rendering (Fase 2)
- [ ] URL bersih: `/kategori/copywriting`
- [ ] `sitemap.xml` otomatis · `robots.txt` (larang `/admin`)
- [ ] URL kanonik di semua halaman
- [ ] Lighthouse > 90, LCP < 2,5 detik di 4G
- [ ] Structured data (`WebApplication`, `Course`)
- [ ] Navigasi breadcrumb

### Content SEO

- [ ] **11 landing page per kategori** — aset SEO terbesar yang belum digarap; setiap halaman menyasar keyword profesi spesifik
- [ ] Blog: perluas dari 3 artikel ke 15+
- [ ] FAQ dengan `FAQPage` schema
- [ ] Testimoni & studi kasus (setelah ada user nyata)

### Off-Page SEO

- [ ] Komunitas developer & freelancer Indonesia (Discord, Telegram, Facebook)
- [ ] Guest post di dev.to dan Medium
- [ ] LinkedIn — sesuai dengan target audiens pekerja remote
- [ ] TikTok/Reels: tips bahasa Inggris pendek per profesi

---

## 11. Integrasi AI

### Penggunaan

| Fitur | Kebutuhan | Fase |
|---|---|---|
| Penilaian writing | Skor + koreksi tata bahasa + versi perbaikan | 3 |
| Feedback speaking | Umpan balik pengucapan dari transkrip | 3 |
| Contoh vocabulary | Contoh kalimat kontekstual | 4 |

### Pilihan Model

> **Koreksi dari v1.0.** v1.0 menetapkan `claude-3-haiku` — model yang sudah lawas — dan membangun seluruh model biaya di atas model "gratis" OpenRouter (`xiaomi/mimo-v2.5`). Membangun proyeksi biaya di atas tier gratis pihak ketiga itu rapuh: tier gratis bisa dibatasi atau dihapus tanpa pemberitahuan, dan seluruh perhitungan ikut runtuh.

**Model utama: Claude Haiku 4.5** — `claude-haiku-4-5`

| Properti | Nilai |
|---|---|
| Context window | 200K token |
| Harga input | $1,00 / 1 juta token |
| Harga output | $5,00 / 1 juta token |

Haiku adalah tier yang tepat di sini: penilaian writing adalah tugas terstruktur dan bervolume tinggi dengan rubrik yang jelas — persis jenis pekerjaan yang cocok untuk model cepat dan murah.

### Model Biaya

**Per panggilan penilaian writing** (~500 token input, ~200 token output):

```
Input  :  500 / 1.000.000 × $1,00  = $0,0005
Output :  200 / 1.000.000 × $5,00  = $0,0010
────────────────────────────────────────────
Total  :                             $0,0015 per panggilan
```

> v1.0 menyebut $0,0004 per panggilan — sekitar **4× terlalu rendah**. Perbaikannya tidak mengubah kelayakan bisnis (lihat di bawah), tapi angkanya harus benar.

**Batch API memangkas biaya 50%.** Penilaian writing tidak sensitif latensi — user bisa menerima hasil dalam hitungan menit. Menjalankannya lewat Batches API (`client.messages.batches.create`) menurunkan biaya menjadi **$0,00075 per panggilan**, dengan penyelesaian umumnya di bawah 1 jam.

**Proyeksi bulanan (100 user premium):**

| Skenario | Panggilan/bulan | Real-time | Via Batch |
|---|---:|---:|---:|
| Ringan (1 tulisan/hari) | 3.000 | $4,50 | $2,25 |
| Sedang (3/hari) | 9.000 | $13,50 | $6,75 |
| Berat (batas 20/hari terpakai penuh) | 60.000 | $90,00 | $45,00 |

Pendapatan dari 100 user premium ≈ Rp 9,9 juta (~$600/bulan). **Biaya AI berada di 1–15% pendapatan**, dengan skenario realistis di ujung bawah. Ekonominya sehat.

### Catatan Prompt Caching

Rubrik penilaian dan system prompt bersifat stabil dan merupakan kandidat alami untuk prompt caching. **Namun perlu diperhatikan: minimum prefix yang bisa di-cache pada Haiku 4.5 adalah 4.096 token.** Rubrik pendek tidak akan ter-cache — tidak ada error, hanya `cache_creation_input_tokens: 0` secara diam-diam. Kalau caching diinginkan, rubrik + panduan + contoh harus benar-benar melewati ambang itu; kalau tidak, jangan pasang `cache_control` sama sekali dan hemat kompleksitasnya.

### Rate Limit

```go
const (
    FreeDailyLimit    = 0   // free tier tidak mendapat akses AI
    PremiumDailyLimit = 20
    PremiumHourLimit  = 5
)
```

**Counter tinggal di Redis, bukan hasil `COUNT(*)` ke PostgreSQL.** Tabel `ai_usage` adalah catatan audit dan akuntansi biaya; penegakan rate limit memakai counter Redis dengan TTL yang habis di tengah malam waktu Jakarta.

### Kontrol Biaya

- [ ] Batas anggaran bulanan; melewatinya → fitur AI degradasi anggun dengan pesan jelas, bukan error
- [ ] Setiap panggilan mencatat token dan biaya ke `ai_usage`
- [ ] Alert saat pemakaian harian melampaui ambang
- [ ] Batch untuk semua penilaian non-interaktif

---

## 12. Skema Database

> Skema ini memperbaiki empat masalah pada v1.0: kerentanan webhook, tiga sumber kebenaran status langganan, progres yang tidak sadar kategori, dan penyimpanan rekaman suara.

```sql
-- =========================================================
-- USERS
-- Catatan: kolom `plan` di v1.0 dihapus. Status langganan
-- punya satu sumber kebenaran: tabel `subscriptions`.
-- =========================================================
CREATE TABLE users (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email          VARCHAR(255) UNIQUE NOT NULL,
    name           VARCHAR(100) NOT NULL,
    password_hash  VARCHAR(255) NOT NULL,   -- argon2id
    avatar_url     VARCHAR(500),
    free_category  VARCHAR(50),             -- kategori gratis pilihan user
    streak_count   INTEGER   DEFAULT 0,
    total_xp       INTEGER   DEFAULT 0,
    level          INTEGER   DEFAULT 1,
    last_active_at TIMESTAMPTZ,
    created_at     TIMESTAMPTZ DEFAULT NOW(),
    updated_at     TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_users_email ON users(email);

-- =========================================================
-- REFRESH TOKENS
-- v1.0 menyebut "JWT + Refresh Token" di arsitektur
-- tapi tidak pernah mendefinisikan tabelnya.
-- =========================================================
CREATE TABLE refresh_tokens (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id    UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token_hash VARCHAR(255) NOT NULL UNIQUE,  -- simpan hash, jangan token mentah
    expires_at TIMESTAMPTZ NOT NULL,
    revoked_at TIMESTAMPTZ,
    user_agent VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_refresh_user ON refresh_tokens(user_id) WHERE revoked_at IS NULL;

-- =========================================================
-- PROGRES USER
-- Perubahan penting: ditambah kolom `category`.
-- v1.0 memakai kunci (user, chapter, skill) — nama chapter
-- seperti "Greetings" muncul di beberapa kategori sekaligus,
-- sehingga progres antar-kategori akan saling menimpa.
-- =========================================================
CREATE TABLE user_progress (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id           UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category          VARCHAR(50)  NOT NULL,   -- slug kanonik
    chapter           VARCHAR(100) NOT NULL,
    skill_type        VARCHAR(20)  NOT NULL,   -- listening|reading|speaking|writing|vocabulary
    best_score        INTEGER   DEFAULT 0,
    total_attempts    INTEGER   DEFAULT 0,
    completed         BOOLEAN   DEFAULT FALSE,
    last_practiced_at TIMESTAMPTZ,
    created_at        TIMESTAMPTZ DEFAULT NOW(),
    updated_at        TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, category, chapter, skill_type)
);
CREATE INDEX idx_progress_user_cat ON user_progress(user_id, category);

-- =========================================================
-- LATIHAN WRITING
-- =========================================================
CREATE TABLE writing_exercises (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id       UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category      VARCHAR(50)  NOT NULL,
    chapter       VARCHAR(100) NOT NULL,
    topic         TEXT NOT NULL,
    user_input    TEXT NOT NULL,
    ai_score      INTEGER,     -- 0-100
    ai_feedback   JSONB,       -- {grammar:[], vocabulary:[], improved:""}
    ai_model      VARCHAR(50),
    tokens_input  INTEGER DEFAULT 0,
    tokens_output INTEGER DEFAULT 0,
    created_at    TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_writing_user ON writing_exercises(user_id, created_at DESC);

-- =========================================================
-- LATIHAN SPEAKING
-- Perubahan penting: kolom `audio_url` dari v1.0 DIHAPUS.
-- Rekaman suara adalah data pribadi. Kita menyimpan transkrip
-- dan skor saja — ini menghilangkan seluruh kelas kewajiban
-- hukum tanpa mengurangi nilai produk. Lihat §14.
-- =========================================================
CREATE TABLE speaking_practices (
    id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id          UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category         VARCHAR(50) NOT NULL,
    script_num_id    VARCHAR(50),
    mode             VARCHAR(20) NOT NULL,  -- practice|freetalk|conversation
    expected_text    TEXT,
    transcribed_text TEXT,
    similarity_score INTEGER,
    duration_seconds INTEGER,
    created_at       TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_speaking_user ON speaking_practices(user_id, created_at DESC);

-- =========================================================
-- PEMBAYARAN
-- Perubahan penting: mayar_invoice_id UNIQUE.
-- Ini adalah pertahanan tingkat database terhadap aktivasi
-- premium ganda akibat webhook retry.
-- =========================================================
CREATE TABLE payments (
    id                   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id              UUID NOT NULL REFERENCES users(id),
    mayar_invoice_id     VARCHAR(100) NOT NULL UNIQUE,
    mayar_transaction_id VARCHAR(100),
    amount               INTEGER NOT NULL,      -- Rupiah
    currency             VARCHAR(3) DEFAULT 'IDR',
    plan_type            VARCHAR(20) NOT NULL,  -- monthly|lifetime|course
    payment_method       VARCHAR(50),
    status               VARCHAR(20) DEFAULT 'pending',
                         -- pending|paid|failed|refunded|expired
    paid_at              TIMESTAMPTZ,
    metadata             JSONB,
    created_at           TIMESTAMPTZ DEFAULT NOW(),
    updated_at           TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_payments_user ON payments(user_id);

-- =========================================================
-- EVENT WEBHOOK  (tabel baru — tidak ada di v1.0)
-- Mayar.id melakukan retry pengiriman webhook. Tanpa
-- penjagaan idempotensi, retry mengaktifkan premium
-- berkali-kali. Tabel ini adalah penjagaannya.
-- =========================================================
CREATE TABLE webhook_events (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider     VARCHAR(20)  NOT NULL DEFAULT 'mayar',
    event_id     VARCHAR(255) NOT NULL,   -- id event dari provider
    event_type   VARCHAR(50)  NOT NULL,
    payload      JSONB        NOT NULL,   -- body mentah, untuk audit
    processed_at TIMESTAMPTZ,
    created_at   TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(provider, event_id)
);

-- =========================================================
-- LANGGANAN — SATU-SATUNYA SUMBER KEBENARAN
-- =========================================================
CREATE TABLE subscriptions (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id      UUID NOT NULL REFERENCES users(id),
    plan_type    VARCHAR(20) NOT NULL,   -- monthly|lifetime|course
    starts_at    TIMESTAMPTZ NOT NULL,
    expires_at   TIMESTAMPTZ,            -- NULL = lifetime
    payment_id   UUID REFERENCES payments(id),
    status       VARCHAR(20) DEFAULT 'active',  -- active|expired|cancelled
    cancelled_at TIMESTAMPTZ,
    created_at   TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_subs_user_active ON subscriptions(user_id)
    WHERE status = 'active';

-- Cek entitlement: query view ini, jangan users.plan
CREATE VIEW active_entitlements AS
SELECT user_id,
       plan_type,
       expires_at,
       (expires_at IS NULL OR expires_at > NOW()) AS is_valid
FROM subscriptions
WHERE status = 'active';

-- =========================================================
-- PEMAKAIAN AI  (audit & biaya; rate limit ada di Redis)
-- =========================================================
CREATE TABLE ai_usage (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id       UUID NOT NULL REFERENCES users(id),
    feature       VARCHAR(20) NOT NULL,  -- writing|speaking|vocabulary
    model         VARCHAR(50) NOT NULL,
    tokens_input  INTEGER DEFAULT 0,
    tokens_output INTEGER DEFAULT 0,
    cost_usd_e6   BIGINT  DEFAULT 0,     -- USD × 1.000.000, hindari float
    created_at    TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_ai_usage_user_date ON ai_usage(user_id, created_at DESC);

-- =========================================================
-- LEADERBOARD
-- Strategi refresh: cron tiap 15 menit.
-- v1.0 mendefinisikan view ini tanpa menyebut cara me-refresh-nya.
-- =========================================================
CREATE MATERIALIZED VIEW leaderboard AS
SELECT u.id, u.name, u.total_xp, u.level, u.streak_count,
       RANK() OVER (ORDER BY u.total_xp DESC) AS rank
FROM users u
WHERE u.total_xp > 0;
CREATE UNIQUE INDEX idx_leaderboard_id ON leaderboard(id);
-- Refresh: REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard;
```

### Desain Webhook yang Benar

> v1.0 menulis `ActivatePremium(payload.UserID, payload.PlanType)` — mempercayai `user_id` yang dikirim di **body webhook**. Siapa pun yang bisa membentuk request ke endpoint itu bisa mengaktifkan premium untuk akun mana pun. Perbaikannya: **selalu resolusi lewat record milik sendiri.**

```go
func HandleMayarWebhook(c echo.Context) error {
    raw, err := io.ReadAll(c.Request().Body)
    if err != nil {
        return echo.ErrBadRequest
    }

    // 1. Verifikasi signature SEBELUM parsing apa pun
    if !VerifyMayarSignature(raw, c.Request().Header.Get("X-Mayar-Signature")) {
        return echo.ErrUnauthorized
    }

    var p MayarWebhook
    if err := json.Unmarshal(raw, &p); err != nil {
        return echo.ErrBadRequest
    }

    // 2. Penjagaan idempotensi — retry dari Mayar berhenti di sini
    inserted, err := repo.InsertWebhookEvent(ctx, "mayar", p.EventID, p.Type, raw)
    if err != nil {
        return err
    }
    if !inserted {
        return c.JSON(200, map[string]string{"status": "duplicate"})
    }

    // 3. Resolusi user dari record SENDIRI, bukan dari payload.
    //    Ini yang menutup lubang keamanan di v1.0.
    payment, err := repo.FindPaymentByInvoiceID(ctx, p.InvoiceID)
    if err != nil {
        return err
    }

    // 4. Transisi status yang dijaga — 'paid' tidak bisa mundur
    switch p.Status {
    case "paid":
        if payment.Status != "pending" {
            return c.JSON(200, map[string]string{"status": "already_processed"})
        }
        if err := svc.ActivateSubscription(ctx, payment); err != nil {
            return err
        }
    case "expired", "failed":
        if err := svc.MarkPaymentFailed(ctx, payment.ID, p.Status); err != nil {
            return err
        }
    }

    repo.MarkWebhookProcessed(ctx, p.EventID)
    return c.JSON(200, map[string]string{"status": "ok"})
}
```

**Empat pertahanan berlapis:** verifikasi signature → idempotensi tingkat database → resolusi user dari record sendiri → penjagaan transisi status. Menghilangkan salah satunya membuat tiga sisanya lebih rapuh.

---

## 13. Analytics & Instrumentation

> Tidak ada di v1.0. Konsekuensinya: v1.0 menargetkan retensi D7 dan NPS tanpa satu pun alat untuk mengukurnya. Target yang tidak terukur bukan target.

### Alat

Analytics ramah privasi (Plausible atau Umami self-hosted). GA4 dihindari — cookie banner-nya menambah beban legal tanpa memberi wawasan tambahan pada skala ini.

### Event yang Dilacak

| Event | Properti | Pertanyaan yang dijawab |
|---|---|---|
| `category_selected` | slug | Profesi mana yang paling diminati? |
| `lesson_started` | slug, mode | Mode belajar mana yang dipakai? |
| `lesson_completed` | slug, mode, skor | Berapa yang menyelesaikan? |
| `paywall_viewed` | slug | Di mana orang membentur batas? |
| `checkout_clicked` | paket | Berapa yang berniat bayar? |
| `purchase_completed` | paket, nominal | Berapa yang benar-benar bayar? |
| `audio_fallback_used` | num_id | File audio mana yang bermasalah? |
| `speech_unsupported` | user agent | Berapa besar dampak celah iOS? |

### Funnel

```
Kunjungan → Pilih kategori → Mulai lesson → Selesai → Paywall → Checkout → Beli
```

Setiap tahap direkam. Titik bocor terbesar menentukan apa yang dikerjakan berikutnya.

### Feedback Kualitatif

- Widget 👍/👎 di akhir setiap lesson
- Survei NPS setelah lesson ke-5 (bukan pertama — terlalu dini untuk bermakna)
- Kanal kontak yang terlihat di footer

**Aturan yang mengikat:** tidak ada PII yang dikirim ke analytics. Tanpa email, tanpa nama, tanpa isi tulisan.

---

## 14. Legal, Privasi, dan Data

> Tidak ada di v1.0. Ini **memblokir monetisasi** — payment gateway Indonesia umumnya mensyaratkan halaman ini sebelum menyetujui akun merchant.

### Halaman yang Wajib Ada

| Halaman | Isi |
|---|---|
| `terms.html` | Cakupan layanan, kewajiban user, batasan tanggung jawab, klausa perubahan harga |
| `privacy.html` | Data yang dikumpulkan, dasar hukum, retensi, hak user, kontak |
| `refund.html` | Refund 7 hari tanpa syarat, cara mengajukan, SLA proses |

### Sikap terhadap Rekaman Suara

Modul speaking mengakses mikrofon. Ini keputusan produk yang perlu dinyatakan tegas:

> **Audio diproses di perangkat lewat Web Speech API dan tidak pernah dikirim atau disimpan di server kami. Yang tersimpan hanya teks transkrip dan skor kemiripan.**

Karena itu kolom `speaking_practices.audio_url` dari v1.0 dihapus dari skema. Menyimpan rekaman suara akan memicu kewajiban perlindungan data biometrik tanpa memberi nilai produk yang sepadan. Kalau suatu saat penyimpanan audio benar-benar diperlukan, itu keputusan terpisah yang butuh: persetujuan eksplisit, kebijakan retensi, mekanisme penghapusan, dan penilaian ulang di §18.

### Kepatuhan

- UU Perlindungan Data Pribadi (UU 27/2022)
- Persyaratan merchant Mayar.id
- Persetujuan cookie hanya jika analytics memerlukannya (Plausible tidak)

### Data yang Dikumpulkan

| Data | Tujuan | Retensi |
|---|---|---|
| Email, nama | Akun | Sampai akun dihapus |
| Progres belajar | Fungsi inti | Sampai akun dihapus |
| Transkrip speaking | Umpan balik ke user | 90 hari |
| Riwayat pembayaran | Kewajiban akuntansi | 5 tahun (ketentuan pajak) |
| Analytics | Perbaikan produk | 24 bulan, teragregasi |

---

## 15. Risk Register

> Tidak ada di v1.0.

| ID | Risiko | Dampak | Kemungkinan | Mitigasi |
|---|---|---|---|---|
| **R-01** | **Safari iOS tidak mendukung `SpeechRecognition`** — modul Speaking mati total di sana | Tinggi | **Pasti** | Deteksi dan tampilkan pesan jujur + alternatif. Jangka menengah: rekam → kirim ke server → Whisper. Persona menyebut iOS ~20% |
| R-02 | Konversi berbayar di bawah ambang | Tinggi | Sedang | Gerbang D3 mencegah investasi backend yang sia-sia |
| R-03 | Distribusi gagal — produk bagus, tidak ada yang tahu | Tinggi | Sedang | Rencana distribusi butuh perhatian setara rencana produk. Lihat §17 |
| R-04 | Ketergantungan pada tier gratis AI pihak ketiga | Sedang | Tinggi | Model biaya dibangun di atas harga berbayar Haiku 4.5, bukan tier gratis |
| R-05 | Kualitas konten TTS untuk istilah teknis | Sedang | Sedang | QA sampel per kategori; override fonetik untuk `API`, `SEO`, `UI/UX`, `CTA` |
| R-06 | Tim satu orang — bus factor 1 | Tinggi | — | Dokumentasikan semuanya (`CLAUDE.md`, `notes/`); hindari kepintaran yang tidak perlu |
| R-07 | Ukuran repo tumbuh karena aset audio | Rendah | Tinggi | Keputusan penyimpanan di task G3; Cloudflare R2 kalau melewati batas nyaman |
| R-08 | Admin panel tanpa auth terekspos publik | Tinggi | Tinggi (setelah B1) | B3 harus dirilis bersamaan dengan B1, bukan setelahnya |
| R-09 | Kompetitor meniru posisi "per profesi" | Sedang | Sedang | Kecepatan + kedekatan komunitas; posisi ini tidak punya parit teknologi |

---

## 16. Success Metrics

> Target v1.0 direvisi ke angka yang bisa dipertanggungjawabkan. Target yang mustahil membuat kita salah membaca sinyal — mustahil membedakan "sedang berjalan baik" dari "sedang gagal" kalau tolok ukurnya fiksi.

### KPI Produk

| Metrik | Bulan 3 | Bulan 6 | Bulan 12 | v1.0 bilang | Kenapa direvisi |
|---|---:|---:|---:|---:|---|
| Pendaftar | 160 | 600 | 2.000 | 30.000 | v1.0 mengasumsikan traffic yang tidak didukung strategi SEO-nya sendiri |
| DAU | 20 | 80 | 300 | 5.000 | Turun proporsional |
| Retensi D7 | 15% | 18% | 22% | 50% | 50% setingkat Duolingo. Edtech umum 10–20% |
| Konversi berbayar | 1% | 1,5% | 1,5% | 2% | Dipertahankan konservatif sampai tervalidasi |
| Pendapatan bulanan | Rp 200rb | Rp 900rb | Rp 3jt | Rp 45jt | Turun mengikuti basis user |
| NPS | — | 25 | 35 | 50 | 50 itu luar biasa; 30–40 sudah sangat baik |

### Metrik Teknis

| Metrik | Target |
|---|---|
| Lighthouse (mobile) | > 90 |
| LCP di 4G | < 2,5 detik |
| Uptime | 99,5% (realistis untuk satu VPS) |
| JS error rate | < 0,5% sesi |
| Cakupan audio | 100% (1.142/1.142) |

### Metrik Bisnis

| Metrik | Target | v1.0 bilang |
|---|---|---|
| CAC | < Rp 30.000 | < Rp 10.000 |
| LTV | > Rp 150.000 | > Rp 300.000 |
| LTV:CAC | **> 3:1** | > 30:1 |
| Payback | < 6 bulan | < 3 bulan |

> **Soal LTV:CAC 30:1.** Itu bukan target, itu fantasi — tidak ada perusahaan yang merencanakannya. Standar sehat adalah 3:1. Angka 30:1 di v1.0 menandakan asumsi CAC-nya (< Rp 10.000) tidak pernah dimodelkan sama sekali.

---

## 17. Open Questions

Pertanyaan yang belum terjawab, beserta cara menjawabnya.

| # | Pertanyaan | Cara menjawab | Kapan dibutuhkan |
|---|---|---|---|
| Q1 | **Apa strategi distribusinya?** Ini pertanyaan yang paling belum tergarap. Produk bagus tanpa distribusi tidak menghasilkan apa pun | Pilih 2 kanal (komunitas + LinkedIn/TikTok), jalankan 30 hari, ukur | Sebelum Fase 1 |
| Q2 | Kategori mana yang paling diminati? | Event `category_selected` menjawabnya dalam 2 minggu | Fase 1 |
| Q3 | Apakah Rp 99.000 titik harga yang tepat? | Uji A/B pada 3 titik harga setelah ada traffic dasar | Setelah D3 |
| Q4 | Perlukah user memilih satu kategori gratis, atau semua kategori sebagian? | Uji keduanya; ukur konversi dari `paywall_viewed` | Fase 1 |
| Q5 | Siapa yang menulis konten kategori berikutnya? | Butuh proses content ops — belum ada | Sebelum kategori ke-12 |
| Q6 | Apakah mentoring layak dipertahankan sama sekali? | Hitung jam nyata setelah 10 pembeli pertama | Setelah 10 penjualan |
| Q7 | Apakah `graphic-design` dan `web-design` cukup berbeda untuk jadi dua kategori? | Lihat overlap konten dan minat user | Fase 1 |
| Q8 | Apakah PWA benar-benar dibutuhkan, atau web mobile sudah cukup? | Ukur bounce rate mobile dan permintaan user | Fase 4 |

---

## 18. Decision Log

Keputusan yang mengikat, beserta alasannya. Entri baru ditambahkan, entri lama tidak dihapus.

| Tgl | Keputusan | Alasan | Status |
|---|---|---|---|
| 2026-08-03 | Domain kanonik: `english.tool.biz.id` | Konsistensi; 15 referensi di kode vs 4 di dokumen lama | Final |
| 2026-08-03 | Slug kanonik = `id` di `content/categories.json` | Tiga skema penamaan yang bentrok butuh satu pemenang | Final |
| 2026-08-03 | Monetisasi **sebelum** rewrite Go | 60 jam tanpa validasi permintaan adalah risiko terbesar dalam rencana | Final |
| 2026-08-03 | Jangan simpan rekaman suara | Menghilangkan kewajiban data biometrik; nilai produk tidak berkurang | Final |
| 2026-08-03 | Mentoring Lifetime dibatasi 3 bulan pertama | Bayar-sekali + layanan manusia selamanya = kewajiban tak terbatas | Final |
| 2026-08-03 | Model AI: Claude Haiku 4.5 berbayar, bukan tier gratis | Tier gratis pihak ketiga bukan fondasi untuk model biaya | Final |
| 2026-08-03 | Merge per-field untuk konflik progres, bukan last-write-wins | LWW menghilangkan sesi offline user | Usulan — perlu persetujuan sebelum H5 |
| 2026-08-03 | Go + HTMX, karena kecocokan tim | Keunggulan teknisnya lebih kecil dari klaim v1.0; kecocokan penulis yang menentukan | Final |
| — | *Hasil gerbang D3* | — | **Menunggu 30 hari data** |

---

## Lampiran

### A. Struktur Konten

```json
// content/categories.json — manifest
{
  "categories": [
    {
      "id": "copywriting",
      "slug": "copywriting",
      "name": "Copywriting",
      "icon": "✍️",
      "description": "English untuk copywriter",
      "color": "#a855f7",
      "hasAudio": false,
      "topics": ["sales-copy", "landing-pages", "email-marketing"]
    }
  ]
}

// content/copywriting.json — konten
{
  "id": "copywriting",
  "name": "Copywriting",
  "scripts": [
    {
      "num_id": "copywriting_001",
      "chapter": "Sales Copy",
      "type": "phrase",
      "role": "Speaker",
      "en": "I'll write compelling sales copy for the landing page.",
      "translation": "Saya akan tulis sales copy yang menarik untuk landing page."
    }
  ]
}
```

**Aturan `num_id`:** `{slug}_{urut 3 digit}`. File audio mengikuti: `{num_id}.mp3` (Inggris) dan `{num_id}_id.mp3` (Indonesia). Kategori `software-engineering` memakai `num_id` numerik warisan (`1`–`120`) — dipertahankan agar audio yang sudah ada tetap berlaku.

### B. Struktur Proyek Go *(Fase 2)*

```
english-learning/
├── cmd/server/main.go
├── internal/
│   ├── handler/      auth · quiz · progress · payment · webhook
│   ├── middleware/   auth · ratelimit · cors · recover
│   ├── model/        user · progress · payment · subscription
│   ├── service/      auth · ai · payment · progress · content
│   ├── repository/   user · progress · payment · webhook
│   └── template/     layout · partials (HTMX)
├── web/static/       css · js · audio
├── content/          11 kategori JSON (tidak berubah)
├── migrations/
├── notes/            prd.md · task.md
├── go.mod
├── Dockerfile
└── docker-compose.yml
```

### C. Environment Variables

```bash
# Database
DATABASE_URL=postgres://user:pass@localhost:5432/english_learning
REDIS_URL=redis://localhost:6379

# Auth
JWT_SECRET=<32+ byte acak>
JWT_ACCESS_TTL=15m
JWT_REFRESH_TTL=720h

# Mayar.id
MAYAR_API_KEY=
MAYAR_WEBHOOK_SECRET=

# AI
ANTHROPIC_API_KEY=
AI_MODEL=claude-haiku-4-5
AI_MONTHLY_BUDGET_USD=50

# Server
PORT=3000
ENV=production
BASE_URL=https://english.tool.biz.id
```

### D. Endpoint API *(Fase 2)*

```
POST   /api/auth/register          POST   /api/auth/login
POST   /api/auth/refresh           POST   /api/auth/logout

GET    /                           → landing
GET    /kategori/{slug}            → landing page kategori (SEO)
GET    /app?category={slug}        → aplikasi belajar
GET    /pricing                    /blog/{slug}

GET    /api/progress               PUT    /api/progress
POST   /api/progress/migrate       → migrasi dari localStorage
GET    /api/leaderboard

POST   /quiz/{mode}/submit         POST   /speaking/submit
GET    /writing/{category}         POST   /writing/submit

POST   /api/checkout               POST   /api/webhook/mayar
GET    /api/subscription/status

GET    /api/categories             GET    /api/content/{slug}
```

---

*Dokumen ini menggantikan `PRD.md` v1.0. Setiap klaim tentang status produk berasal dari audit kode pada commit `46b960b` dan bisa diverifikasi lewat perintah di [`notes/task.md`](./task.md) Lampiran B.*

*FathForce Academy — Agustus 2026*
