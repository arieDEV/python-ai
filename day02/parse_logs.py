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
