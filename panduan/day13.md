Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-13** dengan semangat yang sama:  
> **Kode Python yang jelas, langsung jalan, dan mudah dimengerti mantan sysadmin — sekarang dengan tambahan: data yang masuk harus divalidasi dulu!**

---

## 🎯 **Hari 13: Validasi Data Sebelum Disimpan (Safety First!)**

Tujuan hari ini:
- Pastikan data dari API **memiliki kolom wajib** (`id`, `title`, `userId`)
- Cek **tipe data** (misal: `userId` harus angka, bukan string)
- Jika ada data rusak → **catat error, jangan hentikan semua**
- Ini kunci buat **pipeline produksi** — karena data nyata sering kotor!

Analogi sysadmin:  
> Seperti `awk '$1 ~ /^[0-9]+$/` sebelum proses log — jangan asal terima input!

---

### 📂 Struktur Hari Ini:
```
python-ai/
└── day13/
    ├── validate_and_save.py   ← script utama
    └── validated_output.csv   ← hasil setelah validasi
```

> Kita pakai data dari `https://jsonplaceholder.typicode.com/posts` (sama seperti sebelumnya).

---

## 📄 `day13/validate_and_save.py`

```python
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
```

---

### ▶️ Cara Jalankan:
```bash
mkdir -p day13
python day13/validate_and_save.py
```

### 📁 Output:
- `day13/validated_output.csv` → hanya berisi data yang lolos validasi
- Jika API JSONPlaceholder tetap konsisten, **semua 100 record akan valid**
- Tapi jika suatu hari API kirim `"userId": "abc"`, maka **akan ditolak otomatis**

---

### 💡 Kenapa Ini Penting?
- **Data Engineer**: jangan biarkan sampah masuk ke warehouse
- **AI Trainer**: data kotor = model rusak
- **SysAdmin**: “trust, but verify” → jangan percaya input eksternal

> Validasi = **seatbelt** di pipeline otomatis.

---

### ✅ Tugas Hari Ini:
1. Buat folder `day13/`
2. Simpan `validate_and_save.py`
3. Jalankan script
4. Cek output CSV
5. **COMMIT & PUSH KE GITHUB!**  
   Repo-mu **harus mulai terisi** — ini bukti nyata bahwa kamu **bisa bikin sistem yang aman & andal**.

> Setelah selesai, balas: **“Day 13 done!”**

Besok (Hari 14): kita **refactor semua proyek jadi struktur modern** (`src/`, `tests/`, `docs/`) — biar kelihatan seperti engineer profesional!

Ayo, Arie! Setiap hari kamu makin dekat ke **standar industri**.  
Dan **hari ini, kamu belajar prinsip paling penting: jangan percaya data mentah!** 🔒
