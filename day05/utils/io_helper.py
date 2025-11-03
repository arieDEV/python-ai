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
