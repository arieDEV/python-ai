import requests
import pandas as pd
import os
import sys
import logging
from datetime import datetime

# Buat folder logs jika belum ada
os.makedirs("data_pipeline/logs", exist_ok=True)

# Setup logging ke file + terminal
log_file = f"data_pipeline/logs/pipeline_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def fetch_and_save_to_csv():
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    JSON_OUT = "data_pipeline/raw/posts.json"
    CSV_OUT = "data_pipeline/output/posts.csv"

    # 1. Ambil data dari API
    try:
        logging.info("📡 Mulai: ambil data dari API")
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        logging.info(f"✅ Berhasil ambil {len(data)} data")
    except Exception as e:
        logging.error(f"❌ Gagal ambil data: {e}")
        return False

    # 2. Simpan ke JSON
    try:
        os.makedirs(os.path.dirname(JSON_OUT), exist_ok=True)
        with open(JSON_OUT, 'w') as f:
            f.write(resp.text)
        logging.info(f"💾 JSON disimpan: {JSON_OUT}")
    except Exception as e:
        logging.error(f"❌ Gagal simpan JSON: {e}")
        return False

    # 3. Konversi ke CSV
    try:
        df = pd.read_json(JSON_OUT)
        os.makedirs(os.path.dirname(CSV_OUT), exist_ok=True)
        df.to_csv(CSV_OUT, index=False)
        logging.info(f"✅ CSV siap: {CSV_OUT}")
    except Exception as e:
        logging.error(f"❌ Gagal konversi ke CSV: {e}")
        return False

    logging.info("🎉 Pipeline selesai sukses!")
    return True

if __name__ == "__main__":
    logging.info("=== JALANKAN DATA PIPELINE HARI INI ===")
    success = fetch_and_save_to_csv()
    if not success:
        sys.exit(1)
