# 🐍 Python for AI & Data Engineering — 30-Day Challenger

> **From SysAdmin to Software + Data Engineer**  
> Oleh: **Arie Ibrahim** — Quant Analyst & Algo Developer | Freelance IT | Linux SysAdmin

Proyek ini adalah hasil **30 hari latihan intensif** untuk transisi karier:
- Mantan **Linux sysadmin** → **Python engineer**
- Fokus pada: **data pipeline, otomasi, AI-ready data, CLI tooling**

Setiap hari: 1 jam coding → 1 commit → 1 skill baru.

---

## 🚀 Fitur Utama
- ✅ **Ambil data dari API** → validasi → simpan ke CSV/JSON
- ✅ **CLI tool** dengan `argparse` (seperti `curl` atau `awk`)
- ✅ **Otomasi harian** (simulasi cron)
- ✅ **Dockerized** — jalan di mana saja, 1 perintah
- ✅ **Unit test** dengan `pytest`
- ✅ **GitHub Actions** — CI otomatis tiap push
- ✅ **Modular & reusable** — struktur `src/`, `scripts/`, `tests/`

---

## 🛠️ Teknologi
- **Python 3.9+**
- `requests` → ambil data API
- `pytest` → test otomatis
- `python-dotenv` → konfigurasi
- `Docker` → containerisasi
- **GitHub Actions** → CI/CD

---

## ▶️ Cara Coba (Langsung Jalan!)

```bash
# 1. Clone repo
git clone https://github.com/arieDEV/python-ai.git
cd python-ai

# 2. Setup (opsional: pakai venv)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Jalankan pipeline
python scripts/run_pipeline.py --output data/output/demo.csv

# 4. Atau pakai Docker (tanpa install Python!)
docker build -t loganalyzer .
docker run --rm -v "$(pwd)/data:/app/data" loganalyzer
