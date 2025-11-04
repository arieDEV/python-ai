import requests
import csv
import os
import logging

# Setup logging simpel
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

# Kolom wajib & tipe data yang diharapkan
REQUIRED_FIELDS = {
    'id': int,
    'userId': int,
    'title': str,
    'body': str
}

def is_valid_record(record):
    """
    Validasi 1 record:
    - Semua kolom wajib ada
    - Tipe data sesuai
    Return: (valid: bool, error_msg: str)
    """
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in record:
            return False, f"❌ Kolom '{field}' tidak ada"
        
        value = record[field]
        if not isinstance(value, expected_type):
            # Izinkan string angka → convert ke int (misal: "123" → 123)
            if expected_type == int and isinstance(value, str) and value.isdigit():
                record[field] = int(value)  # perbaiki di tempat
            else:
                return False, f"❌ Kolom '{field}' harus {expected_type.__name__}, dapat {type(value).__name__}: {value}"
    return True, ""

def fetch_and_validate():
    URL = "https://jsonplaceholder.typicode.com/posts"
    OUTPUT_CSV = "day13/validated_output.csv"
    
    # 1. Ambil data
    try:
        resp = requests.get(URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        logging.info(f"📡 Ambil {len(data)} record dari API")
    except Exception as e:
        logging.error(f"💥 Gagal ambil data: {e}")
        return

    # 2. Validasi & filter
    valid_records = []
    invalid_count = 0

    for i, record in enumerate(data, 1):
        is_valid, error = is_valid_record(record)
        if is_valid:
            valid_records.append(record)
        else:
            invalid_count += 1
            logging.warning(f"⚠️  Baris {i}: {error} → dilewati")

    logging.info(f"✅ {len(valid_records)} valid | ❌ {invalid_count} tidak valid")

    # 3. Simpan hanya data valid
    if valid_records:
        os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
        fieldnames = list(REQUIRED_FIELDS.keys())
        with open(OUTPUT_CSV, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_records)
        logging.info(f"💾 Data valid disimpan ke: {OUTPUT_CSV}")
    else:
        logging.warning("📭 Tidak ada data valid untuk disimpan")

if __name__ == "__main__":
    logging.info("=== Pipeline dengan Validasi Data ===")
    fetch_and_validate()
