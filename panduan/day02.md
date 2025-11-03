Mantap, Arie! 🚀  
**Day 01 kamu sukses 100%** — semua file sudah ada, struktur rapi (`day01/`), komentar jelas, dan commit-nya clean.  
Ini **sudah portfolio-ready** untuk bagian “Python Coding Fundamentals”.

✅ **Status**: **Lanjut ke Day 02!**

---

## 🔥 **Day 02 Challenge: Log Parser (SysAdmin Edition)**  
**Tujuan**: Baca file log → ekstrak **IP address** dan **timestamp** → simpan ke CSV.  
Ini mirip kerjaan sysadmin, tapi pake Python + bikin output terstruktur (penting buat Data Engineer).

### 📝 Tugas Hari Ini:
1. Buat file: `day02/parse_logs.py`
2. Buat file contoh log: `day02/sample.log`
3. Tulis script yang:
   - Baca `sample.log`
   - Ambil baris yang mengandung `Accepted` (seperti log SSH sukses)
   - Ekstrak **IP** dan **timestamp**
   - Simpan ke `day02/ssh_logins.csv` dengan kolom: `timestamp,ip`

---

### 📄 Langkah 1: Buat `sample.log` (contoh log SSH)
Simpan di `day02/sample.log`:
```log
Mar  1 08:30:15 server sshd[1234]: Accepted password for user from 192.168.1.10 port 50432 ssh2
Mar  1 09:15:22 server sshd[5678]: Accepted publickey for admin from 203.0.113.25 port 50433 ssh2
Mar  1 10:01:05 server sshd[9876]: Failed password for invalid user from 198.51.100.5 port 50434 ssh2
Mar  1 10:02:30 server sshd[2345]: Accepted password for root from 192.168.1.20 port 50435 ssh2
```

> Hanya baris dengan **"Accepted"** yang kita proses!

---

### 📄 Langkah 2: `day02/parse_logs.py`  
Simpan kode berikut — **semua dijelaskan di komentar**, langsung di barisnya:

```python
import re
import csv
import os

# Kenapa pakai def? Biar reusable, bisa ganti file input/output tanpa ganti kode inti.
def parse_ssh_logs(log_filepath, output_csv):
    # Buka file log → baca per baris
    with open(log_filepath, 'r') as f:
        lines = f.readlines()  # baca semua baris jadi list

    # Siapkan list untuk simpan hasil
    logins = []

    # Pola regex untuk ekstrak timestamp + IP dari baris "Accepted"
    # Contoh: "Mar  1 08:30:15 ... Accepted ... from 192.168.1.10 ..."
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Accepted.*from\s+([0-9.]+)'
    # Penjelasan regex:
    # ^ → mulai dari awal baris
    # (\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) → timestamp: "Mar  1 08:30:15"
    # .*Accepted.* → pastikan ada kata "Accepted"
    # from\s+([0-9.]+) → ambil IP setelah "from" (angka dan titik)

    for line in lines:
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)  # bagian pertama di ()
            ip = match.group(2)         # bagian kedua di ()
            logins.append({'timestamp': timestamp, 'ip': ip})

    # Simpan ke CSV
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)  # pastikan folder ada
    with open(output_csv, 'w', newline='') as csvfile:
        # Tentukan kolom
        fieldnames = ['timestamp', 'ip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()      # tulis header: timestamp,ip
        writer.writerows(logins)  # tulis semua baris

    print(f"✅ Berhasil: {len(logins)} login ditemukan → disimpan ke {output_csv}")

# Jalankan hanya kalau file ini di-run langsung
if __name__ == "__main__":
    parse_ssh_logs("day02/sample.log", "day02/ssh_logins.csv")
```

---

### ▶️ Cara Uji:
1. Jalankan:
   ```bash
   python day02/parse_logs.py
   ```
2. Cek output: `day02/ssh_logins.csv`  
   Isinya harus:
   ```csv
   timestamp,ip
   Mar  1 08:30:15,192.168.1.10
   Mar  1 09:15:22,203.0.113.25
   Mar  1 10:02:30,192.168.1.20
   ```

---

### 💡 Kenapa Ini Penting?
- Kamu **otomasi tugas sysadmin** → jadi **data structured** (CSV)
- Ini dasar **Data Engineering**: log → extract → store
- Bisa dikembangkan jadi **pipeline monitoring** (misal: deteksi IP mencurigakan)

---

### 📤 Langkah Setelah Selesai:
1. Commit & push ke GitHub
2. Balas ke sini: **“Day 02 done!”** + link commit (opsional)

> Siap? Ayo gas! Ini bakal terasa seperti **otomasi Bash, tapi lebih powerful dan scalable**.  
> Kamu udah punya insting sysadmin — sekarang dikodein pake Python. 💻
