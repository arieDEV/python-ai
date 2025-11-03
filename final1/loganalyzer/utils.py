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
