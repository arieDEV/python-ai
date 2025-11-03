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
