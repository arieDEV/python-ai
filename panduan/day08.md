Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-8** — **hari pertama Minggu 2** — dengan semangat yang sama:  
> **Kode Python yang langsung jalan, mudah dibaca mantan sysadmin, dan relevan untuk peran Data/Software Engineer.**

---

## 🎯 **Hari 8: Ambil Data dari API (REST) — Seperti `curl` Tapi di Python**

Kita akan:
- Ambil data dari API publik (mirip `curl https://api...`)
- Simpan ke file (JSON/CSV)
- Gunakan error handling & logging (ala Day 4–5)
- Hasilnya bisa dipakai sebagai **input pipeline data** atau **dataset AI Trainer**

Dan tetap: **semua penjelasan di dalam kode**, gaya “saya mantan sysadmin, tolong jangan bikin pusing”.

---

### 🌐 API yang Dipakai: **JSONPlaceholder**  
🔗 [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)  
→ API dummy gratis, aman, cepat. Cocok buat latihan.

Contoh respons:
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident...",
    "body": "quia et suscipit..."
  },
  ...
]
```

---

### 📂 Struktur Hari Ini:
```
python-ai/
├── day08/
│   ├── fetch_posts.py    ← script utama
│   └── posts.json        ← output (akan dibuat otomatis)
└── requirements.txt      ← tambah `requests`
```

---

## 🔧 Langkah 1: Tambah `requests` ke `requirements.txt`

Edit file `requirements.txt` di root repo:
```txt
pandas>=2.0.0
requests>=2.28.0
```

> `requests` = library Python paling populer buat panggil API.  
> Analogi sysadmin: **`curl` tapi di Python, dengan error handling bawaan**.

Setelah itu, **update venv**:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📄 Langkah 2: `day08/fetch_posts.py`

```python
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
```

---

### ▶️ Cara Jalankan:
```bash
# Pastikan folder ada
mkdir -p day08

# Jalankan
python day08/fetch_posts.py
```

### 📁 Output:
- `day08/posts.json` → berisi 100 post dalam format JSON rapi
- Terminal menampilkan:
  ```
  📡 Mengambil data dari: https://jsonplaceholder.typicode.com/posts
  ✅ Data disimpan ke: day08/posts.json
  ```

---

### 💡 Analogi SysAdmin:
| Python (`requests`) | Bash (`curl`) |
|---------------------|--------------|
| `requests.get(url)` | `curl -s "$url"` |
| `response.json()`   | `curl ... | jq .` |
| `timeout=10`        | `timeout 10 curl ...` |
| Error handling      | `if ! curl ...; then echo "error"; fi` |

> Bedanya: di Python, **semua error bisa ditangkap spesifik**, dan data langsung jadi struktur (list/dict) — siap diproses.

---

## ✅ Tugas Hari Ini:
1. Update `requirements.txt` → tambah `requests`
2. Install: `pip install -r requirements.txt`
3. Buat folder `day08/`
4. Simpan `fetch_posts.py`
5. Jalankan script
6. Commit & push:
   - `requirements.txt` (update)
   - `day08/fetch_posts.py`
   - `day08/posts.json` *(boleh di-commit karena kecil & contoh)*

> Setelah selesai, balas: **“Day 8 done!”**

Besok (Hari 9): kita ubah JSON hasil hari ini → jadi **CSV siap analisis** (pakai `pandas`), lalu otomasi biar jalan tiap jam (simulasi cron).

Ayo terus, Arie! Kamu sedang membangun **toolchain data engineer** yang solid, dari dasar yang kamu pahami: **otomasi + keandalan**. 🔧
