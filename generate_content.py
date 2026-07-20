#!/usr/bin/env python3
"""Generate English learning content for 11 categories."""
import json
import os

OUTPUT_DIR = "/tmp/english-learning/content"

categories = [
    {
        "id": "general",
        "name": "General English",
        "chapters": [
            {
                "chapter": "Greetings",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Hi! Nice to meet you. I'm a remote developer.", "translation": "Halo! Senang bertemu denganmu. Saya developer remote."},
                    {"type": "dialogue", "role": "A", "en": "How are you doing today?", "translation": "Bagaimana kabarmu hari ini?"},
                    {"type": "dialogue", "role": "B", "en": "I'm doing great, thanks! Just finished a sprint.", "translation": "Saya baik-baik saja, terima kasih! Baru selesai sprint."},
                    {"type": "phrase", "role": "Speaker", "en": "Good morning! Ready for the standup?", "translation": "Selamat pagi! Siap untuk standup?"},
                    {"type": "dialogue", "role": "A", "en": "Long time no see! How's the new project?", "translation": "Lama tidak bertemu! Bagaimana project barunya?"},
                    {"type": "dialogue", "role": "B", "en": "It's going well! We're building a mobile app.", "translation": "Berjalan lancar! Kami sedang membangun aplikasi mobile."},
                    {"type": "phrase", "role": "Speaker", "en": "See you at the next meeting!", "translation": "Sampai jumpa di pertemuan berikutnya!"},
                    {"type": "dialogue", "role": "A", "en": "What time zone are you in?", "translation": "Kamu di timezone berapa?"},
                    {"type": "dialogue", "role": "B", "en": "I'm in GMT+7, same as Jakarta.", "translation": "Saya di GMT+7, sama seperti Jakarta."},
                ]
            },
            {
                "chapter": "Daily Conversation",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I work from home most days.", "translation": "Saya bekerja dari rumah kebanyakan hari."},
                    {"type": "dialogue", "role": "A", "en": "What do you do for a living?", "translation": "Apa pekerjaan kamu?"},
                    {"type": "dialogue", "role": "B", "en": "I'm a full-stack developer working remotely.", "translation": "Saya full-stack developer yang bekerja remote."},
                    {"type": "phrase", "role": "Speaker", "en": "My internet connection is unstable today.", "translation": "Koneksi internet saya tidak stabil hari ini."},
                    {"type": "dialogue", "role": "A", "en": "Do you prefer working in the morning or evening?", "translation": "Kamu lebih suka kerja pagi atau malam?"},
                    {"type": "dialogue", "role": "B", "en": "I'm a night owl, so I code better after 8 PM.", "translation": "Saya orang malam, jadi saya lebih produktif coding setelah jam 8 malam."},
                    {"type": "phrase", "role": "Speaker", "en": "Let me share my screen.", "translation": "Saya akan share layar saya."},
                    {"type": "dialogue", "role": "A", "en": "Can you hear me okay?", "translation": "Apakah kamu bisa mendengar saya dengan jelas?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, loud and clear.", "translation": "Ya, jelas sekali."},
                    {"type": "phrase", "role": "Speaker", "en": "I need to grab a coffee, be right back.", "translation": "Saya perlu ambil kopi, sebentar ya."},
                ]
            },
            {
                "chapter": "Travel",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'm traveling to Bali for a tech conference.", "translation": "Saya akan pergi ke Bali untuk konferensi teknologi."},
                    {"type": "dialogue", "role": "A", "en": "Where is the nearest coworking space?", "translation": "Di mana coworking space terdekat?"},
                    {"type": "dialogue", "role": "B", "en": "There's one about 10 minutes from here.", "translation": "Ada satu sekitar 10 menit dari sini."},
                    {"type": "phrase", "role": "Speaker", "en": "I need to extend my hotel booking by two days.", "translation": "Saya perlu memperpanjang booking hotel dua hari."},
                    {"type": "dialogue", "role": "A", "en": "Is the WiFi good at your hotel?", "translation": "Apakah WiFi bagus di hotel kamu?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it's fast enough for video calls.", "translation": "Ya, cukup cepat untuk video call."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll be working from a cafe today.", "translation": "Saya akan kerja dari cafe hari ini."},
                    {"type": "dialogue", "role": "A", "en": "Can you recommend a good restaurant nearby?", "translation": "Bisa rekomendasi restoran bagus di sekitar sini?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, there's a great warung on the corner.", "translation": "Tentu, ada warung bagus di pojokan."},
                ]
            },
            {
                "chapter": "Food",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Let's order lunch via GoFood.", "translation": "Ayo pesan makan siang lewat GoFood."},
                    {"type": "dialogue", "role": "A", "en": "What kind of food do you like?", "translation": "Kamu suka makanan apa?"},
                    {"type": "dialogue", "role": "B", "en": "I love Indonesian food, especially nasi goreng.", "translation": "Saya suka makanan Indonesia, terutama nasi goreng."},
                    {"type": "phrase", "role": "Speaker", "en": "I usually skip lunch when I'm deep in coding.", "translation": "Saya biasanya lewatkan makan siang saat sedang fokus coding."},
                    {"type": "dialogue", "role": "A", "en": "Do you want to grab coffee after the meeting?", "translation": "Mau ngopi setelah meeting?"},
                    {"type": "dialogue", "role": "B", "en": "Sure! I know a great coffee shop nearby.", "translation": "Tentu! Saya tahu kedai kopi bagus di dekat sini."},
                    {"type": "phrase", "role": "Speaker", "en": "The food here is delicious and affordable.", "translation": "Makanan di sini enak dan terjangkau."},
                    {"type": "dialogue", "role": "A", "en": "Are you vegetarian?", "translation": "Kamu vegetarian?"},
                    {"type": "dialogue", "role": "B", "en": "No, but I'm trying to eat healthier.", "translation": "Tidak, tapi saya sedang mencoba makan lebih sehat."},
                ]
            },
            {
                "chapter": "Shopping",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I need to buy a new keyboard.", "translation": "Saya perlu membeli keyboard baru."},
                    {"type": "dialogue", "role": "A", "en": "Where did you buy your standing desk?", "translation": "Di mana kamu beli meja berdiri kamu?"},
                    {"type": "dialogue", "role": "B", "en": "I ordered it from Tokopedia during the sale.", "translation": "Saya pesan dari Tokopedia saat diskon."},
                    {"type": "phrase", "role": "Speaker", "en": "How much does a good monitor cost?", "translation": "Berapa harga monitor yang bagus?"},
                    {"type": "dialogue", "role": "A", "en": "Do you prefer mechanical or membrane keyboards?", "translation": "Kamu lebih suka keyboard mekanis atau membran?"},
                    {"type": "dialogue", "role": "B", "en": "I prefer mechanical with blue switches.", "translation": "Saya lebih suka mekanis dengan switch blue."},
                    {"type": "phrase", "role": "Speaker", "en": "Let me check the reviews before buying.", "translation": "Saya cek ulasannya dulu sebelum beli."},
                    {"type": "dialogue", "role": "A", "en": "Is there a warranty for this laptop?", "translation": "Apakah ada garansi untuk laptop ini?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it comes with a two-year warranty.", "translation": "Ya, sudah termasuk garansi dua tahun."},
                ]
            }
        ]
    },
    {
        "id": "business",
        "name": "Business English",
        "chapters": [
            {
                "chapter": "Meetings",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Let's kick off the meeting with a quick update.", "translation": "Ayo mulai meeting dengan update singkat."},
                    {"type": "dialogue", "role": "A", "en": "Can everyone join the Zoom call?", "translation": "Bisakah semua orang join Zoom call?"},
                    {"type": "dialogue", "role": "B", "en": "I'm having audio issues, can you hear me now?", "translation": "Saya ada masalah audio, bisa dengar saya sekarang?"},
                    {"type": "phrase", "role": "Speaker", "en": "Let's table this discussion for the next meeting.", "translation": "Ayo tunda diskusi ini untuk meeting berikutnya."},
                    {"type": "dialogue", "role": "A", "en": "Who will take the meeting minutes?", "translation": "Siapa yang akan mencatat hasil meeting?"},
                    {"type": "dialogue", "role": "B", "en": "I'll handle it. I'll share the notes on Slack.", "translation": "Saya yang tanggung. Saya akan bagikan catatannya di Slack."},
                    {"type": "phrase", "role": "Speaker", "en": "Let's wrap up. Any final questions?", "translation": "Ayo tutup. Ada pertanyaan terakhir?"},
                    {"type": "dialogue", "role": "A", "en": "Can we schedule a follow-up for next week?", "translation": "Bisa kita jadwalkan follow-up minggu depan?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, I'll send a calendar invite.", "translation": "Tentu, saya akan kirim undangan kalender."},
                ]
            },
            {
                "chapter": "Negotiation",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "What's your best rate for this project?", "translation": "Tarif terbaik kamu untuk project ini berapa?"},
                    {"type": "dialogue", "role": "A", "en": "We need to find a middle ground on the budget.", "translation": "Kita perlu menemukan titik tengah soal budget."},
                    {"type": "dialogue", "role": "B", "en": "I understand. Let me propose a flexible plan.", "translation": "Saya mengerti. Saya usulkan rencana fleksibel."},
                    {"type": "phrase", "role": "Speaker", "en": "That's below my minimum rate, unfortunately.", "translation": "Itu di bawah tarif minimum saya, sayangnya."},
                    {"type": "dialogue", "role": "A", "en": "Can we offer equity instead of full payment?", "translation": "Bisa kami tawarkan ekuitas sebagai pengganti pembayaran penuh?"},
                    {"type": "dialogue", "role": "B", "en": "I'd prefer a mix of cash and equity.", "translation": "Saya lebih suka kombinasi cash dan ekuitas."},
                    {"type": "phrase", "role": "Speaker", "en": "Let me think about it and get back to you.", "translation": "Biarkan saya pikirkan dan saya kabari nanti."},
                    {"type": "dialogue", "role": "A", "en": "What's included in the scope of work?", "translation": "Apa yang termasuk dalam cakupan kerja?"},
                    {"type": "dialogue", "role": "B", "en": "Development, testing, and one month of support.", "translation": "Pengembangan, testing, dan satu bulan support."},
                ]
            },
            {
                "chapter": "Presentations",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Today I'll walk you through our tech stack.", "translation": "Hari ini saya akan menjelaskan tech stack kami."},
                    {"type": "dialogue", "role": "A", "en": "Can you share the slide deck with the team?", "translation": "Bisa share slide deck ke tim?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I've uploaded it to Google Drive.", "translation": "Ya, saya sudah upload ke Google Drive."},
                    {"type": "phrase", "role": "Speaker", "en": "Let me demo the new feature.", "translation": "Saya perlihatkan demo fitur baru."},
                    {"type": "dialogue", "role": "A", "en": "What metrics will you be presenting?", "translation": "Metrik apa yang akan kamu presentasikan?"},
                    {"type": "dialogue", "role": "B", "en": "Revenue growth, user retention, and churn rate.", "translation": "Pertumbuhan pendapatan, retensi pengguna, dan churn rate."},
                    {"type": "phrase", "role": "Speaker", "en": "Any questions before I move to the next slide?", "translation": "Ada pertanyaan sebelum saya lanjut ke slide berikutnya?"},
                    {"type": "dialogue", "role": "A", "en": "Your presentation was very clear, thank you.", "translation": "Presentasimu sangat jelas, terima kasih."},
                    {"type": "dialogue", "role": "B", "en": "Thanks! I'll send the recording later.", "translation": "Terima kasih! Saya akan kirim rekamannya nanti."},
                ]
            },
            {
                "chapter": "Networking",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "What do you do for a living?", "translation": "Apa pekerjaan kamu?"},
                    {"type": "dialogue", "role": "A", "en": "I'm a freelance developer specializing in React.", "translation": "Saya developer freelance yang mengkhususkan diri di React."},
                    {"type": "dialogue", "role": "B", "en": "That's great! I'm looking for someone with those skills.", "translation": "Bagus! Saya sedang mencari orang dengan keahlian itu."},
                    {"type": "phrase", "role": "Speaker", "en": "Can I add you on LinkedIn?", "translation": "Boleh saya tambah di LinkedIn?"},
                    {"type": "dialogue", "role": "A", "en": "Do you attend any tech meetups?", "translation": "Kamu ikut tech meetup nggak?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I go to the Jakarta JS meetup every month.", "translation": "Ya, saya datang ke Jakarta JS meetup tiap bulan."},
                    {"type": "phrase", "role": "Speaker", "en": "I'd love to collaborate on a project.", "translation": "Saya ingin berkolaborasi dalam suatu project."},
                    {"type": "dialogue", "role": "A", "en": "Here's my business card.", "translation": "Ini kartu nama saya."},
                    {"type": "dialogue", "role": "B", "en": "Thanks! I'll reach out to you on email.", "translation": "Terima kasih! Saya akan hubungi kamu lewat email."},
                ]
            },
            {
                "chapter": "Email",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll send you the project proposal by EOD.", "translation": "Saya akan kirim proposal project sebelum akhir hari."},
                    {"type": "dialogue", "role": "A", "en": "Did you receive my email about the deadline?", "translation": "Apakah kamu menerima email saya tentang deadline?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I'll review it and reply by tomorrow.", "translation": "Ya, saya akan review dan balas besok."},
                    {"type": "phrase", "role": "Speaker", "en": "Please find the attached invoice.", "translation": "Silakan lihat lampiran invoice."},
                    {"type": "dialogue", "role": "A", "en": "Can you CC me on that email thread?", "translation": "Bisa kamu CC saya di thread email itu?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, I've added you to the CC list.", "translation": "Tentu, saya sudah tambahkan kamu ke CC."},
                    {"type": "phrase", "role": "Speaker", "en": "Thanks for your prompt response.", "translation": "Terima kasih atas respon cepatnya."},
                    {"type": "dialogue", "role": "A", "en": "I'm following up on my previous email.", "translation": "Saya follow up email saya sebelumnya."},
                    {"type": "dialogue", "role": "B", "en": "Apologies for the late reply. Here's my feedback.", "translation": "Maaf atas keterlambatan balasan. Ini feedback saya."},
                ]
            }
        ]
    },
    {
        "id": "finance",
        "name": "Finance English",
        "chapters": [
            {
                "chapter": "Accounting",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I need to reconcile the monthly expenses.", "translation": "Saya perlu merekonsiliasi pengeluaran bulanan."},
                    {"type": "dialogue", "role": "A", "en": "Can you send me the balance sheet?", "translation": "Bisa kirim saya balance sheet-nya?"},
                    {"type": "dialogue", "role": "B", "en": "I'll prepare it by end of business today.", "translation": "Saya akan siapkan sebelum akhir hari kerja."},
                    {"type": "phrase", "role": "Speaker", "en": "The profit and loss statement looks good.", "translation": "Laporan laba rugi terlihat bagus."},
                    {"type": "dialogue", "role": "A", "en": "What's our accounts receivable balance?", "translation": "Berapa saldo accounts receivable kita?"},
                    {"type": "dialogue", "role": "B", "en": "It's approximately two million rupiah.", "translation": "Kurang lebih dua juta rupiah."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll need the invoices sorted by date.", "translation": "Saya perlu invoice diurutkan berdasarkan tanggal."},
                    {"type": "dialogue", "role": "A", "en": "Did we close the books for last month?", "translation": "Sudahkah kita tutup buku bulan lalu?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, everything has been reconciled.", "translation": "Ya, semuanya sudah direkonsiliasi."},
                ]
            },
            {
                "chapter": "Investing",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'm diversifying my investment portfolio.", "translation": "Saya sedang mendiversifikasi portofolio investasi saya."},
                    {"type": "dialogue", "role": "A", "en": "Have you looked into index funds?", "translation": "Sudahkah kamu melihat reksa dana indeks?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I'm putting 30% of savings into them.", "translation": "Ya, saya alokasikan 30% tabungan ke situ."},
                    {"type": "phrase", "role": "Speaker", "en": "The return on investment was impressive this quarter.", "translation": "Return on investment trimester ini mengesankan."},
                    {"type": "dialogue", "role": "A", "en": "What's your risk tolerance?", "translation": "Seberapa besar toleransi risiko kamu?"},
                    {"type": "dialogue", "role": "B", "en": "I prefer low-risk investments at this point.", "translation": "Saya lebih suka investasi berisiko rendah saat ini."},
                    {"type": "phrase", "role": "Speaker", "en": "Do you invest in stocks or crypto?", "translation": "Kamu investasi di saham atau crypto?"},
                    {"type": "dialogue", "role": "A", "en": "The stock market has been volatile lately.", "translation": "Pasar saham akhir-akhir ini volatil."},
                    {"type": "dialogue", "role": "B", "en": "I'm holding long-term and not panicking.", "translation": "Saya hold jangka panjang dan tidak panik."},
                ]
            },
            {
                "chapter": "Banking",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I need to transfer funds to my business account.", "translation": "Saya perlu mentransfer dana ke rekening bisnis saya."},
                    {"type": "dialogue", "role": "A", "en": "Which bank do you use for your freelance income?", "translation": "Kamu pakai bank mana untuk penghasilan freelance?"},
                    {"type": "dialogue", "role": "B", "en": "I use Bank Mandiri for business and BCA for personal.", "translation": "Saya pakai Bank Mandiri untuk bisnis dan BCA untuk pribadi."},
                    {"type": "phrase", "role": "Speaker", "en": "The international transfer takes 2-3 business days.", "translation": "Transfer internasional membutuhkan 2-3 hari kerja."},
                    {"type": "dialogue", "role": "A", "en": "What's the exchange rate for USD to IDR today?", "translation": "Berapa kurs USD ke IDR hari ini?"},
                    {"type": "dialogue", "role": "B", "en": "It's around fifteen thousand per dollar.", "translation": "Sekitar lima belas ribu per dolar."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll set up automatic bill payments.", "translation": "Saya akan atur pembayaran tagihan otomatis."},
                    {"type": "dialogue", "role": "A", "en": "Do you have a business credit line?", "translation": "Kamu punya credit line bisnis?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it helps with cash flow management.", "translation": "Ya, ini membantu manajemen arus kas."},
                ]
            },
            {
                "chapter": "Budgeting",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'm creating a monthly budget for my startup.", "translation": "Saya sedang membuat anggaran bulanan untuk startup saya."},
                    {"type": "dialogue", "role": "A", "en": "What percentage of income goes to tools and software?", "translation": "Berapa persen penghasilan untuk tools dan software?"},
                    {"type": "dialogue", "role": "B", "en": "About 15% covers all my subscriptions.", "translation": "Sekitar 15% untuk semua langganan saya."},
                    {"type": "phrase", "role": "Speaker", "en": "We need to cut costs somewhere.", "translation": "Kita perlu mengurangi biaya di suatu tempat."},
                    {"type": "dialogue", "role": "A", "en": "How do you track your expenses?", "translation": "Bagaimana kamu melacak pengeluaran?"},
                    {"type": "dialogue", "role": "B", "en": "I use a spreadsheet and update it weekly.", "translation": "Saya pakai spreadsheet dan update tiap minggu."},
                    {"type": "phrase", "role": "Speaker", "en": "We're under budget this month, which is great.", "translation": "Kami di bawah anggaran bulan ini, bagus sekali."},
                    {"type": "dialogue", "role": "A", "en": "Should we allocate more to marketing?", "translation": "Haruskah kita alokasikan lebih banyak ke marketing?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, but only for high-ROI channels.", "translation": "Ya, tapi hanya untuk channel dengan ROI tinggi."},
                ]
            },
            {
                "chapter": "Reporting",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll prepare the quarterly financial report.", "translation": "Saya akan menyiapkan laporan keuangan trimester."},
                    {"type": "dialogue", "role": "A", "en": "Can you break down the revenue by source?", "translation": "Bisa kamu rincikan pendapatan berdasarkan sumber?"},
                    {"type": "dialogue", "role": "B", "en": "Freelance projects bring 60%, and SaaS is 40%.", "translation": "Proyek freelance membawa 60%, dan SaaS 40%."},
                    {"type": "phrase", "role": "Speaker", "en": "The cash flow report is ready for review.", "translation": "Laporan arus kas sudah siap untuk direview."},
                    {"type": "dialogue", "role": "A", "en": "What were our biggest expenses this quarter?", "translation": "Apa pengeluaran terbesar kami trimester ini?"},
                    {"type": "dialogue", "role": "B", "en": "Cloud hosting and contractor payments.", "translation": "Cloud hosting dan pembayaran kontraktor."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll include charts in the presentation.", "translation": "Saya akan sertakan grafik dalam presentasi."},
                    {"type": "dialogue", "role": "A", "en": "When is the board meeting to discuss finances?", "translation": "Kapan rapat dewan untuk membahas keuangan?"},
                    {"type": "dialogue", "role": "B", "en": "It's scheduled for Friday at 10 AM.", "translation": "Dijadwalkan hari Jumat jam 10 pagi."},
                ]
            }
        ]
    },
    {
        "id": "admin",
        "name": "Administration",
        "chapters": [
            {
                "chapter": "Scheduling",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Let me check my calendar for availability.", "translation": "Saya cek kalender saya dulu untuk ketersediaan."},
                    {"type": "dialogue", "role": "A", "en": "Can we reschedule the meeting to Thursday?", "translation": "Bisa kita reschedule meeting ke hari Kamis?"},
                    {"type": "dialogue", "role": "B", "en": "Thursday works for me. I'll update the invite.", "translation": "Kamis cocok untuk saya. Saya akan update undangannya."},
                    {"type": "phrase", "role": "Speaker", "en": "I've blocked off 2-4 PM for focused work.", "translation": "Saya sudah blokir jam 2-4 sore untuk kerja fokus."},
                    {"type": "dialogue", "role": "A", "en": "What time zone should we use for the meeting?", "translation": "Time zone mana yang harus kita pakai untuk meeting?"},
                    {"type": "dialogue", "role": "B", "en": "Let's use UTC to avoid confusion.", "translation": "Ayo pakai UTC agar tidak bingung."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll set up the recurring weekly sync.", "translation": "Saya akan atur sinkronisasi mingguan berulang."},
                    {"type": "dialogue", "role": "A", "en": "Do you have any conflicts next week?", "translation": "Apakah kamu ada konflik minggu depan?"},
                    {"type": "dialogue", "role": "B", "en": "Wednesday afternoon is open for me.", "translation": "Rabu sore kosong untuk saya."},
                ]
            },
            {
                "chapter": "Documentation",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I've updated the project documentation.", "translation": "Saya sudah update dokumentasi project."},
                    {"type": "dialogue", "role": "A", "en": "Where should we store the SOPs?", "translation": "Di mana kita simpan SOP-nya?"},
                    {"type": "dialogue", "role": "B", "en": "Let's keep them in the shared Google Drive.", "translation": "Ayo simpan di Google Drive bersama."},
                    {"type": "phrase", "role": "Speaker", "en": "Please fill out the onboarding checklist.", "translation": "Silakan isi checklist onboarding."},
                    {"type": "dialogue", "role": "A", "en": "I need the standard operating procedures.", "translation": "Saya butuh prosedur operasional standar."},
                    {"type": "dialogue", "role": "B", "en": "I'll send you the link to our knowledge base.", "translation": "Saya akan kirim link ke knowledge base kami."},
                    {"type": "phrase", "role": "Speaker", "en": "All contracts need to be filed digitally.", "translation": "Semua kontrak harus disimpan secara digital."},
                    {"type": "dialogue", "role": "A", "en": "Can you sign the digital document via DocuSign?", "translation": "Bisa kamu tanda tangan dokumen digital lewat DocuSign?"},
                    {"type": "dialogue", "role": "B", "en": "Done! I've signed and returned it.", "translation": "Selesai! Saya sudah tanda tangan dan kembalikan."},
                ]
            },
            {
                "chapter": "Correspondence",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll draft the response to the client.", "translation": "Saya akan buat draft balasan untuk klien."},
                    {"type": "dialogue", "role": "A", "en": "Can you CC the project manager on this email?", "translation": "Bisa kamu CC project manager di email ini?"},
                    {"type": "dialogue", "role": "B", "en": "Done. I've also included the team lead.", "translation": "Selesai. Saya juga sudah sertakan team lead."},
                    {"type": "phrase", "role": "Speaker", "en": "We need to send a formal letter of intent.", "translation": "Kita perlu mengirim surat niat resmi."},
                    {"type": "dialogue", "role": "A", "en": "The client is asking for a status update.", "translation": "Klien meminta update status."},
                    {"type": "dialogue", "role": "B", "en": "I'll prepare a summary and send it today.", "translation": "Saya akan siapkan ringkasan dan kirim hari ini."},
                    {"type": "phrase", "role": "Speaker", "en": "Please acknowledge receipt of this document.", "translation": "Silakan konfirmasi penerimaan dokumen ini."},
                    {"type": "dialogue", "role": "A", "en": "We should follow up on the proposal.", "translation": "Kita harus follow up proposal-nya."},
                    {"type": "dialogue", "role": "B", "en": "I'll send a polite reminder tomorrow.", "translation": "Saya akan kirim pengingat sopan besok."},
                ]
            },
            {
                "chapter": "Filing",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "All invoices are filed under the finance folder.", "translation": "Semua invoice disimpan di folder keuangan."},
                    {"type": "dialogue", "role": "A", "en": "Can you organize the shared drive folders?", "translation": "Bisa kamu atur folder di drive bersama?"},
                    {"type": "dialogue", "role": "B", "en": "I'll create a clear folder structure.", "translation": "Saya akan buat struktur folder yang jelas."},
                    {"type": "phrase", "role": "Speaker", "en": "Please scan and upload the signed contract.", "translation": "Silakan scan dan upload kontrak yang sudah ditandatangani."},
                    {"type": "dialogue", "role": "A", "en": "How do you name your files for easy search?", "translation": "Bagaimana kamu memberi nama file agar mudah dicari?"},
                    {"type": "dialogue", "role": "B", "en": "I use the format: date_client_project.", "translation": "Saya pakai format: tanggal_klien_project."},
                    {"type": "phrase", "role": "Speaker", "en": "We need a backup system for critical files.", "translation": "Kita butuh sistem backup untuk file penting."},
                    {"type": "dialogue", "role": "A", "en": "Are all the expense receipts archived?", "translation": "Apakah semua kuitansi pengeluaran sudah diarsipkan?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, they're organized by month and category.", "translation": "Ya, sudah diorganisir berdasarkan bulan dan kategori."},
                ]
            },
            {
                "chapter": "Reporting",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "The weekly status report is due on Friday.", "translation": "Laporan status mingguan harus selesai hari Jumat."},
                    {"type": "dialogue", "role": "A", "en": "Can you compile the team's progress updates?", "translation": "Bisa kamu kumpulkan update progres tim?"},
                    {"type": "dialogue", "role": "B", "en": "I'll gather the data from everyone's Slack updates.", "translation": "Saya akan ambil data dari update Slack semua orang."},
                    {"type": "phrase", "role": "Speaker", "en": "I've submitted the monthly activity report.", "translation": "Saya sudah mengirim laporan aktivitas bulanan."},
                    {"type": "dialogue", "role": "A", "en": "What format should the report follow?", "translation": "Format apa yang harus diikuti laporannya?"},
                    {"type": "dialogue", "role": "B", "en": "Use the standard template in the shared folder.", "translation": "Pakai template standar di folder bersama."},
                    {"type": "phrase", "role": "Speaker", "en": "The KPI dashboard is updated in real-time.", "translation": "Dashboard KPI diperbarui secara real-time."},
                    {"type": "dialogue", "role": "A", "en": "When is the quarterly review meeting?", "translation": "Kapan pertemuan review trimester?"},
                    {"type": "dialogue", "role": "B", "en": "It's next Monday at 9 AM.", "translation": "Senin depan jam 9 pagi."},
                ]
            }
        ]
    },
    {
        "id": "webdesign",
        "name": "Web Design",
        "chapters": [
            {
                "chapter": "Design Tools",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll create the mockup in Figma.", "translation": "Saya akan buat mockup di Figma."},
                    {"type": "dialogue", "role": "A", "en": "Are you using Figma or Adobe XD for this project?", "translation": "Kamu pakai Figma atau Adobe XD untuk project ini?"},
                    {"type": "dialogue", "role": "B", "en": "I prefer Figma for its collaboration features.", "translation": "Saya lebih suka Figma untuk fitur kolaborasinya."},
                    {"type": "phrase", "role": "Speaker", "en": "Let me export the assets in SVG format.", "translation": "Saya akan ekspor aset dalam format SVG."},
                    {"type": "dialogue", "role": "A", "en": "Can you share the Figma prototype link?", "translation": "Bisa share link prototype Figma-nya?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, I'll send the view-only link.", "translation": "Tentu, saya akan kirim link view-only."},
                    {"type": "phrase", "role": "Speaker", "en": "I use Canva for quick social media designs.", "translation": "Saya pakai Canva untuk desain media sosial cepat."},
                    {"type": "dialogue", "role": "A", "en": "What design system are you following?", "translation": "Design system apa yang kamu ikuti?"},
                    {"type": "dialogue", "role": "B", "en": "I'm building a custom design system in Figma.", "translation": "Saya sedang membangun design system custom di Figma."},
                ]
            },
            {
                "chapter": "Client Communication",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll present the initial concepts on Friday.", "translation": "Saya akan presentasikan konsep awal hari Jumat."},
                    {"type": "dialogue", "role": "A", "en": "What's your design process for a new project?", "translation": "Bagaimana proses desain kamu untuk project baru?"},
                    {"type": "dialogue", "role": "B", "en": "Research, wireframes, then high-fidelity mockups.", "translation": "Riset, wireframe, lalu mockup high-fidelity."},
                    {"type": "phrase", "role": "Speaker", "en": "Let's schedule a walkthrough of the design.", "translation": "Ayo jadwalkan walkthrough desainnya."},
                    {"type": "dialogue", "role": "A", "en": "Can you give me a timeline for the redesign?", "translation": "Bisa beri saya timeline untuk redesain?"},
                    {"type": "dialogue", "role": "B", "en": "About 3 weeks from concept to final delivery.", "translation": "Sekitar 3 minggu dari konsep ke pengiriman final."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll incorporate your feedback into the next revision.", "translation": "Saya akan masukkan feedback Anda ke revisi berikutnya."},
                    {"type": "dialogue", "role": "A", "en": "The client wants a more modern look.", "translation": "Klien ingin tampilan yang lebih modern."},
                    {"type": "dialogue", "role": "B", "en": "I'll update the style guide accordingly.", "translation": "Saya akan update style guide sesuai permintaan."},
                ]
            },
            {
                "chapter": "Portfolio",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I need to update my portfolio website.", "translation": "Saya perlu update website portfolio saya."},
                    {"type": "dialogue", "role": "A", "en": "What's the best way to showcase your work?", "translation": "Cara terbaik untuk memamerkan karya kamu?"},
                    {"type": "dialogue", "role": "B", "en": "I use case studies with before-and-after shots.", "translation": "Saya pakai studi kasus dengan foto sebelum dan sesudah."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll add the new project to my Behance page.", "translation": "Saya akan tambahkan project baru ke halaman Behance saya."},
                    {"type": "dialogue", "role": "A", "en": "Do you include client testimonials in your portfolio?", "translation": "Kamu sertakan testimonial klien di portfolio?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, social proof is very important.", "translation": "Ya, bukti sosial sangat penting."},
                    {"type": "phrase", "role": "Speaker", "en": "My portfolio is hosted on Webflow.", "translation": "Portfolio saya dihost di Webflow."},
                    {"type": "dialogue", "role": "A", "en": "How often should you update your portfolio?", "translation": "Seberapa sering kamu harus update portfolio?"},
                    {"type": "dialogue", "role": "B", "en": "I try to update it quarterly with new projects.", "translation": "Saya coba update tiap trimester dengan project baru."},
                ]
            },
            {
                "chapter": "Feedback",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Can you give me specific feedback on the layout?", "translation": "Bisa beri feedback spesifik tentang layout-nya?"},
                    {"type": "dialogue", "role": "A", "en": "The color palette feels a bit too bright.", "translation": "Palet warnanya terasa sedikit terlalu terang."},
                    {"type": "dialogue", "role": "B", "en": "I'll tone it down and use softer tones.", "translation": "Saya akan redam dan pakai warna lebih lembut."},
                    {"type": "phrase", "role": "Speaker", "en": "I'd suggest making the CTA button more prominent.", "translation": "Saya sarankan buat tombol CTA lebih menonjol."},
                    {"type": "dialogue", "role": "A", "en": "The typography needs to be more readable.", "translation": "Tipografi perlu lebih mudah dibaca."},
                    {"type": "dialogue", "role": "B", "en": "I'll increase the font size and line height.", "translation": "Saya akan perbesar ukuran font dan line height."},
                    {"type": "phrase", "role": "Speaker", "en": "Your feedback has improved the design significantly.", "translation": "Feedback Anda telah meningkatkan desain secara signifikan."},
                    {"type": "dialogue", "role": "A", "en": "What do you think about the spacing?", "translation": "Menurutmu bagaimana spacing-nya?"},
                    {"type": "dialogue", "role": "B", "en": "It looks great, nice use of white space.", "translation": "Terlihat bagus, penggunaan white space yang baik."},
                ]
            },
            {
                "chapter": "Specifications",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "The design should be responsive across all devices.", "translation": "Desain harus responsif di semua perangkat."},
                    {"type": "dialogue", "role": "A", "en": "What's the required screen resolution?", "translation": "Berapa resolusi layar yang dibutuhkan?"},
                    {"type": "dialogue", "role": "B", "en": "We need to support 1920x1080 down to 375px mobile.", "translation": "Kita harus mendukung 1920x1080 hingga 375px mobile."},
                    {"type": "phrase", "role": "Speaker", "en": "Please follow the brand guidelines strictly.", "translation": "Silakan ikuti panduan brand secara ketat."},
                    {"type": "dialogue", "role": "A", "en": "What file formats do you need for handoff?", "translation": "Format file apa yang kamu butuhkan untuk handoff?"},
                    {"type": "dialogue", "role": "B", "en": "SVG for icons and PNG for images.", "translation": "SVG untuk ikon dan PNG untuk gambar."},
                    {"type": "phrase", "role": "Speaker", "en": "The accessibility standards must be WCAG 2.1 AA.", "translation": "Standar aksesibilitas harus WCAG 2.1 AA."},
                    {"type": "dialogue", "role": "A", "en": "Does this need to integrate with a CMS?", "translation": "Apakah ini perlu terintegrasi dengan CMS?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, the client wants WordPress integration.", "translation": "Ya, klien ingin integrasi WordPress."},
                ]
            }
        ]
    },
    {
        "id": "seo",
        "name": "SEO Specialist",
        "chapters": [
            {
                "chapter": "Analytics",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Organic traffic increased by 25% this month.", "translation": "Traffic organik meningkat 25% bulan ini."},
                    {"type": "dialogue", "role": "A", "en": "What does the Google Analytics data show?", "translation": "Apa data Google Analytics menunjukkan?"},
                    {"type": "dialogue", "role": "B", "en": "Bounce rate is down and session duration is up.", "translation": "Bounce rate turun dan durasi sesi naik."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll set up a custom dashboard in GA4.", "translation": "Saya akan buat dashboard custom di GA4."},
                    {"type": "dialogue", "role": "A", "en": "Which pages are getting the most traffic?", "translation": "Halaman mana yang mendapat traffic paling banyak?"},
                    {"type": "dialogue", "role": "B", "en": "The blog posts about tutorials perform best.", "translation": "Artikel blog tentang tutorial paling perform."},
                    {"type": "phrase", "role": "Speaker", "en": "Let's track conversions from organic search.", "translation": "Ayo lacak konversi dari pencarian organik."},
                    {"type": "dialogue", "role": "A", "en": "Can you pull the monthly SEO report?", "translation": "Bisa ambil laporan SEO bulanan?"},
                    {"type": "dialogue", "role": "B", "en": "It's ready. I'll share it on the dashboard.", "translation": "Sudah siap. Saya akan bagikan di dashboard."},
                ]
            },
            {
                "chapter": "Keywords",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "We should target long-tail keywords for better ranking.", "translation": "Kita harus target keyword long-tail untuk ranking lebih baik."},
                    {"type": "dialogue", "role": "A", "en": "What keyword research tools do you use?", "translation": "Tools riset keyword apa yang kamu pakai?"},
                    {"type": "dialogue", "role": "B", "en": "Ahrefs and Google Keyword Planner.", "translation": "Ahrefs dan Google Keyword Planner."},
                    {"type": "phrase", "role": "Speaker", "en": "The keyword difficulty is too high for new sites.", "translation": "Kesulitan keyword terlalu tinggi untuk situs baru."},
                    {"type": "dialogue", "role": "A", "en": "How many keywords should we target per page?", "translation": "Berapa banyak keyword yang harus kita target per halaman?"},
                    {"type": "dialogue", "role": "B", "en": "One primary keyword and 3-5 secondary ones.", "translation": "Satu keyword utama dan 3-5 keyword sekunder."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll optimize the meta descriptions with target keywords.", "translation": "Saya akan optimasi meta deskripsi dengan keyword target."},
                    {"type": "dialogue", "role": "A", "en": "What's the search intent behind these keywords?", "translation": "Apa search intent di balik keyword-keyword ini?"},
                    {"type": "dialogue", "role": "B", "en": "Mostly informational and commercial intent.", "translation": "Kebanyakan intent informatif dan komersial."},
                ]
            },
            {
                "chapter": "Technical SEO",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "The site needs a proper sitemap.xml.", "translation": "Situs butuh sitemap.xml yang benar."},
                    {"type": "dialogue", "role": "A", "en": "Is the website loading fast enough?", "translation": "Apakah website cukup cepat dimuat?"},
                    {"type": "dialogue", "role": "B", "en": "Core Web Vitals are passing on all pages.", "translation": "Core Web Vitals lulus di semua halaman."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll fix the crawl errors in Search Console.", "translation": "Saya akan perbaiki error crawling di Search Console."},
                    {"type": "dialogue", "role": "A", "en": "Do we need to implement structured data?", "translation": "Apakah kita perlu menerapkan structured data?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, Article schema will help with rich snippets.", "translation": "Ya, schema Article akan membantu dengan rich snippet."},
                    {"type": "phrase", "role": "Speaker", "en": "The site is now fully HTTPS with no mixed content.", "translation": "Situs sekarang sepenuhnya HTTPS tanpa mixed content."},
                    {"type": "dialogue", "role": "A", "en": "Are there any broken links on the site?", "translation": "Apakah ada link rusak di situs?"},
                    {"type": "dialogue", "role": "B", "en": "I found 12 and I'm redirecting them now.", "translation": "Saya menemukan 12 dan saya sedang redirect sekarang."},
                ]
            },
            {
                "chapter": "SEO Reporting",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll prepare the monthly SEO performance report.", "translation": "Saya akan menyiapkan laporan performa SEO bulanan."},
                    {"type": "dialogue", "role": "A", "en": "What metrics should be included in the report?", "translation": "Metrik apa yang harus disertakan dalam laporan?"},
                    {"type": "dialogue", "role": "B", "en": "Traffic, rankings, backlinks, and conversions.", "translation": "Traffic, ranking, backlink, dan konversi."},
                    {"type": "phrase", "role": "Speaker", "en": "We gained 15 new backlinks this month.", "translation": "Kita mendapatkan 15 backlink baru bulan ini."},
                    {"type": "dialogue", "role": "A", "en": "How does our traffic compare to last month?", "translation": "Bagaimana traffic kita dibandingkan bulan lalu?"},
                    {"type": "dialogue", "role": "B", "en": "It's up 18% overall and 30% from organic.", "translation": "Naik 18% secara keseluruhan dan 30% dari organik."},
                    {"type": "phrase", "role": "Speaker", "en": "The report is available on our shared Google Sheet.", "translation": "Laporan tersedia di Google Sheet bersama kami."},
                    {"type": "dialogue", "role": "A", "en": "Can you visualize the data with charts?", "translation": "Bisa kamu visualisasikan data dengan grafik?"},
                    {"type": "dialogue", "role": "B", "en": "I'll add line graphs and bar charts.", "translation": "Saya akan tambahkan grafik garis dan batang."},
                ]
            },
            {
                "chapter": "SEO Strategy",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "We need a content strategy for the blog.", "translation": "Kita butuh strategi konten untuk blog."},
                    {"type": "dialogue", "role": "A", "en": "Should we focus on link building or content first?", "translation": "Harusnya kita fokus link building atau konten dulu?"},
                    {"type": "dialogue", "role": "B", "en": "Content first, then build links to it.", "translation": "Konten dulu, baru bangun link ke situ."},
                    {"type": "phrase", "role": "Speaker", "en": "Let's create a topic cluster strategy.", "translation": "Ayo buat strategi topic cluster."},
                    {"type": "dialogue", "role": "A", "en": "How often should we publish new content?", "translation": "Seberapa sering kita harus publish konten baru?"},
                    {"type": "dialogue", "role": "B", "en": "At least two quality articles per week.", "translation": "Minimal dua artikel berkualitas per minggu."},
                    {"type": "phrase", "role": "Speaker", "en": "We should optimize existing content before creating new.", "translation": "Kita harus optimasi konten yang ada sebelum buat baru."},
                    {"type": "dialogue", "role": "A", "en": "What's our main SEO goal for this quarter?", "translation": "Apa tujuan SEO utama kita trimester ini?"},
                    {"type": "dialogue", "role": "B", "en": "Increase organic traffic by 40% and rank top 5 for key terms.", "translation": "Tingkatkan traffic organik 40% dan ranking top 5 untuk kata kunci utama."},
                ]
            }
        ]
    },
    {
        "id": "graphic-design",
        "name": "Graphic Design",
        "chapters": [
            {
                "chapter": "Design Brief",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Can you share the design brief for the new brand?", "translation": "Bisa share design brief untuk brand baru?"},
                    {"type": "dialogue", "role": "A", "en": "What's the target audience for this design?", "translation": "Siapa target audiens untuk desain ini?"},
                    {"type": "dialogue", "role": "B", "en": "Young professionals aged 25-35.", "translation": "Profesional muda berusia 25-35 tahun."},
                    {"type": "phrase", "role": "Speaker", "en": "I need more details about the project goals.", "translation": "Saya butuh detail lebih banyak tentang tujuan project."},
                    {"type": "dialogue", "role": "A", "en": "Do you have any reference designs we like?", "translation": "Apakah ada desain referensi yang kita suka?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I've pinned some on our Pinterest board.", "translation": "Ya, saya sudah pin beberapa di papan Pinterest kami."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll start with mood boards based on the brief.", "translation": "Saya akan mulai dengan mood board berdasarkan brief."},
                    {"type": "dialogue", "role": "A", "en": "What's the deadline for the first draft?", "translation": "Berapa deadline untuk draft pertama?"},
                    {"type": "dialogue", "role": "B", "en": "We need it by end of next week.", "translation": "Kita butuh akhir minggu depan."},
                ]
            },
            {
                "chapter": "Branding",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll design a new logo for the company.", "translation": "Saya akan desain logo baru untuk perusahaan."},
                    {"type": "dialogue", "role": "A", "en": "What feeling should the brand convey?", "translation": "Perasaan apa yang harus disampaikan brand?"},
                    {"type": "dialogue", "role": "B", "en": "Professional, trustworthy, and innovative.", "translation": "Profesional, terpercaya, dan inovatif."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll create a brand style guide.", "translation": "Saya akan buat brand style guide."},
                    {"type": "dialogue", "role": "A", "en": "Should the logo be minimalist or detailed?", "translation": "Apakah logo harus minimalis atau detail?"},
                    {"type": "dialogue", "role": "B", "en": "We prefer a clean, modern look.", "translation": "Kami lebih suka tampilan bersih dan modern."},
                    {"type": "phrase", "role": "Speaker", "en": "The brand colors are blue and white.", "translation": "Warna brand adalah biru dan putih."},
                    {"type": "dialogue", "role": "A", "en": "Can we see logo variations for different uses?", "translation": "Bisa kita lihat variasi logo untuk penggunaan berbeda?"},
                    {"type": "dialogue", "role": "B", "en": "I'll prepare versions for print and digital.", "translation": "Saya akan siapkan versi untuk cetak dan digital."},
                ]
            },
            {
                "chapter": "Typography",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I recommend using a sans-serif font for the UI.", "translation": "Saya sarankan pakai font sans-serif untuk UI."},
                    {"type": "dialogue", "role": "A", "en": "What font pairings work well together?", "translation": "Pasangan font apa yang cocok bersama?"},
                    {"type": "dialogue", "role": "B", "en": "Montserrat for headings and Open Sans for body.", "translation": "Montserrat untuk judul dan Open Sans untuk body."},
                    {"type": "phrase", "role": "Speaker", "en": "The line height should be 1.5 for readability.", "translation": "Line height harus 1.5 untuk keterbacaan."},
                    {"type": "dialogue", "role": "A", "en": "Should we use web-safe fonts or custom ones?", "translation": "Harusnya kita pakai font web-safe atau custom?"},
                    {"type": "dialogue", "role": "B", "en": "Google Fonts for performance, custom for brand.", "translation": "Google Fonts untuk performa, custom untuk brand."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll set up a typography scale for consistency.", "translation": "Saya akan buat skala tipografi untuk konsistensi."},
                    {"type": "dialogue", "role": "A", "en": "The font size seems too small on mobile.", "translation": "Ukuran font sepertinya terlalu kecil di mobile."},
                    {"type": "dialogue", "role": "B", "en": "I'll bump it up to at least 16px.", "translation": "Saya akan naikkan minimal 16px."},
                ]
            },
            {
                "chapter": "Color Theory",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "The color palette should match the brand identity.", "translation": "Palet warna harus sesuai dengan identitas brand."},
                    {"type": "dialogue", "role": "A", "en": "What colors evoke trust and reliability?", "translation": "Warna apa yang memunculkan kepercayaan dan keandalan?"},
                    {"type": "dialogue", "role": "B", "en": "Blue is the most common choice for trust.", "translation": "Biru adalah pilihan paling umum untuk kepercayaan."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll use complementary colors for contrast.", "translation": "Saya akan pakai warna komplementer untuk kontras."},
                    {"type": "dialogue", "role": "A", "en": "Are these colors accessible for color-blind users?", "translation": "Apakah warna ini aksesibel untuk pengguna buta warna?"},
                    {"type": "dialogue", "role": "B", "en": "I'll check the contrast ratio with a tool.", "translation": "Saya akan cek rasio kontras dengan tools."},
                    {"type": "phrase", "role": "Speaker", "en": "I've created a 5-color palette for the design.", "translation": "Saya sudah buat palet 5 warna untuk desain."},
                    {"type": "dialogue", "role": "A", "en": "Can we see how it looks in light and dark mode?", "translation": "Bisa kita lihat tampilan di light dan dark mode?"},
                    {"type": "dialogue", "role": "B", "en": "I'll prepare mockups for both themes.", "translation": "Saya akan siapkan mockup untuk kedua tema."},
                ]
            },
            {
                "chapter": "Client Work",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll send the deliverables in the agreed formats.", "translation": "Saya akan kirim hasil kerja dalam format yang disepakati."},
                    {"type": "dialogue", "role": "A", "en": "Can you provide the source files along with exports?", "translation": "Bisa kamu berikan source file beserta ekspor?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I'll include AI, PSD, and SVG files.", "translation": "Ya, saya akan sertakan file AI, PSD, dan SVG."},
                    {"type": "phrase", "role": "Speaker", "en": "I've completed the third revision as requested.", "translation": "Saya sudah selesaikan revisi ketiga sesuai permintaan."},
                    {"type": "dialogue", "role": "A", "en": "How many revision rounds are included?", "translation": "Berapa ronde revisi yang termasuk?"},
                    {"type": "dialogue", "role": "B", "en": "Two rounds are standard, additional ones are charged.", "translation": "Dua ronde standar, yang lebih dikenakan biaya."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll watermark the preview images.", "translation": "Saya akan beri watermark pada gambar preview."},
                    {"type": "dialogue", "role": "A", "en": "When will the final files be ready?", "translation": "Kapan file final akan siap?"},
                    {"type": "dialogue", "role": "B", "en": "I'll have everything ready by Wednesday.", "translation": "Saya akan selesaikan semuanya hari Rabu."},
                ]
            }
        ]
    },
    {
        "id": "video-editing",
        "name": "Video Editing",
        "chapters": [
            {
                "chapter": "Editing Terms",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll do a rough cut first, then refine.", "translation": "Saya akan buat rough cut dulu, lalu perbaiki."},
                    {"type": "dialogue", "role": "A", "en": "Can you add some B-roll footage here?", "translation": "Bisa kamu tambahkan footage B-roll di sini?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, I'll overlay it with the interview.", "translation": "Tentu, saya akan overlay dengan wawancara."},
                    {"type": "phrase", "role": "Speaker", "en": "I need to color grade the footage.", "translation": "Saya perlu color grade footage-nya."},
                    {"type": "dialogue", "role": "A", "en": "What's the desired look and feel?", "translation": "Tampilan dan nuansa yang diinginkan seperti apa?"},
                    {"type": "dialogue", "role": "B", "en": "Warm tones, cinematic feel.", "translation": "Nada hangat, nuansa sinematik."},
                    {"type": "phrase", "role": "Speaker", "en": "The jump cuts need to be smoother.", "translation": "Jump cut-nya perlu lebih halus."},
                    {"type": "dialogue", "role": "A", "en": "Can we add transitions between scenes?", "translation": "Bisa kita tambahkan transisi antar adegan?"},
                    {"type": "dialogue", "role": "B", "en": "I'll use subtle cross-dissolves.", "translation": "Saya akan pakai cross-dissolve yang halus."},
                ]
            },
            {
                "chapter": "Client Brief",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "What's the target length for the video?", "translation": "Panjang target video berapa?"},
                    {"type": "dialogue", "role": "A", "en": "The client wants a 3-minute promotional video.", "translation": "Klien ingin video promosi 3 menit."},
                    {"type": "dialogue", "role": "B", "en": "I'll keep it punchy with strong visuals.", "translation": "Saya akan buat padat dengan visual kuat."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll use the footage shot on location.", "translation": "Saya akan pakai footage yang diambil di lokasi."},
                    {"type": "dialogue", "role": "A", "en": "Do you need the raw footage or edited clips?", "translation": "Kamu butuh footage mentah atau klip yang sudah diedit?"},
                    {"type": "dialogue", "role": "B", "en": "Raw footage gives me more flexibility.", "translation": "Footage mentah memberi saya lebih banyak fleksibilitas."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll add subtitles in English and Indonesian.", "translation": "Saya akan tambahkan subtitle dalam bahasa Inggris dan Indonesia."},
                    {"type": "dialogue", "role": "A", "en": "What resolution should the final export be?", "translation": "Resolusi apa untuk ekspor final?"},
                    {"type": "dialogue", "role": "B", "en": "4K for the main file, 1080p for social media.", "translation": "4K untuk file utama, 1080p untuk media sosial."},
                ]
            },
            {
                "chapter": "Equipment",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I use a MacBook Pro for editing.", "translation": "Saya pakai MacBook Pro untuk editing."},
                    {"type": "dialogue", "role": "A", "en": "Do you use an external hard drive for storage?", "translation": "Kamu pakai hard drive eksternal untuk penyimpanan?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I have a 4TB SSD for all my projects.", "translation": "Ya, saya punya SSD 4TB untuk semua project saya."},
                    {"type": "phrase", "role": "Speaker", "en": "A good microphone is essential for quality audio.", "translation": "Mic yang bagus sangat penting untuk audio berkualitas."},
                    {"type": "dialogue", "role": "A", "en": "What camera do you use for shooting?", "translation": "Kamera apa yang kamu pakai untuk syuting?"},
                    {"type": "dialogue", "role": "B", "en": "I use a Sony A7III for most projects.", "translation": "Saya pakai Sony A7III untuk kebanyakan project."},
                    {"type": "phrase", "role": "Speaker", "en": "I have a dual monitor setup for efficient editing.", "translation": "Saya punya setup dual monitor untuk editing efisien."},
                    {"type": "dialogue", "role": "A", "en": "How much RAM do you recommend for video editing?", "translation": "Berapa RAM yang kamu rekomendasikan untuk editing video?"},
                    {"type": "dialogue", "role": "B", "en": "At least 32GB for smooth 4K editing.", "translation": "Minimal 32GB untuk editing 4K yang lancar."},
                ]
            },
            {
                "chapter": "Software",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I primarily use Adobe Premiere Pro.", "translation": "Saya terutama pakai Adobe Premiere Pro."},
                    {"type": "dialogue", "role": "A", "en": "Have you tried DaVinci Resolve for color grading?", "translation": "Sudah coba DaVinci Resolve untuk color grading?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it's excellent for color work.", "translation": "Ya, sangat bagus untuk pekerjaan warna."},
                    {"type": "phrase", "role": "Speaker", "en": "I use After Effects for motion graphics.", "translation": "Saya pakai After Effects untuk motion graphics."},
                    {"type": "dialogue", "role": "A", "en": "What plugins do you use for editing?", "translation": "Plugin apa yang kamu pakai untuk editing?"},
                    {"type": "dialogue", "role": "B", "en": "FilmConvert for color and Neat Video for denoising.", "translation": "FilmConvert untuk warna dan Neat Video untuk denoising."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll render the video in H.264 for compatibility.", "translation": "Saya akan render video dalam H.264 untuk kompatibilitas."},
                    {"type": "dialogue", "role": "A", "en": "Do you use proxy editing for large files?", "translation": "Kamu pakai proxy editing untuk file besar?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it makes the editing process much smoother.", "translation": "Ya, membuat proses editing jauh lebih lancar."},
                ]
            },
            {
                "chapter": "Delivery",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll upload the final video to Google Drive.", "translation": "Saya akan upload video final ke Google Drive."},
                    {"type": "dialogue", "role": "A", "en": "What format should the final deliverable be?", "translation": "Format apa yang harus untuk hasil akhir?"},
                    {"type": "dialogue", "role": "B", "en": "MP4 H.264 with AAC audio.", "translation": "MP4 H.264 dengan audio AAC."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll create separate versions for social platforms.", "translation": "Saya akan buat versi terpisah untuk platform sosial."},
                    {"type": "dialogue", "role": "A", "en": "Do you provide a preview before final delivery?", "translation": "Kamu berikan preview sebelum pengiriman final?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I'll share a watermarked preview first.", "translation": "Ya, saya akan share preview dengan watermark dulu."},
                    {"type": "phrase", "role": "Speaker", "en": "The final file will be delivered via WeTransfer.", "translation": "File final akan dikirim via WeTransfer."},
                    {"type": "dialogue", "role": "A", "en": "Can you compress the file without losing quality?", "translation": "Bisa kamu kompres file tanpa kehilangan kualitas?"},
                    {"type": "dialogue", "role": "B", "en": "I'll optimize the bitrate for the best balance.", "translation": "Saya akan optimasi bitrate untuk keseimbangan terbaik."},
                ]
            }
        ]
    },
    {
        "id": "virtual-assistant",
        "name": "Virtual Assistant",
        "chapters": [
            {
                "chapter": "Email Management",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll sort your inbox by priority.", "translation": "Saya akan urutkan inbox Anda berdasarkan prioritas."},
                    {"type": "dialogue", "role": "A", "en": "Can you draft a response to this client email?", "translation": "Bisa kamu buat draft balasan untuk email klien ini?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, I'll have it ready in 10 minutes.", "translation": "Tentu, saya akan selesaikan dalam 10 menit."},
                    {"type": "phrase", "role": "Speaker", "en": "I've filtered the emails into categories.", "translation": "Saya sudah filter email ke dalam kategori."},
                    {"type": "dialogue", "role": "A", "en": "How many unread emails do I have?", "translation": "Berapa banyak email belum dibaca saya?"},
                    {"type": "dialogue", "role": "B", "en": "There are 23 unread, but only 5 need action.", "translation": "Ada 23 belum dibaca, tapi hanya 5 yang perlu tindakan."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll set up email filters to reduce spam.", "translation": "Saya akan atur filter email untuk kurangi spam."},
                    {"type": "dialogue", "role": "A", "en": "Can you follow up on the pending replies?", "translation": "Bisa kamu follow up balasan yang tertunda?"},
                    {"type": "dialogue", "role": "B", "en": "Done, I've sent follow-ups to 3 contacts.", "translation": "Selesai, saya sudah kirim follow-up ke 3 kontak."},
                ]
            },
            {
                "chapter": "Scheduling",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll manage your Google Calendar.", "translation": "Saya akan mengelola Google Calendar Anda."},
                    {"type": "dialogue", "role": "A", "en": "Do I have any meetings tomorrow?", "translation": "Apakah saya ada meeting besok?"},
                    {"type": "dialogue", "role": "B", "en": "You have two: a standup at 9 AM and a client call at 2 PM.", "translation": "Anda punya dua: standup jam 9 pagi dan panggilan klien jam 2 sore."},
                    {"type": "phrase", "role": "Speaker", "en": "I've blocked your focus time from 10-12.", "translation": "Saya sudah blokir waktu fokus Anda dari jam 10-12."},
                    {"type": "dialogue", "role": "A", "en": "Can you schedule a meeting with the developer?", "translation": "Bisa kamu jadwalkan meeting dengan developer?"},
                    {"type": "dialogue", "role": "B", "en": "Sure, what time works best for you?", "translation": "Tentu, jam berapa yang paling cocok untuk Anda?"},
                    {"type": "phrase", "role": "Speaker", "en": "I'll send calendar invites for all meetings.", "translation": "Saya akan kirim undangan kalender untuk semua meeting."},
                    {"type": "dialogue", "role": "A", "en": "I need to reschedule my afternoon meetings.", "translation": "Saya perlu reschedule meeting sore saya."},
                    {"type": "dialogue", "role": "B", "en": "I'll move them to next week.", "translation": "Saya akan pindahkan ke minggu depan."},
                ]
            },
            {
                "chapter": "Data Entry",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll input all the contact information.", "translation": "Saya akan masukkan semua informasi kontak."},
                    {"type": "dialogue", "role": "A", "en": "Can you update the customer database?", "translation": "Bisa kamu update database pelanggan?"},
                    {"type": "dialogue", "role": "B", "en": "I'll add the 50 new entries today.", "translation": "Saya akan tambahkan 50 entri baru hari ini."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll double-check all the data for accuracy.", "translation": "Saya akan periksa ulang semua data untuk akurasi."},
                    {"type": "dialogue", "role": "A", "en": "How fast can you enter these records?", "translation": "Seberapa cepat kamu bisa masukkan catatan ini?"},
                    {"type": "dialogue", "role": "B", "en": "I can handle about 200 entries per hour.", "translation": "Saya bisa handle sekitar 200 entri per jam."},
                    {"type": "phrase", "role": "Speaker", "en": "The spreadsheet has been updated.", "translation": "Spreadsheet sudah diupdate."},
                    {"type": "dialogue", "role": "A", "en": "Can you transfer this data to our CRM?", "translation": "Bisa kamu transfer data ini ke CRM kami?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I'll import it via CSV.", "translation": "Ya, saya akan import lewat CSV."},
                ]
            },
            {
                "chapter": "Customer Service",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll respond to customer inquiries promptly.", "translation": "Saya akan merespons pertanyaan pelanggan dengan cepat."},
                    {"type": "dialogue", "role": "A", "en": "Can you handle the live chat support?", "translation": "Bisa kamu tangani live chat support?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I'll monitor it during business hours.", "translation": "Ya, saya akan pantau selama jam kerja."},
                    {"type": "phrase", "role": "Speaker", "en": "I've created FAQ templates for common questions.", "translation": "Saya sudah buat template FAQ untuk pertanyaan umum."},
                    {"type": "dialogue", "role": "A", "en": "How do you handle difficult customers?", "translation": "Bagaimana kamu menangani pelanggan yang sulit?"},
                    {"type": "dialogue", "role": "B", "en": "I stay calm, listen actively, and offer solutions.", "translation": "Saya tetap tenang, mendengarkan aktif, dan tawarkan solusi."},
                    {"type": "phrase", "role": "Speaker", "en": "All tickets have been resolved.", "translation": "Semua tiket sudah diselesaikan."},
                    {"type": "dialogue", "role": "A", "en": "What's our average response time?", "translation": "Berapa waktu respons rata-rata kita?"},
                    {"type": "dialogue", "role": "B", "en": "It's under 2 hours, which is great.", "translation": "Di bawah 2 jam, yang sangat bagus."},
                ]
            },
            {
                "chapter": "Social Media",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll schedule posts on all platforms.", "translation": "Saya akan jadwalkan postingan di semua platform."},
                    {"type": "dialogue", "role": "A", "en": "Can you create content for our Instagram?", "translation": "Bisa kamu buat konten untuk Instagram kami?"},
                    {"type": "dialogue", "role": "B", "en": "I'll prepare a week's worth of content.", "translation": "Saya akan siapkan konten untuk satu minggu."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll respond to comments and DMs.", "translation": "Saya akan merespons komentar dan DM."},
                    {"type": "dialogue", "role": "A", "en": "What posting schedule do you recommend?", "translation": "Jadwal posting apa yang kamu rekomendasikan?"},
                    {"type": "dialogue", "role": "B", "en": "Daily on Instagram, 3 times a week on LinkedIn.", "translation": "Tiap hari di Instagram, 3 kali seminggu di LinkedIn."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll use Buffer to manage all accounts.", "translation": "Saya akan pakai Buffer untuk mengelola semua akun."},
                    {"type": "dialogue", "role": "A", "en": "Can you track our social media analytics?", "translation": "Bisa kamu lacak analitik media sosial kami?"},
                    {"type": "dialogue", "role": "B", "en": "I'll provide a weekly report with key metrics.", "translation": "Saya akan berikan laporan mingguan dengan metrik kunci."},
                ]
            }
        ]
    },
    {
        "id": "copywriting",
        "name": "Copywriting",
        "chapters": [
            {
                "chapter": "Sales Copy",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll write compelling sales copy for the landing page.", "translation": "Saya akan tulis sales copy yang menarik untuk landing page."},
                    {"type": "dialogue", "role": "A", "en": "What's the main benefit of this product?", "translation": "Apa manfaat utama produk ini?"},
                    {"type": "dialogue", "role": "B", "en": "It saves developers 10 hours per week.", "translation": "Ini menghemat waktu developer 10 jam per minggu."},
                    {"type": "phrase", "role": "Speaker", "en": "The headline needs to grab attention immediately.", "translation": "Headline harus menarik perhatian segera."},
                    {"type": "dialogue", "role": "A", "en": "Can you write a call to action that converts?", "translation": "Bisa kamu tulis call to action yang mengkonversi?"},
                    {"type": "dialogue", "role": "B", "en": "I'll A/B test a few variations.", "translation": "Saya akan A/B test beberapa variasi."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll focus on pain points and solutions.", "translation": "Saya akan fokus pada titik masalah dan solusi."},
                    {"type": "dialogue", "role": "A", "en": "What tone should the sales copy have?", "translation": "Nada apa yang harus dimiliki sales copy?"},
                    {"type": "dialogue", "role": "B", "en": "Professional but approachable.", "translation": "Profesional tapi mudah didekati."},
                ]
            },
            {
                "chapter": "Landing Pages",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll optimize the landing page for conversions.", "translation": "Saya akan optimasi landing page untuk konversi."},
                    {"type": "dialogue", "role": "A", "en": "What elements should a high-converting page have?", "translation": "Elemen apa yang harus dimiliki halaman konversi tinggi?"},
                    {"type": "dialogue", "role": "B", "en": "Strong headline, social proof, and clear CTA.", "translation": "Headline kuat, bukti sosial, dan CTA jelas."},
                    {"type": "phrase", "role": "Speaker", "en": "The hero section needs a powerful value proposition.", "translation": "Bagian hero butuh value proposition yang kuat."},
                    {"type": "dialogue", "role": "A", "en": "Should we include testimonials on the page?", "translation": "Haruskah kita sertakan testimonial di halaman?"},
                    {"type": "dialogue", "role": "B", "en": "Absolutely, they build trust immediately.", "translation": "Pasti, mereka membangun kepercayaan segera."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll write the copy above the fold.", "translation": "Saya akan tulis copy di atas fold."},
                    {"type": "dialogue", "role": "A", "en": "How long should the landing page be?", "translation": "Seberapa panjang landing page seharusnya?"},
                    {"type": "dialogue", "role": "B", "en": "Long enough to address all objections.", "translation": "Cukup panjang untuk mengatasi semua keberatan."},
                ]
            },
            {
                "chapter": "Email Marketing",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll create an email drip campaign.", "translation": "Saya akan buat kampanye email drip."},
                    {"type": "dialogue", "role": "A", "en": "What's a good subject line for high open rates?", "translation": "Apa subject line yang bagus untuk open rate tinggi?"},
                    {"type": "dialogue", "role": "B", "en": "Keep it short, personal, and curiosity-driven.", "translation": "Buat singkat, personal, dan memancing rasa penasaran."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll segment the email list for targeted messaging.", "translation": "Saya akan segmentasi daftar email untuk pesan yang terarah."},
                    {"type": "dialogue", "role": "A", "en": "How many emails should we send per week?", "translation": "Berapa banyak email yang harus kita kirim per minggu?"},
                    {"type": "dialogue", "role": "B", "en": "Two to three is the sweet spot.", "translation": "Dua hingga tiga adalah titik ideal."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll write a welcome sequence for new subscribers.", "translation": "Saya akan tulis urutan sambutan untuk subscriber baru."},
                    {"type": "dialogue", "role": "A", "en": "Can you A/B test the email templates?", "translation": "Bisa kamu A/B test template email?"},
                    {"type": "dialogue", "role": "B", "en": "I'll test subject lines and CTA placement.", "translation": "Saya akan test subject line dan penempatan CTA."},
                ]
            },
            {
                "chapter": "Social Media",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll write engaging captions for Instagram.", "translation": "Saya akan tulis caption menarik untuk Instagram."},
                    {"type": "dialogue", "role": "A", "en": "What kind of content performs best on LinkedIn?", "translation": "Jenis konten apa yang paling perform di LinkedIn?"},
                    {"type": "dialogue", "role": "B", "en": "Thought leadership posts with actionable tips.", "translation": "Postingan pemimpin pemikiran dengan tips yang bisa dipraktikkan."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll create a content calendar for the month.", "translation": "Saya akan buat content calendar untuk bulan ini."},
                    {"type": "dialogue", "role": "A", "en": "Should we use hashtags in our posts?", "translation": "Haruskah kita pakai hashtag di postingan?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, but only relevant ones, about 5-10.", "translation": "Ya, tapi hanya yang relevan, sekitar 5-10."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll write thread content for Twitter/X.", "translation": "Saya akan tulis konten thread untuk Twitter/X."},
                    {"type": "dialogue", "role": "A", "en": "Can you write viral-worthy copy?", "translation": "Bisa kamu tulis copy yang layak viral?"},
                    {"type": "dialogue", "role": "B", "en": "I'll write hooks that stop the scroll.", "translation": "Saya akan tulis hook yang bikin orang berhenti scroll."},
                ]
            },
            {
                "chapter": "Advertising",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll write ad copy for Google Ads.", "translation": "Saya akan tulis copy iklan untuk Google Ads."},
                    {"type": "dialogue", "role": "A", "en": "What's the character limit for Google Ads?", "translation": "Berapa batas karakter untuk Google Ads?"},
                    {"type": "dialogue", "role": "B", "en": "Headlines are 30 characters, descriptions 90.", "translation": "Headline 30 karakter, deskripsi 90 karakter."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll create Facebook ad variations for A/B testing.", "translation": "Saya akan buat variasi iklan Facebook untuk A/B testing."},
                    {"type": "dialogue", "role": "A", "en": "How do we write ads that convert?", "translation": "Bagaimana kita tulis iklan yang mengkonversi?"},
                    {"type": "dialogue", "role": "B", "en": "Focus on benefits, use urgency, and clear CTA.", "translation": "Fokus pada manfaat, gunakan urgensi, dan CTA jelas."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll optimize the ad copy based on performance.", "translation": "Saya akan optimasi copy iklan berdasarkan performa."},
                    {"type": "dialogue", "role": "A", "en": "What's our target cost per click?", "translation": "Berapa target cost per click kita?"},
                    {"type": "dialogue", "role": "B", "en": "We're aiming for under 5,000 rupiah per click.", "translation": "Kami mentok di bawah 5.000 rupiah per klik."},
                ]
            }
        ]
    },
    {
        "id": "software-engineering",
        "name": "Software Engineering",
        "chapters": [
            {
                "chapter": "Interview",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I have experience with React, Node.js, and PostgreSQL.", "translation": "Saya punya pengalaman dengan React, Node.js, dan PostgreSQL."},
                    {"type": "dialogue", "role": "A", "en": "Can you tell me about a challenging project you've worked on?", "translation": "Bisa ceritakan tentang project menantang yang pernah kamu kerjakan?"},
                    {"type": "dialogue", "role": "B", "en": "I built a real-time chat system handling 10,000 concurrent users.", "translation": "Saya membangun sistem chat real-time yang menangani 10.000 pengguna concurrent."},
                    {"type": "phrase", "role": "Speaker", "en": "I'm comfortable with agile development methodologies.", "translation": "Saya nyaman dengan metodologi pengembangan agile."},
                    {"type": "dialogue", "role": "A", "en": "How do you approach debugging complex issues?", "translation": "Bagaimana kamu mendekati debugging masalah kompleks?"},
                    {"type": "dialogue", "role": "B", "en": "I start with logs, then add breakpoints to isolate the issue.", "translation": "Saya mulai dari log, lalu tambahkan breakpoint untuk mengisolasi masalah."},
                    {"type": "phrase", "role": "Speaker", "en": "I'm passionate about writing clean, maintainable code.", "translation": "Saya bersemangat menulis kode yang bersih dan mudah dirawat."},
                    {"type": "dialogue", "role": "A", "en": "What's your experience with CI/CD pipelines?", "translation": "Pengalaman kamu dengan CI/CD pipeline apa?"},
                    {"type": "dialogue", "role": "B", "en": "I've set up GitHub Actions and Jenkins for automated deployment.", "translation": "Saya sudah setup GitHub Actions dan Jenkins untuk deployment otomatis."},
                ]
            },
            {
                "chapter": "Documentation",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll write the API documentation for the new endpoints.", "translation": "Saya akan tulis dokumentasi API untuk endpoint baru."},
                    {"type": "dialogue", "role": "A", "en": "Can you update the README with installation steps?", "translation": "Bisa kamu update README dengan langkah instalasi?"},
                    {"type": "dialogue", "role": "B", "en": "Done, I've also added usage examples.", "translation": "Selesai, saya juga sudah tambahkan contoh penggunaan."},
                    {"type": "phrase", "role": "Speaker", "en": "Good documentation saves hours of support time.", "translation": "Dokumentasi yang baik menghemat jam waktu support."},
                    {"type": "dialogue", "role": "A", "en": "Should we use Swagger for API docs?", "translation": "Haruskah kita pakai Swagger untuk dokumentasi API?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it auto-generates interactive documentation.", "translation": "Ya, ini auto-generate dokumentasi interaktif."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll document the database schema changes.", "translation": "Saya akan dokumentasikan perubahan skema database."},
                    {"type": "dialogue", "role": "A", "en": "Where should we store the technical docs?", "translation": "Di mana kita simpan dokumen teknis?"},
                    {"type": "dialogue", "role": "B", "en": "In the repo's docs folder and Confluence.", "translation": "Di folder docs repo dan Confluence."},
                ]
            },
            {
                "chapter": "Code Review",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "I'll review your pull request today.", "translation": "Saya akan review pull request kamu hari ini."},
                    {"type": "dialogue", "role": "A", "en": "Can you check for potential security vulnerabilities?", "translation": "Bisa kamu cek potensi kerentanan keamanan?"},
                    {"type": "dialogue", "role": "B", "en": "I found one SQL injection risk and flagged it.", "translation": "Saya menemukan satu risiko SQL injection dan saya tandai."},
                    {"type": "phrase", "role": "Speaker", "en": "The code looks good, just a few minor suggestions.", "translation": "Kodenya bagus, hanya beberapa saran kecil."},
                    {"type": "dialogue", "role": "A", "en": "Is this function well-tested?", "translation": "Apakah fungsi ini sudah teruji dengan baik?"},
                    {"type": "dialogue", "role": "B", "en": "I'd suggest adding more edge case tests.", "translation": "Saya sarankan tambahkan lebih banyak test edge case."},
                    {"type": "phrase", "role": "Speaker", "en": "Let's refactor this to improve readability.", "translation": "Ayo refactor ini untuk tingkatkan keterbacaan."},
                    {"type": "dialogue", "role": "A", "en": "Should we split this into smaller components?", "translation": "Haruskah kita bagi ini menjadi komponen lebih kecil?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, it's doing too much in one function.", "translation": "Ya, terlalu banyak yang dilakukan dalam satu fungsi."},
                ]
            },
            {
                "chapter": "Standup",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Yesterday I finished the authentication module.", "translation": "Kemarin saya selesaikan modul autentikasi."},
                    {"type": "dialogue", "role": "A", "en": "What are you working on today?", "translation": "Apa yang kamu kerjakan hari ini?"},
                    {"type": "dialogue", "role": "B", "en": "I'm implementing the user profile API.", "translation": "Saya sedang mengimplementasikan API profil pengguna."},
                    {"type": "phrase", "role": "Speaker", "en": "I'm blocked by the database migration.", "translation": "Saya terhalang oleh migrasi database."},
                    {"type": "dialogue", "role": "A", "en": "Do you need any help from the team?", "translation": "Apakah kamu butuh bantuan dari tim?"},
                    {"type": "dialogue", "role": "B", "en": "Yes, I need the DBA to review the migration script.", "translation": "Ya, saya butuh DBA untuk review script migrasi."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll push the code before lunch.", "translation": "Saya akan push kode sebelum makan siang."},
                    {"type": "dialogue", "role": "A", "en": "Any risks to the sprint deadline?", "translation": "Ada risiko terhadap deadline sprint?"},
                    {"type": "dialogue", "role": "B", "en": "The third-party API integration might take longer.", "translation": "Integrasi API pihak ketiga mungkin memakan waktu lebih lama."},
                ]
            },
            {
                "chapter": "Technical Discussion",
                "scripts": [
                    {"type": "phrase", "role": "Speaker", "en": "Let's discuss the architecture for the new service.", "translation": "Ayo diskusikan arsitektur untuk service baru."},
                    {"type": "dialogue", "role": "A", "en": "Should we use microservices or a monolith?", "translation": "Haruskah kita pakai microservices atau monolit?"},
                    {"type": "dialogue", "role": "B", "en": "Microservices will give us better scalability.", "translation": "Microservices akan memberi kami skalabilitas lebih baik."},
                    {"type": "phrase", "role": "Speaker", "en": "We need to consider the trade-offs.", "translation": "Kita perlu mempertimbangkan trade-off."},
                    {"type": "dialogue", "role": "A", "en": "What database would you recommend?", "translation": "Database apa yang kamu rekomendasikan?"},
                    {"type": "dialogue", "role": "B", "en": "PostgreSQL for relational data, Redis for caching.", "translation": "PostgreSQL untuk data relasional, Redis untuk caching."},
                    {"type": "phrase", "role": "Speaker", "en": "I'll write an RFC for the proposed changes.", "translation": "Saya akan tulis RFC untuk perubahan yang diusulkan."},
                    {"type": "dialogue", "role": "A", "en": "How will we handle error handling across services?", "translation": "Bagaimana kita menangani error handling lintas service?"},
                    {"type": "dialogue", "role": "B", "en": "We'll use a centralized logging system and circuit breakers.", "translation": "Kita akan pakai sistem logging terpusat dan circuit breaker."},
                ]
            }
        ]
    }
]

# Generate individual files and master file
all_categories_master = {"categories": []}

for cat in categories:
    cat_id = cat["id"]
    cat_name = cat["name"]
    scripts = []
    script_num = 1
    
    for chapter_data in cat["chapters"]:
        chapter_name = chapter_data["chapter"]
        for line in chapter_data["scripts"]:
            scripts.append({
                "num_id": f"{cat_id}_{script_num:03d}",
                "chapter": chapter_name,
                "type": line["type"],
                "role": line["role"],
                "en": line["en"],
                "translation": line["translation"]
            })
            script_num += 1
    
    # Save individual category file
    individual = {
        "id": cat_id,
        "name": cat_name,
        "scripts": scripts
    }
    
    filename = f"{cat_id}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(individual, f, indent=2, ensure_ascii=False)
    print(f"Created {filepath} with {len(scripts)} scripts")
    
    # Add to master
    all_categories_master["categories"].append(individual)

# Save master file
master_path = os.path.join(OUTPUT_DIR, "all-categories.json")
with open(master_path, "w", encoding="utf-8") as f:
    json.dump(all_categories_master, f, indent=2, ensure_ascii=False)

total = sum(len(cat["scripts"]) for cat in all_categories_master["categories"])
print(f"\nCreated master file: {master_path}")
print(f"Total scripts across all categories: {total}")
