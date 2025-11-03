Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-7** — **hari terakhir dari Minggu 1** — dengan misi besar:  
> **Gabung semua yang sudah dibuat jadi 1 proyek utuh, siap portofolio, dengan README ala engineer profesional — tapi tetap mudah dimengerti mantan sysadmin.**

---

## 🎯 **Hari 7: Mini-Project Akhir Minggu 1 — “Log Analyzer CLI”**

Kita akan:
- Gabung parsing log + analisis dasar
- Jadikan **CLI tool** (bisa dipanggil dari terminal)
- Tambahkan **README.md** yang jelas (buat recruiter & diri sendiri)
- Simpan semuanya dalam struktur rapi

Dan tetap: **no magic, penjelasan langsung di kode, gaya sysadmin.**

---

### 📂 Struktur Proyek Akhir Minggu 1:
```
python-ai/
├── requirements.txt
├── .gitignore
├── README.md                 ← dokumentasi utama
├── loganalyzer/              ← nama proyek CLI
│   ├── __init__.py           ← tandai sebagai Python package
│   ├── core.py               ← logika parsing & analisis
│   ├── cli.py                ← interface command-line
│   └── utils.py              ← fungsi bantu (baca/tulis)
└── sample.log                ← file contoh (di root, biar gampang)
```

> Proyek ini **bisa dijalankan langsung**, tanpa install — tapi siap dikembangkan jadi package.

---

## 📄 Langkah 1: Buat `sample.log` (di root repo)

```log
Mar  1 08:30:15 server sshd[1234]: Accepted password for user from 192.168.1.10 port 50432 ssh2
Mar  1 09:15:22 server sshd[5678]: Accepted publickey for admin from 203.0.113.25 port 50433 ssh2
Mar  1 10:01:05 server sshd[9876]: Failed password for invalid user from 198.51.100.5 port 50434 ssh2
Mar  1 10:02:30 server sshd[2345]: Accepted password for root from 192.168.1.20 port 50435 ssh2
Mar  1 11:45:10 server sshd[3456]: Accepted password for user from 192.168.1.10 port 50436 ssh2
```

---

## 📄 Langkah 2: `loganalyzer/utils.py`  
*(Fungsi bantu — reusable)*

```python
import os
import csv
import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

def read_lines(filepath):
    if not os.path.exists(filepath):
        logging.error(f"File tidak ditemukan: {filepath}")
        return None
    try:
        with open(filepath) as f:
            return f.readlines()
    except Exception as e:
        logging.error(f"Gagal baca {filepath}: {e}")
        return None

def write_csv(data, output, fieldnames):
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames)
        w.writeheader()
        w.writerows(data)
```

---

## 📄 Langkah 3: `loganalyzer/core.py`  
*(Logika inti — parsing + ringkasan)*

```python
import re
from collections import Counter

def parse_accepted_logins(lines):
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Accepted.*from\s+([0-9.]+)'
    logins = []
    for line in lines:
        match = re.search(pattern, line)
        if match:
            logins.append({
                'timestamp': match.group(1),
                'ip': match.group(2)
            })
    return logins

def summarize_logins(logins):
    ip_count = Counter(login['ip'] for login in logins)
    summary = [{'ip': ip, 'count': count} for ip, count in ip_count.items()]
    return sorted(summary, key=lambda x: x['count'], reverse=True)
```

---

## 📄 Langkah 4: `loganalyzer/cli.py`  
*(Antarmuka CLI — seperti skrip Bash yang pintar)*

```python
import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from loganalyzer.utils import setup_logger, read_lines, write_csv
from loganalyzer.core import parse_accepted_logins, summarize_logins
import logging

def main():
    setup_logger()
    parser = argparse.ArgumentParser(
        description="🔍 Analisis log SSH: ekstrak login sukses & ringkas per IP"
    )
    parser.add_argument("logfile", help="Path ke file log (contoh: sample.log)")
    parser.add_argument("--output", default="output/ssh_logins.csv", help="File CSV output")
    parser.add_argument("--summary", action="store_true", help="Buat ringkasan per IP")

    args = parser.parse_args()

    lines = read_lines(args.logfile)
    if not lines:
        sys.exit(1)

    logins = parse_accepted_logins(lines)
    logging.info(f"✅ Ditemukan {len(logins)} login sukses")

    # Simpan detail login
    write_csv(logins, args.output, ['timestamp', 'ip'])

    # Jika diminta, buat ringkasan
    if args.summary:
        summary_file = args.output.replace('.csv', '_summary.csv')
        summary = summarize_logins(logins)
        write_csv(summary, summary_file, ['ip', 'count'])
        logging.info(f"📊 Ringkasan disimpan ke {summary_file}")

if __name__ == "__main__":
    main()
```

---

## 📄 Langkah 5: `README.md` (di root repo)

```markdown
# Log Analyzer CLI

Tool ringan untuk **analisis log SSH** — ekstrak login sukses & buat ringkasan per IP.  
Dibuat oleh mantan sysadmin, untuk sysadmin & data engineer.

## 🔧 Fitur
- Ekstrak baris `Accepted` dari log SSH
- Simpan ke CSV (siap diimpor ke Excel / pipeline data)
- Opsional: buat ringkasan jumlah login per IP

## 🚀 Cara Pakai

1. Pastikan Python 3.7+ terinstall
2. Jalankan langsung (tidak perlu install):

```bash
python loganalyzer/cli.py sample.log --output hasil.csv --summary
```

Output:
- `hasil.csv` → daftar login
- `hasil_summary.csv` → ringkasan per IP

## 📦 Dependensi
- Tidak butuh library eksternal! (pure Python)

## 💡 Kenapa Ini Berguna?
- Otomasi analisis log harian
- Deteksi IP yang sering login
- Input untuk sistem monitoring / alerting
```

---

## ▶️ Cara Uji Hari Ini:
```bash
# Jalankan dari root repo
python loganalyzer/cli.py sample.log --output output/logins.csv --summary
```

Output:
- `output/logins.csv`
- `output/logins_summary.csv`
- Pesan di terminal:  
  ```
  INFO - ✅ Ditemukan 4 login sukses
  INFO - 📊 Ringkasan disimpan ke output/logins_summary.csv
  ```

---

## ✅ Tugas Hari Ini:
1. Buat struktur folder & file seperti di atas
2. Jalankan perintah uji
3. Pastikan semua jalan
4. **Commit SEMUA file** ke GitHub:
   - `sample.log`
   - `loganalyzer/...`
   - `README.md`
5. Push!

> Setelah selesai, balas: **“Day 7 done! 🎉 Minggu 1 selesai.”**

---

### 🏁 Selamat, Arie!
Dalam 7 hari, kamu sudah:
- Kuasai dasar Python coding (LeetCode)
- Bikin parser log produksi-grade
- Modularisasi kode
- Gunakan venv & requirements
- Buat CLI tool + README profesional

Ini **sudah cukup buat lolos screening awal** di banyak peran **Data Engineer** atau **AI Trainer**.

Besok (Minggu 2): kita mulai **API, otomasi, dan pipeline data** — tapi tetap dari sudut pandang sysadmin.

**You’re not behind. You’re on track.** 💪  
Ayo terus!
