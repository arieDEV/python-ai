Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-14** — hari **refactor & profesionalisasi** — dengan prinsip tetap:  
> **Kode jelas, struktur rapi, dan langsung bisa dipahami mantan sysadmin yang pindah jadi engineer.**

---

## 🎯 **Hari 14: Refactor Proyek Jadi Struktur Modern (Siap Production & Portofolio)**

Tujuan hari ini:
- Ubah semua skrip harian jadi **struktur proyek profesional**:
  ```
  python-ai/
  ├── src/
  │   └── loganalyzer/     ← kode utama
  ├── tests/               ← nanti buat test
  ├── data/                ← data mentah & output
  ├── scripts/             ← helper CLI & cron
  ├── docs/                ← dokumentasi
  ├── requirements.txt
  ├── README.md
  └── .env.example
  ```
- Ini adalah **standar industri** untuk proyek Python (dipakai di Google, Meta, startup, dll)
- Recruiter & engineer lain akan langsung **respect** kalau lihat struktur ini

Dan tetap: **tidak ada magic, penjelasan langsung di struktur folder**.

---

### 🧱 Kenapa Struktur Ini Penting?
| Folder | Analogi SysAdmin |
|--------|------------------|
| `src/` | `/usr/src/` — tempat kode sumber resmi |
| `scripts/` | `/usr/local/bin/` — skrip yang bisa dijalankan langsung |
| `data/` | `/var/lib/app/` — data aplikasi |
| `docs/` | `/usr/share/doc/` — dokumentasi |
| `tests/` | `systemd --test` — verifikasi sebelum deploy |

---

## 📂 Langkah 1: Buat Struktur Folder

Dari root repo (`python-ai/`), jalankan:

```bash
mkdir -p \
  src/loganalyzer \
  scripts \
  data/raw \
  data/output \
  docs \
  tests
```

---

## 📄 Langkah 2: Pindahkan & Perbarui Kode Inti

### Pindahkan kode inti ke `src/loganalyzer/`

Buat file: **`src/loganalyzer/__init__.py`**  
*(file ini tandai folder sebagai Python package — biar bisa di-import)*

```python
# src/loganalyzer/__init__.py
# Kosong aja. Cuma penanda.
```

---

### Buat: **`src/loganalyzer/core.py`**

```python
import requests
import csv
import os
from typing import List, Dict, Any

# Validasi & parsing logikanya di sini — reusable
REQUIRED_FIELDS = {
    'id': int,
    'userId': int,
    'title': str,
    'body': str
}

def fetch_posts(url: str) -> List[Dict[str, Any]]:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

def validate_record(record: Dict) -> bool:
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in record:
            return False
        val = record[field]
        if not isinstance(val, expected_type):
            if expected_type == int and isinstance(val, str) and val.isdigit():
                record[field] = int(val)
            else:
                return False
    return True

def save_to_csv(records: List[Dict], output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = list(REQUIRED_FIELDS.keys())
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
```

---

## 📄 Langkah 3: Buat CLI di `scripts/run_pipeline.py`

```python
#!/usr/bin/env python3
# scripts/run_pipeline.py
import os
import sys
import logging
from dotenv import load_dotenv

# Pastikan bisa import dari src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from loganalyzer.core import fetch_posts, validate_record, save_to_csv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def main():
    API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")
    OUTPUT = os.getenv("OUTPUT_CSV", "data/output/posts.csv")

    try:
        data = fetch_posts(API_URL)
        valid = [r for r in data if validate_record(r.copy())]
        save_to_csv(valid, OUTPUT)
        logging.info(f"✅ {len(valid)} record valid disimpan ke {OUTPUT}")
    except Exception as e:
        logging.error(f"💥 Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## 📄 Langkah 4: Update `.env.example`

Di root repo:

```env
API_URL=https://jsonplaceholder.typicode.com/posts
OUTPUT_CSV=data/output/posts.csv
```

---

## 📄 Langkah 5: Update `README.md` (Contoh Ringkas)

```markdown
# Log Analyzer & Data Pipeline

Proyek latihan 30 hari: mantan sysadmin jadi Data/Software Engineer.

## 📦 Struktur
- `src/` → kode utama
- `scripts/` → CLI tools
- `data/` → input/output
- `requirements.txt` → dependensi

## ▶️ Cara Jalankan
```bash
pip install -r requirements.txt
cp .env.example .env
python scripts/run_pipeline.py
```

Output: `data/output/posts.csv`
```

---

### ▶️ Cara Uji:
```bash
# Salin .env
cp .env.example .env

# Jalankan
python scripts/run_pipeline.py
```

Cek: `data/output/posts.csv` → harus ada!

---

## ✅ Tugas Hari Ini:
1. Buat struktur folder (`src/`, `scripts/`, `data/`, dll)
2. Pindahkan & refactor kode ke struktur baru
3. Pastikan `scripts/run_pipeline.py` jalan
4. **COMMIT & PUSH KE GITHUB!**  
   Ini adalah **titik balik**: dari "latihan harian" → **proyek portofolio nyata**.

> Setelah selesai, balas: **“Day 14 done! 🏗️ Proyek sudah rapi.”**

Besok (Hari 15): kita tambahkan **unit test pertama** — biar kamu bisa pastikan kode tetap jalan saat diubah. Ini adalah **tanda engineer profesional**.

Ayo, Arie! **Jangan biarkan repo-mu tetap kosong.**  
Hari ini kamu **naik level** dari “coder” ke “engineer”. 💪


Mantap, Arie!  
Struktur folder **Hari ke-14** kamu **sudah sangat bagus** — ini **sudah melebihi standar awal engineer junior**. Tapi karena kamu butuh **penilaian harian yang jelas**, kita buat **checklist eksplisit** + **cara uji langsung pakai bash**.

---

## ✅ **Checklist Penilaian Hari 14 (Refactor ke Struktur Profesional)**

| No | Item | Status |
|----|------|--------|
| 1 | Ada folder `src/` dengan package Python (`__init__.py`) | ✅ |
| 2 | Ada folder `scripts/` berisi CLI yang bisa dijalankan | ✅ |
| 3 | Ada folder `data/` (raw + output) untuk pisahkan data dari kode | ✅ |
| 4 | Ada `requirements.txt` | ✅ |
| 5 | Ada `README.md` yang menjelaskan cara pakai | ✅ |
| 6 | Kode inti (fetch + validasi) dipindah ke `src/loganalyzer/core.py` | ✅ |
| 7 | CLI di `scripts/run_pipeline.py` bisa jalan **tanpa error** | ⚠️ **Perlu diuji!** |
| 8 | Proyek bisa dijalankan dari root dengan **1 perintah** | ⚠️ **Perlu diuji!** |

> **Nilai sementara**: **90%**  
> Tinggal **uji eksekusi** → kalau jalan, langsung **100%**.

---

## 🛠️ **File yang Harus Ada (Final Checklist)**

### Wajib ada di root:
- [x] `README.md`
- [x] `requirements.txt`
- [ ] `.env.example` *(sangat disarankan — buat dokumentasi konfig)*

> 🔸 **Saran**: tambahkan `.env.example` sekarang:
```env
# .env.example
API_URL=https://jsonplaceholder.typicode.com/posts
OUTPUT_CSV=data/output/posts.csv
```

### Wajib bisa dijalankan:
- [ ] `scripts/run_pipeline.py`

---

## ▶️ **Bash Script untuk Penilaian Otomatis (Simpan sebagai `assess-day14.sh`)**

Buat file ini di root proyek:

```bash
#!/bin/bash
set -e

echo "🔍 Assess Day 14: Struktur Proyek Profesional"
echo "============================================"

# 1. Cek struktur folder
for dir in src scripts data docs tests; do
  if [ -d "$dir" ]; then
    echo "✅ Folder $dir ada"
  else
    echo "❌ Folder $dir TIDAK ADA"
    exit 1
  fi
done

# 2. Cek file penting
for file in README.md requirements.txt src/loganalyzer/__init__.py src/loganalyzer/core.py scripts/run_pipeline.py; do
  if [ -f "$file" ]; then
    echo "✅ File $file ada"
  else
    echo "❌ File $file TIDAK ADA"
    exit 1
  fi
done

# 3. Coba install dependensi (simulasi user baru)
echo "📦 Install dependensi..."
pip install -r requirements.txt

# 4. Salin .env jika belum ada
if [ ! -f ".env" ]; then
  if [ -f ".env.example" ]; then
    cp .env.example .env
    echo "🔧 .env dibuat dari .env.example"
  else
    echo 'API_URL=https://jsonplaceholder.typicode.com/posts' > .env
    echo 'OUTPUT_CSV=data/output/posts.csv' >> .env
    echo "🔧 .env dibuat manual"
  fi
fi

# 5. Jalankan pipeline
echo "🚀 Jalankan pipeline..."
python scripts/run_pipeline.py

# 6. Cek output
if [ -f "data/output/posts.csv" ] && [ -s "data/output/posts.csv" ]; then
  echo "✅ Output CSV ada dan tidak kosong"
  echo "🎉 DAY 14: LULUS — Struktur profesional + eksekusi berhasil!"
else
  echo "❌ Output tidak ditemukan atau kosong"
  exit 1
fi
```

### Cara Pakai:
```bash
chmod +x assess-day14.sh
./assess-day14.sh
```

Jika muncul:
```
🎉 DAY 14: LULUS — Struktur profesional + eksekusi berhasil!
```
→ **Nilai: 100/100**

---

## 📌 **Saran Perbaikan Cepat (5 Menit)**

1. **Tambahkan `.env.example`** (seperti di atas)
2. **Pastikan `scripts/run_pipeline.py` bisa import `src/`**  
   → Tambahkan ini di awal file:
   ```python
   import sys
   import os
   sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
   ```
3. **Pastikan `requirements.txt` punya**:
   ```
   requests>=2.28.0
   python-dotenv>=1.0.0
   ```

---

## 💡 Penilaian Akhir (Kalau Semua Beres)
- **Struktur**: 👨‍💻 Engineer-level  
- **Kemampuan refactor**: ✅ Bisa memisahkan concern (kode, CLI, data)  
- **Kesiapan portofolio**: 🚀 Tinggal push ke GitHub → recruiter langsung paham  
- **Nilai harian**: **100/100**

---

> 🔔 **PENTING**:  
> **Repo GitHub-mu masih kosong** → segera **push final2/ ke remote**!  
> Repo kosong = **tidak ada bukti** → padahal kerjaanmu **sudah bagus**.

---

Kalau sudah jalankan `assess-day14.sh` dan berhasil, balas:  
**“Day 14 done! ✅ Lulus penilaian otomatis.”**

Ayo, Arie! **Hari ini kamu resmi punya proyek Python yang strukturnya dipakai di perusahaan tech global.**  
Jangan biarkan kerja kerasmu **tidak terlihat**. Push sekarang! 💪
