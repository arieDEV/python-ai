import requests
import json
import os
import sys
import logging

# Setup logging simpel — seperti logger di bash
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

def fetch_json_from_api(url, timeout=10):
    """
    Ambil data dari API pakai GET.
    Mirip: curl -s "$url"
    """
    try:
        logging.info(f"📡 Mengambil data dari: {url}")
        response = requests.get(url, timeout=timeout)
        # Jika HTTP error (4xx/5xx), raise exception
        response.raise_for_status()
        return response.json()  # ubah JSON otomatis jadi dict/list Python
    except requests.exceptions.ConnectionError:
        logging.error("❌ Gagal koneksi ke internet atau server mati")
        return None
    except requests.exceptions.Timeout:
        logging.error("⏱️  Request timeout")
        return None
    except requests.exceptions.HTTPError as e:
        logging.error(f"🚫 HTTP Error: {e}")
        return None
    except json.JSONDecodeError:
        logging.error("💩 Respons bukan JSON valid")
        return None
    except Exception as e:
        logging.error(f"💥 Error tak terduga: {e}")
        return None

def save_to_json(data, filepath):
    """Simpan data Python (dict/list) ke file JSON"""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)  # indent=2 → rapi kayak di VS Code
        logging.info(f"✅ Data disimpan ke: {filepath}")
        return True
    except Exception as e:
        logging.error(f"❌ Gagal simpan ke {filepath}: {e}")
        return False

# Jalankan hanya kalau file ini di-run langsung
if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    OUTPUT_FILE = "day08/posts.json"

    data = fetch_json_from_api(API_URL)
    if data is not None:
        save_to_json(data, OUTPUT_FILE)
    else:
        logging.critical("Gagal ambil data → keluar")
        sys.exit(1)
