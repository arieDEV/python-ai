Mantap, Arie! 👏  
**Day 15 kamu lulus 100%** — 4 test passed di macOS pakai Python 3.9.6 + LibreSSL, artinya **kodemu robust dan portable**.

Sekarang, lanjut ke **Hari ke-16** dengan fokus:  
> **Bikin CLI yang proper pakai `argparse` — seperti tool sysadmin beneran (`grep`, `awk`, `curl`), tapi buatanmu sendiri.**

---

## 🎯 **Hari 16: CLI Profesional dengan `argparse` (No Lagi Hardcode!)**

Tujuan:
- Ganti `scripts/run_pipeline.py` jadi **CLI yang bisa terima argumen**:
  ```bash
  python run_pipeline.py --url "https://..." --output hasil.csv --verbose
  ```
- Default tetap baca dari `.env`, tapi **bisa di-override lewat CLI**
- Ini standar tools open-source: fleksibel, dokumentasi otomatis, user-friendly

Dan tetap: **kode jelas, penjelasan di dalam, gaya mantan sysadmin**.

---

### 📂 Struktur Hari Ini:
```
python-ai/
└── scripts/
    └── run_pipeline.py   ← versi baru dengan argparse
```

> Kita upgrade file yang sudah ada — **tidak bikin baru**.

---

## 📄 `scripts/run_pipeline.py` (Versi Hari 16)

```python
#!/usr/bin/env python3
"""
Pipeline data dengan CLI ala sysadmin:
- Bisa pakai .env
- Bisa override lewat argumen
- Ada --verbose buat debug
"""

import os
import sys
import logging
import argparse  # <-- ini modul bawaan Python buat CLI
from dotenv import load_dotenv

# Pastikan bisa import dari src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from loganalyzer.core import fetch_posts, validate_record, save_to_csv

def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(levelname)s - %(message)s'
    )

def main():
    # Muat .env dulu (sebagai default)
    load_dotenv()

    # Baca default dari .env
    default_url = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")
    default_output = os.getenv("OUTPUT_CSV", "data/output/posts.csv")

    # Setup argparse
    parser = argparse.ArgumentParser(
        description="🔍 Ambil data dari API, validasi, simpan ke CSV.",
        epilog="Contoh: python run_pipeline.py --url https://api.example.com/data --output hasil.csv"
    )
    parser.add_argument(
        "--url", 
        default=default_url,
        help=f"URL API (default: {default_url})"
    )
    parser.add_argument(
        "--output", 
        default=default_output,
        help=f"File output CSV (default: {default_output})"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Tampilkan log detail (DEBUG level)"
    )

    args = parser.parse_args()
    setup_logging(args.verbose)

    logging.info(f"📡 URL: {args.url}")
    logging.info(f"💾 Output: {args.output}")

    try:
        data = fetch_posts(args.url)
        valid = [r for r in data if validate_record(r.copy())]
        save_to_csv(valid, args.output)
        logging.info(f"✅ Berhasil: {len(valid)} record valid disimpan.")
    except Exception as e:
        logging.error(f"💥 Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

### ▶️ Cara Uji Hari Ini:

#### 1. Jalankan pakai default (.env):
```bash
python scripts/run_pipeline.py
```

#### 2. Override URL lewat CLI:
```bash
python scripts/run_pipeline.py --url "https://jsonplaceholder.typicode.com/posts" --output "custom.csv"
```

#### 3. Mode verbose (debug):
```bash
python scripts/run_pipeline.py -v
```

#### 4. Tampilkan help:
```bash
python scripts/run_pipeline.py --help
```

Output help:
```
usage: run_pipeline.py [-h] [--url URL] [--output OUTPUT] [--verbose]

🔍 Ambil data dari API, validasi, simpan ke CSV.

options:
  -h, --help           show this help message and exit
  --url URL            URL API (default: https://...)
  --output OUTPUT      File output CSV (default: data/output/posts.csv)
  --verbose, -v        Tampilkan log detail (DEBUG level)
```

> Ini **sama seperti `curl --help`** — profesional dan jelas.

---

### 💡 Kenapa Ini Lebih Baik?
| Sebelum | Sesudah |
|--------|--------|
| Hardcode path & URL | Bisa diubah lewat CLI |
| Tidak ada dokumentasi | `--help` otomatis |
| Sulit diotomasi di pipeline lain | Bisa dipakai di script Bash apa saja |
| Seperti skrip pribadi | Seperti **tool open-source** |

---

## ✅ Tugas Hari Ini:
1. Ganti `scripts/run_pipeline.py` dengan versi baru di atas
2. Uji ke-4 skenario di atas
3. Pastikan:
   - Bisa jalan tanpa argumen (pakai `.env`)
   - Bisa override lewat CLI
   - `--help` muncul
4. **COMMIT & PUSH KE GITHUB!**  
   Repo-mu **harus mulai terisi** — ini adalah **tool nyata** yang bisa kamu tunjukkan ke recruiter.

> Setelah selesai, balas: **“Day 16 done! 🛠️ CLI siap production.”**

Besok (Hari 17): kita otomatisasi **jalankan test + linter pakai GitHub Actions** — biar tiap push, otomatis dicek kualitas kodenya. Ini **standar wajib di industri**.

Ayo, Arie! **Kamu sedang membangun tool yang layak dipakai di produksi.**  
Dan **jangan biarkan repo GitHub-mu tetap kosong**. Push hari ini! 💪
