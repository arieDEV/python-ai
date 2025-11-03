Mantap, Arie! 👏  
Meski repo GitHub-mu masih **empty**, **latihanmu jalan lancar** — bahkan di macOS dengan LibreSSL (yang notabene bikin error di `urllib3 v2`), **pipeline tetap jalan!** 🎯  
Ini bukti: kamu **sudah berpikir dan kerja seperti engineer produksi**.

Sekarang, lanjut ke **Hari ke-11** dengan fokus:  
> **Pisahkan konfigurasi dari kode — pakai `.env`**, biar gampang ganti URL, path, atau API key **tanpa edit skrip**.

Dan tetap: **kode jelas, gaya sysadmin, langsung jalan**.

---

## 🎯 **Hari 11: Gunakan `.env` untuk Konfigurasi (Seperti `/etc/default/` di Linux)**

Tujuan:
- Pisahkan **konfigurasi** (API URL, folder output) dari **kode**
- Mirip cara Linux simpan config di `/etc/default/nama-service`
- Pakai file `.env` → aman, gampang diubah, tidak perlu sentuh Python

> ⚠️ File `.env` **jangan di-commit** jika ada secret — tapi untuk URL publik (seperti JSONPlaceholder), boleh untuk demo.

---

### 📂 Struktur Hari Ini:
```
python-ai/
├── .env                    ← konfigurasi (bisa di-commit kalau publik)
├── .gitignore              ← pastikan .env tidak ikut kalau ada secret
├── day11/
│   └── fetch_with_env.py   ← script baru pakai .env
└── requirements.txt        ← tambah python-dotenv
```

---

## 🔧 Langkah 1: Tambah `python-dotenv` ke `requirements.txt`

Edit `requirements.txt`:
```txt
pandas>=2.0.0
requests>=2.28.0
python-dotenv>=1.0.0
```

Lalu update venv:
```bash
source /Volumes/backup/Desktop/ai-env/bin/activate
pip install -r requirements.txt
```

> `python-dotenv` = library ringan buat baca file `.env` → jadi variabel environment di Python.

---

## 📄 Langkah 2: Buat `.env`

Simpan di **root proyek** (`python-ai/.env`):

```env
# API Configuration
API_URL=https://jsonplaceholder.typicode.com/posts

# Path Configuration
RAW_DATA_DIR=day11/raw
OUTPUT_DIR=day11/output
```

> Ini seperti file `/etc/default/loganalyzer` — semua setting di satu tempat.

---

## 📄 Langkah 3: `day11/fetch_with_env.py`

```python
import os
import requests
import pandas as pd
from dotenv import load_dotenv  # baca .env
import logging

# Muat konfigurasi dari .env → jadi os.environ
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def fetch_and_save():
    # Ambil dari .env — jangan hardcode!
    api_url = os.getenv("API_URL")
    raw_dir = os.getenv("RAW_DATA_DIR")
    output_dir = os.getenv("OUTPUT_DIR")

    # Validasi: pastikan semua konfig ada
    if not all([api_url, raw_dir, output_dir]):
        logging.error("❌ Konfigurasi .env tidak lengkap!")
        return False

    json_path = os.path.join(raw_dir, "posts.json")
    csv_path = os.path.join(output_dir, "posts.csv")

    # 1. Ambil data
    try:
        logging.info(f"📡 Ambil dari: {api_url}")
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logging.error(f"❌ Gagal ambil API: {e}")
        return False

    # 2. Simpan JSON
    os.makedirs(raw_dir, exist_ok=True)
    with open(json_path, 'w') as f:
        f.write(resp.text)
    logging.info(f"💾 JSON: {json_path}")

    # 3. Konversi ke CSV
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False)
    logging.info(f"✅ CSV: {csv_path}")

    return True

if __name__ == "__main__":
    logging.info("=== Pipeline dengan .env ===")
    fetch_and_save()
```

---

### ▶️ Cara Jalankan:
```bash
mkdir -p day11
python day11/fetch_with_env.py
```

Output:
- `day11/raw/posts.json`
- `day11/output/posts.csv`

---

### 🔒 `.gitignore` Update (Opsional Tapi Disarankan)
Edit `.gitignore`:
```gitignore
# Environment files (hapus baris ini jika .env publik & ingin di-commit)
.env

# Tapi kalau .env-nya publik (seperti sekarang), kamu BOLEH commit.
# Untuk proyek nyata dengan API key → JANGAN commit .env!
```

> Untuk **latihan ini**, boleh commit `.env` karena isinya **publik**.

---

### 💡 Analogi SysAdmin:
| Python + `.env` | Linux System |
|------------------|-------------|
| `.env` | `/etc/default/nama-service` |
| `os.getenv("API_URL")` | `source /etc/default/... && echo $API_URL` |
| `load_dotenv()` | `set -a; source .env; set +a` |

> Keuntungan: ganti target API **tanpa ubah kode** — tinggal edit `.env`.

---

## ✅ Tugas Hari Ini:
1. Tambah `python-dotenv` ke `requirements.txt` → `pip install`
2. Buat `.env` di root
3. Buat folder `day11/`
4. Simpan `fetch_with_env.py`
5. Jalankan → pastikan jalan
6. **(PENTING)** Mulai **commit & push ke GitHub** — setidaknya lokal dulu, lalu remote.  
   Repo-mu **harus mulai terisi** — ini bukti nyata progresmu!

> Setelah selesai, balas: **“Day 11 done!”**

Besok (Hari 12): kita **containerize** pipeline ini pakai **Docker** — biar jalan di mana saja, tanpa install Python.  
Dan karena kamu pernah bikin `mini-docker` (Golang), ini akan jadi **koneksi kuat antara dua duniamu**! 🐳

Ayo, Arie! **Jangan biarkan repo-mu tetap kosong.**  
Setiap baris kode yang kamu tulis hari ini adalah **investasi karier**. 💪
