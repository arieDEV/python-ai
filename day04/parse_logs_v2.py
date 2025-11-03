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
