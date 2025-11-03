import os
import requests
import pandas as pd
from dotenv import load_dotenv  # baca .env
import logging

# Muat konfigurasi dari .env → jadi os.environ
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def fetch_and_save():
    # Ambil dari .env — jangan hardcode!
    api_url = os.getenv("API_URL")
    raw_dir = os.getenv("RAW_DATA_DIR")
    output_dir = os.getenv("OUTPUT_DIR")

    # Validasi: pastikan semua konfig ada
    if not all([api_url, raw_dir, output_dir]):
        logging.error("❌ Konfigurasi .env tidak lengkap!")
        return False

    json_path = os.path.join(raw_dir, "posts.json")
    csv_path = os.path.join(output_dir, "posts.csv")

    # 1. Ambil data
    try:
        logging.info(f"📡 Ambil dari: {api_url}")
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logging.error(f"❌ Gagal ambil API: {e}")
        return False

    # 2. Simpan JSON
    os.makedirs(raw_dir, exist_ok=True)
    with open(json_path, 'w') as f:
        f.write(resp.text)
    logging.info(f"💾 JSON: {json_path}")

    # 3. Konversi ke CSV
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False)
    logging.info(f"✅ CSV: {csv_path}")

    return True

if __name__ == "__main__":
    logging.info("=== Pipeline dengan .env ===")
    fetch_and_save()
