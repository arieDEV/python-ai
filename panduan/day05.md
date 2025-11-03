Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-5** dengan prinsip yang sama:  
> **Kode Python yang mudah dicerna mantan sysadmin** → modular, reusable, dan terstruktur seperti skrip produksi.

---

## 🎯 **Hari 5: Modularisasi Kode — Pisah Logika Jadi Fungsi Reusable**

Tujuan hari ini:  
Ambil logika dari **Day 04** (`parse_logs_v2.py`) → **pecah jadi modul kecil** yang bisa dipakai di mana saja, seperti:
- Library parsing log
- CLI tool
- Bagian dari pipeline data

Ini mirip saat kamu bikin:
- `functions.sh` di Bash  
- Atau `lib/` di proyek otomasi

---

### 📂 Struktur Hari Ini:
```
day05/
├── main.py               ← jalankan program
├── log_parser.py         ← logika inti (bisa dipakai ulang!)
└── utils/
    └── io_helper.py      ← fungsi bantu: baca/tulis file
```

---

### 📄 Langkah 1: `day05/utils/io_helper.py`  
*(Fungsi umum untuk baca/tulis — bisa dipakai di proyek lain)*

```python
import os
import csv
import logging

# Baca file teks → kembalikan list baris
def read_lines(filepath):
    """Baca file teks, return list baris. Jika error, return None."""
    if not os.path.exists(filepath):
        logging.error(f"File tidak ditemukan: {filepath}")
        return None
    try:
        with open(filepath, 'r') as f:
            return f.readlines()
    except Exception as e:
        logging.error(f"Gagal baca {filepath}: {e}")
        return None

# Tulis list dict ke CSV
def write_dict_to_csv(data, output_path, fieldnames):
    """Tulis data (list of dict) ke CSV. Contoh: [{'ip':'1.1.1.1'}, ...]"""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Berhasil simpan ke {output_path}")
        return True
    except Exception as e:
        logging.error(f"Gagal tulis ke {output_path}: {e}")
        return False
```

---

### 📄 Langkah 2: `day05/log_parser.py`  
*(Logika parsing log — bersih, fokus, tanpa I/O langsung)*

```python
import re
import logging

def extract_ssh_logins(lines):
    """
    Ambil baris yang mengandung 'Accepted', ekstrak timestamp & IP.
    Input: list baris log
    Output: list dict [{'timestamp': ..., 'ip': ...}]
    """
    if not lines:
        logging.warning("Tidak ada baris untuk diproses")
        return []

    logins = []
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Accepted.*from\s+([0-9.]+)'

    for i, line in enumerate(lines, 1):
        try:
            match = re.search(pattern, line)
            if match:
                logins.append({
                    'timestamp': match.group(1),
                    'ip': match.group(2)
                })
        except Exception as e:
            logging.warning(f"Baris {i} error: {e}")
    return logins
```

---

### 📄 Langkah 3: `day05/main.py`  
*(Program utama — seperti skrip Bash yang panggil fungsi)*

```python
import logging
import os
import sys

# Setup logging sekali saja
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("day05/app.log"),
        logging.StreamHandler()
    ]
)

# Pastikan Python bisa import dari folder ini
sys.path.insert(0, os.path.dirname(__file__))

from utils.io_helper import read_lines, write_dict_to_csv
from log_parser import extract_ssh_logins

def main():
    LOG_INPUT = "day02/sample.log"      # reuse dari Day 02
    CSV_OUTPUT = "day05/ssh_logins.csv"

    logging.info("Mulai: parsing log SSH")
    
    # 1. Baca file
    lines = read_lines(LOG_INPUT)
    if lines is None:
        logging.critical("Gagal baca input → hentikan.")
        return

    # 2. Proses log
    logins = extract_ssh_logins(lines)

    # 3. Simpan hasil
    if not write_dict_to_csv(logins, CSV_OUTPUT, ['timestamp', 'ip']):
        logging.error("Gagal simpan hasil")
        return

    logging.info(f"Selesai! {len(logins)} login ditemukan.")

# Jalankan hanya kalau di-run langsung
if __name__ == "__main__":
    main()
```

---

### ▶️ Cara Jalankan:
```bash
# Pastikan struktur folder benar
mkdir -p day05/utils

# Simpan ketiga file
# Lalu:
python day05/main.py
```

### 🔍 Kenapa Ini Lebih Baik?
| Sebelum (Day 4) | Sesudah (Day 5) |
|------------------|------------------|
| Semua dalam 1 file | Terpisah: I/O, logika, eksekusi |
| Sulit dipakai ulang | Bisa `import log_parser` di proyek lain |
| Campur aduk tanggung jawab | Setiap file punya 1 tugas jelas |
| Mirip skrip cepat | Mirip **software engineer** |

> Ini gaya kerja **Data Engineer / SRE modern**: reusable, testable, scalable.

---

### ✅ Tugas Hari Ini:
1. Buat folder: `day05/` dan `day05/utils/`
2. Simpan ketiga file di atas
3. Jalankan `python day05/main.py`
4. Pastikan hasil muncul di:
   - Terminal
   - `day05/ssh_logins.csv`
   - `day05/app.log`
5. Commit & push ke GitHub

> Setelah selesai, balas: **“Day 5 done!”**

Besok (Hari 6): kita bikin **`requirements.txt` + virtual environment** — biar proyekmu bisa diinstall & dijalankan orang lain tanpa ribet. Ini standar wajib di industri!

Ayo terus — kamu sedang membangun **portofolio engineer, bukan cuma skrip!** 💪
