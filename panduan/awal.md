Mantap, Arie! 🔥  
Kita akan buat **30-Day Challenger Plan** yang *realistis, fokus, dan langsung relevan* dengan targetmu:  
> **Transisi dari sysadmin → Software Engineer + Data Engineer (Python-based, AI-adjacent)**  

Dan karena kamu sudah punya latar belakang kuat (Linux, otomasi, Golang, trading system, open-source), kita **leverage itu**, bukan mulai dari nol.

---

## 🎯 **Prinsip Rancangan Challenger Ini**
1. **Setiap hari = 1 jam fokus** (bisa lebih, tapi 1 jam wajib).  
2. **Output nyata setiap hari** — minimal 1 potongan kode, 1 catatan, atau 1 commit.  
3. **Fokus pada portfolio + skill tes rekrutmen**, bukan teori abstrak.  
4. **Integrasikan dengan identitasmu**: Quant Analyst, Algo Dev, SysAdmin → jadi nilai unik.

---

## 📅 **30-Day Roadmap: “SysAdmin to Data/Software Engineer”**

### **Minggu 1: Python Engineering & Data Wrangling Foundry**  
*(Tujuan: Lolos coding test dasar + buat pipeline data sederhana)*

| Hari | Fokus | Tantangan Harian | Output |
|------|-------|------------------|--------|
| 1 | Python Fundamentals Reboot | Kerjakan 3 soal LeetCode Easy: `reverse string`, `valid palindrome`, `group anagrams` | Repo GitHub: `day01-python-basics` |
| 2 | File I/O + JSON/CSV | Baca file log (mock syslog) → ekstrak IP & timestamp → simpan ke CSV | Script: `parse_logs.py` |
| 3 | Pandas Crash | Muat dataset (gunakan [Kaggle “Top 10k YouTube”](https://www.kaggle.com/datasets/)) → hitung rata-rata views per category | Notebook: `youtube_eda.ipynb` |
| 4 | Error Handling + Logging | Tambahkan try/except + logging ke script hari ke-2 | Update `parse_logs.py` |
| 5 | Functions & Modularity | Pisahkan logic hari ke-3 jadi fungsi reusable | `data_cleaner.py` + `main.py` |
| 6 | Virtual Env + Requirements | Buat `requirements.txt` + `.gitignore` + README | Siap deploy ke GitHub |
| 7 | **Mini-Project**: Log Analyzer CLI | Gabung semua: input file → output statistik → simpan hasil | GitHub repo lengkap |

> ✅ **Akhir Minggu 1**: Kamu punya **1 proyek CLI data tool** — relevan untuk sysadmin & data eng!

---

### **Minggu 2: Data Engineering Lite + API & Automation**  
*(Tujuan: Bangun pipeline otomatis, pahami data flow, sentuh API)*

| Hari | Fokus | Tantangan Harian | Output |
|------|-------|------------------|--------|
| 8 | REST API Basics | Gunakan `requests` untuk ambil data dari [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | `fetch_posts.py` |
| 9 | JSON → Pandas → CSV | Ambil data posts → simpan ke CSV/Parquet | Tambah ke repo |
|10| Schedule Task (cron/systemd) | Jadwalkan script hari ke-9 jalan tiap 1 jam (simulasi di local) | Dokumentasi di README |
|11| Environment Variables | Ganti hardcoded URL dengan `.env` (gunakan `python-dotenv`) | Lebih aman & profesional |
|12| Dockerize App | Buat `Dockerfile` untuk script hari ke-9 | Image bisa jalan di mana saja |
|13| Data Validation | Tambahkan validasi: cek kolom wajib, tipe data | `validate.py` |
|14| **Mini-Project**: Data Fetcher Pipeline | API → clean → validate → save → log → containerize | GitHub + Docker Hub (opsional) |

> ✅ **Akhir Minggu 2**: Kamu punya **data pipeline otomatis, containerized, siap produksi** — ini *gold* untuk DE role!

---

### **Minggu 3: Software Engineering Practices**  
*(Tujuan: Tulis kode seperti engineer profesional — testing, docs, struktur)*

| Hari | Fokus | Tantangan Harian | Output |
|------|-------|------------------|--------|
|15| Project Structure (src/) | Ubah semua proyek ke struktur: `src/`, `tests/`, `docs/` | Modern Python layout |
|16| Unit Testing (pytest) | Tulis 3 test untuk fungsi di `data_cleaner.py` | `tests/test_cleaner.py` |
|17| Type Hints | Tambahkan type hints ke semua fungsi utama | Lebih readable & aman |
|18| CLI with `argparse` | Ubah script jadi CLI: `python run.py --input file.log` | Profesional banget |
|19| GitHub Actions (CI) | Otomatisasi: jalankan test tiap push | `.github/workflows/test.yml` |
|20| Document with README.md | Tulis README teknis: cara install, run, contoh output | Seperti proyek open-source |
|21| **Refactor & Publish** | Gabung semua project jadi 1 monorepo: `sysadmin-to-data-eng` | Portfolio siap!

> ✅ **Akhir Minggu 3**: Kamu bukan cuma coder — kamu **software engineer**.

---

### **Minggu 4: AI/ML Adjacent + Job Ready**  
*(Tujuan: Tunjukkan relevansi ke AI Trainer / Data Eng di AI team)*

| Hari | Fokus | Tantangan Harian | Output |
|------|-------|------------------|--------|
|22| Text Preprocessing | Bersihkan teks: hapus emoji, lower, tokenize | `text_utils.py` |
|23| Format for LLM Training | Ubah data ke format: `{"instruction": "...", "output": "..."}` | JSON siap fine-tune |
|24| Mock AI Trainer Task | Ambil 100 ulasan produk → buat dataset pelatihan | `dataset_llm.json` |
|25| Add to Portfolio | Masukkan ke repo utama: `/ai-trainer-tasks` | Relevan langsung! |
|26| LinkedIn Post #1 | Tulis: “30 hari dari sysadmin ke data engineer: Hari 1–7” | Bangun personal branding |
|27| CV Update | Tambahkan: **Python Data Pipeline**, **Automated ETL**, **Dockerized CLI Tools** | Sesuai target role |
|28| Mock Coding Test | Ambil 1 soal dari [Codility](https://www.codility.com/) atau [HackerRank](https://www.hackerrank.com/) | Latihan realistis |
|29| Record 2-Minute Demo | Rekam layar: demo pipeline otomatis kamu | Untuk portofolio/video intro |
|30| **Apply & Reflect** | Kirim lamaran ke 3 lowongan (termasuk Invisible.co!) + tulis refleksi | **GRADUATION!** 🎓 |

---

## 🛠️ **Tools yang Akan Kamu Kuasai dalam 30 Hari**
- Python (pandas, requests, logging, argparse, pytest)  
- Git & GitHub (CI, README, struktur proyek)  
- Docker  
- Cron / Otomasi  
- CLI development  
- Data validation & cleaning  
- Basic NLP for AI data prep  

---

