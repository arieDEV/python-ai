Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-4** dengan fokus:  
> **Error Handling + Logging — ala SysAdmin yang Production-Ready**

Ini adalah **langkah krusial** agar script Python-mu:
- Gak crash diam-diam  
- Meninggalkan jejak jelas (seperti syslog)  
- Bisa dipercaya di lingkungan otomasi (cron, pipeline, dll)

Dan tetap: **penjelasan di dalam kode**, langsung di barisnya — gaya mantan sysadmin.

---

## 🎯 **Hari 4: Tambahkan Error Handling & Logging ke Log Parser (Day 02)**

Kita ambil script dari **Day 02** (`parse_logs.py`) → lalu **upgrade** jadi versi yang siap produksi.

### 📂 Struktur Hari Ini:
- File utama: `day04/parse_logs_v2.py`
- Log file tetap pakai: `day02/sample.log` (reuse!)
- Output tetap: `day04/ssh_logins.csv`
- Tambahkan: file log error → `day04/app.log`

---

### 📄 `day04/parse_logs_v2.py`

```python
import re
import csv
import os
import logging  # ← ini modul logging bawaan Python

# Setup logging — mirip syslog, tapi di file
# Level INFO = info umum, ERROR = error kritis
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("day04/app.log"),   # simpan ke file
        logging.StreamHandler()                 # tampilkan di terminal juga
    ]
)

def parse_ssh_logs(log_filepath, output_csv):
    """
    Baca file log SSH, ekstrak login sukses (Accepted), simpan ke CSV.
    Dengan error handling & logging lengkap.
    """
    # Cek dulu: apakah file log input ADA?
    if not os.path.exists(log_filepath):
        # Jika tidak ada, tulis error & hentikan
        logging.error(f"File log tidak ditemukan: {log_filepath}")
        return  # keluar dari fungsi, gak lanjut proses

    try:
        # Coba baca file
        with open(log_filepath, 'r') as f:
            lines = f.readlines()
        logging.info(f"Membaca {len(lines)} baris dari {log_filepath}")
    except Exception as e:
        # Kalau gagal baca (izin, corrupt, dll), tangkap error-nya
        logging.error(f"Gagal membaca file {log_filepath}: {e}")
        return

    logins = []
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Accepted.*from\s+([0-9.]+)'

    for i, line in enumerate(lines, 1):  # enumerate → dapat nomor baris (buat debug)
        try:
            match = re.search(pattern, line)
            if match:
                timestamp = match.group(1)
                ip = match.group(2)
                logins.append({'timestamp': timestamp, 'ip': ip})
        except Exception as e:
            # Jika satu baris error, jangan hentikan semua — catat & lanjut
            logging.warning(f"Baris {i} tidak bisa diproses: {e} | Isi: {line.strip()}")

    # Simpan hasil ke CSV
    try:
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        with open(output_csv, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'ip']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(logins)
        logging.info(f"Berhasil: {len(logins)} login disimpan ke {output_csv}")
    except Exception as e:
        logging.error(f"Gagal menulis ke {output_csv}: {e}")
        return

# Jalankan hanya jika di-run langsung
if __name__ == "__main__":
    logging.info("=== Mulai parsing log SSH ===")
    parse_ssh_logs("day02/sample.log", "day04/ssh_logins.csv")
    logging.info("=== Selesai ===")
```

---

### 🔍 Penjelasan Kunci (Gaya SysAdmin):

| Konsep | Analogi SysAdmin |
|-------|------------------|
| `logging.info()` | Seperti `logger "info"` di bash → masuk syslog |
| `logging.error()` | Seperti `echo "ERROR" >&2` + catat di log |
| `try...except` | Seperti `if command; then ... else ... fi` — tangkap kegagalan |
| `return` saat error | Jangan lanjut proses kalau input rusak — safety first |
| `enumerate(lines, 1)` | Dapat nomor baris → cepat debug "baris ke-10 error" |

---

### ▶️ Cara Uji:
```bash
# Pastikan folder day04 ada
mkdir -p day04

# Jalankan
python day04/parse_logs_v2.py
```

### 📁 Output yang Dihasilkan:
- `day04/ssh_logins.csv` → hasil parsing
- `day04/app.log` → log lengkap, contoh isinya:
  ```
  2025-04-05 10:30:15,123 - INFO - === Mulai parsing log SSH ===
  2025-04-05 10:30:15,125 - INFO - Membaca 4 baris dari day02/sample.log
  2025-04-05 10:30:15,128 - INFO - Berhasil: 3 login disimpan ke day04/ssh_logins.csv
  2025-04-05 10:30:15,129 - INFO - === Selesai ===
  ```

> Coba ganti nama file input jadi `"day02/tidak_ada.log"` → lihat error di log!

---

### ✅ Tugas Hari Ini:
1. Buat folder `day04/`
2. Simpan kode di atas sebagai `day04/parse_logs_v2.py`
3. Jalankan
4. Commit & push ke GitHub

> Setelah selesai, balas: **“Day 4 done!”**

Besok (Hari 5): kita **modularisasi** kode — pisah jadi fungsi reusable, kayak bikin library kecil.  
Ini langkah penting biar kode gak jadi "spaghetti", dan bisa dipakai di banyak proyek (termasuk buat AI Trainer task!).

Ayo terus, Arie! Kamu sudah bikin tool yang **lebih baik dari banyak skrip produksi**. 🔧
