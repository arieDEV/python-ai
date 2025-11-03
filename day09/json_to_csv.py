import pandas as pd
import os
import sys
import logging

# Setup logging simpel — seperti echo + logger
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def json_to_csv(json_path, csv_path):
    """
    Baca JSON → jadi tabel → simpan ke CSV.
    Analogi sysadmin: 
      cat data.json | jq -r '... | @csv' > data.csv
    Tapi di Python, lebih aman & otomatis.
    """
    if not os.path.exists(json_path):
        logging.error(f"❌ File tidak ditemukan: {json_path}")
        return False

    try:
        # Baca JSON → jadi DataFrame (tabel di memori)
        df = pd.read_json(json_path)
        logging.info(f"📊 Berhasil baca {len(df)} baris dari {json_path}")

        # Simpan ke CSV
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df.to_csv(csv_path, index=False)  # index=False → jangan tulis nomor baris
        logging.info(f"✅ CSV disimpan ke: {csv_path}")
        return True

    except ValueError as e:
        logging.error(f"💔 Format JSON tidak valid: {e}")
        return False
    except Exception as e:
        logging.error(f"💥 Error: {e}")
        return False

if __name__ == "__main__":
    JSON_INPUT = "day08/posts.json"
    CSV_OUTPUT = "day09/posts.csv"

    success = json_to_csv(JSON_INPUT, CSV_OUTPUT)
    if not success:
        logging.critical("Gagal konversi → keluar")
        sys.exit(1)
