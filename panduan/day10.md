Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-10**, meski repo GitHub-mu masih kosong — **yang penting kamu terus nge-**`code`**!**

Hari ini kita fokus pada sesuatu yang **sangat dekat dengan jiwa sysadmin**:  
> **Jadwalkan script Python jalan otomatis — seperti `cron`, tapi dengan dokumentasi & simulasi jelas.**

---

## 🎯 **Hari 10: Otomasi Harian dengan Simulasi Cron (SysAdmin Style)**

Kita akan:
- Buat script utama yang **menggabungkan Day 8 + Day 9**:  
  **Ambil data dari API → simpan ke JSON → konversi ke CSV**
- Lalu **simulasikan cron** dengan skrip Bash sederhana
- Semua disertai logging → jadi bisa dilacak seperti syslog

Dan tetap: **kode Python-nya jelas, tanpa magic, mudah dibaca mantan sysadmin**.

---

### 📂 Struktur Hari Ini:
```
python-ai/
├── data_pipeline/
│   ├── fetch_and_convert.py   ← gabungan API + CSV
│   └── logs/                  ← folder log otomatis
├── cron_simulator.sh          ← skrip Bash buat simulasi cron
└── README-cron.md             ← dokumentasi cara pasang di cron beneran
```

---

## 📄 Langkah 1: `data_pipeline/fetch_and_convert.py`

```python
import requests
import pandas as pd
import os
import sys
import logging
from datetime import datetime

# Buat folder logs jika belum ada
os.makedirs("data_pipeline/logs", exist_ok=True)

# Setup logging ke file + terminal
log_file = f"data_pipeline/logs/pipeline_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def fetch_and_save_to_csv():
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    JSON_OUT = "data_pipeline/raw/posts.json"
    CSV_OUT = "data_pipeline/output/posts.csv"

    # 1. Ambil data dari API
    try:
        logging.info("📡 Mulai: ambil data dari API")
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        logging.info(f"✅ Berhasil ambil {len(data)} data")
    except Exception as e:
        logging.error(f"❌ Gagal ambil data: {e}")
        return False

    # 2. Simpan ke JSON
    try:
        os.makedirs(os.path.dirname(JSON_OUT), exist_ok=True)
        with open(JSON_OUT, 'w') as f:
            f.write(resp.text)
        logging.info(f"💾 JSON disimpan: {JSON_OUT}")
    except Exception as e:
        logging.error(f"❌ Gagal simpan JSON: {e}")
        return False

    # 3. Konversi ke CSV
    try:
        df = pd.read_json(JSON_OUT)
        os.makedirs(os.path.dirname(CSV_OUT), exist_ok=True)
        df.to_csv(CSV_OUT, index=False)
        logging.info(f"✅ CSV siap: {CSV_OUT}")
    except Exception as e:
        logging.error(f"❌ Gagal konversi ke CSV: {e}")
        return False

    logging.info("🎉 Pipeline selesai sukses!")
    return True

if __name__ == "__main__":
    logging.info("=== JALANKAN DATA PIPELINE HARI INI ===")
    success = fetch_and_save_to_csv()
    if not success:
        sys.exit(1)
```

---

## 📄 Langkah 2: `cron_simulator.sh`  
*(Simulasi cron — buat testing lokal)*

```bash
#!/bin/bash
# Simulasi cron: jalan tiap jam (tapi kita jalan manual dulu)
# Simpan di root repo

echo "🕒 [$(date)] Menjalankan data pipeline..."
cd "$(dirname "$0")" || exit 1

# Aktifkan venv dulu (pastikan ada!)
source venv/bin/activate

# Jalankan Python
python data_pipeline/fetch_and_convert.py

echo "✅ Simulasi cron selesai."
```

> Jangan lupa kasih izin eksekusi:
```bash
chmod +x cron_simulator.sh
```

---

## 📄 Langkah 3: `README-cron.md`  
*(Dokumentasi cara pasang di cron beneran — buat nanti)*

```markdown
# Cara Pasang Pipeline Ini di Cron (Produksi)

## Prasyarat
- Python 3.7+
- Virtual environment sudah dibuat (`venv/`)
- Dependensi terinstall (`pip install -r requirements.txt`)

## Langkah Pasang Cron
1. Dapatkan path absolut ke folder proyek:
   ```bash
   cd /path/ke/python-ai
   pwd  # misal: /home/arie/python-ai
   ```

2. Edit crontab:
   ```bash
   crontab -e
   ```

3. Tambahkan baris berikut (jalankan tiap jam jam 2 pagi):
   ```cron
   0 2 * * * cd /home/arie/python-ai && ./cron_simulator.sh >> /home/arie/python-ai/cron.log 2>&1
   ```

> ⚠️ Pastikan `cron_simulator.sh` bisa dieksekusi (`chmod +x`).

## Logging
- Log harian: `data_pipeline/logs/pipeline_*.log`
- Log cron: `cron.log`
```

---

### ▶️ Cara Uji Hari Ini:
```bash
# Buat folder
mkdir -p data_pipeline

# Jalankan simulator
./cron_simulator.sh
```

Cek output:
- `data_pipeline/output/posts.csv` → ada
- `data_pipeline/logs/pipeline_*.log` → ada isinya
- Terminal menampilkan log jelas

---

### 💡 Kenapa Ini Relevan Buat Kariermu?
- **Data Engineer** = bikin pipeline otomatis
- **AI Trainer** = butuh data segar tiap hari
- **SysAdmin modern** = otomasi + monitoring + logging

Kamu **menggabungkan semua itu** dalam 1 alur kerja.

---

## ✅ Tugas Hari Ini:
1. Buat folder `data_pipeline/`
2. Simpan `fetch_and_convert.py`
3. Buat `cron_simulator.sh` + kasih `chmod +x`
4. Buat `README-cron.md`
5. Jalankan `./cron_simulator.sh`
6. (Sangat disarankan) **Mulai push ke GitHub** — repo-mu akan jadi bukti nyata skillmu!

> Setelah selesai, balas: **“Day 10 done!”**

Besok (Hari 11): kita tambahkan **`.env` untuk konfigurasi** — biar API URL, path, dll bisa diubah tanpa edit kode. Ini standar industri!

Ayo, Arie! Kamu sedang membangun **sistem otomasi produksi-grade**, bukan cuma skrip latihan. 💪  
Dan **setiap hari yang kamu lewati tanpa commit = kesempatan terlewat**. Yuk, mulai isi repo-mu! 🚀
