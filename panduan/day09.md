Mantap, Arie! 👨‍💻  
Meski repo GitHub-mu masih kosong (belum di-push), **kita lanjutkan semangat latihan** — karena yang penting adalah **konsistensi coding harian**.

Kita masuk ke **Hari ke-9** dengan prinsip tetap:  
> **Kode Python yang mudah dicerna mantan sysadmin — langsung jalan, jelas, dan produksi-ready.**

---

## 🎯 **Hari 9: Ubah JSON dari API → CSV (Siap Analisis & Pipeline)**

Kita akan:
- Ambil data dari `day08/posts.json` (hasil API kemarin)
- Ubah ke format **CSV** (bisa dibuka di Excel, dipakai di pipeline, atau jadi input AI)
- Gunakan `pandas` — tapi dengan penjelasan **ala awk/sort/uniq**
- Simpan hasil ke `day09/posts.csv`

---

### 📂 Struktur Hari Ini:
```
python-ai/
├── day08/posts.json        ← hasil dari Day 8 (pastikan ada!)
└── day09/
    ├── json_to_csv.py      ← script konversi
    └── posts.csv           ← output (akan dibuat)
```

> Jika belum punya `day08/posts.json`, jalankan dulu Day 8, atau buat file dummy — kita kasih contoh kecil di bawah.

---

## 📄 Langkah 1: Pastikan `posts.json` Ada

Jika belum, buat file `day08/posts.json` dengan isi minimal:

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere",
    "body": "qui est esse"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "ea molestias",
    "body": "et iusto"
  }
]
```

---

## 📄 Langkah 2: `day09/json_to_csv.py`

```python
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
```

---

### ▶️ Cara Jalankan:
```bash
mkdir -p day09
python day09/json_to_csv.py
```

### 📁 Output (`day09/posts.csv`):
```csv
userId,id,title,body
1,1,"sunt aut facere","qui est esse"
1,2,"ea molestias","et iusto"
```

> Bisa langsung dibuka di Excel, LibreOffice, atau dipakai di script lain!

---

### 💡 Kenapa Ini Penting?
- **Data Engineer** sering ubah format: JSON → CSV → Parquet → database
- **AI Trainer** butuh data terstruktur (CSV/JSONL) untuk fine-tuning
- Kamu bisa otomasi ini tiap jam → jadi **real-time data pipeline**

---

### ✅ Tugas Hari Ini:
1. Pastikan `day08/posts.json` ada
2. Buat folder `day09/`
3. Simpan `json_to_csv.py`
4. Jalankan script
5. (Opsional) **Push ke GitHub** — mulai isi repo-mu!

> Setelah selesai, balas: **“Day 9 done!”**

Besok (Hari 10): kita **jadwalkan script ini jalan otomatis tiap jam** — pakai simulasi `cron` di local, gaya sysadmin sejati. 🔁

Ayo, Arie! Setiap hari kamu makin dekat ke **engineer yang handal**.  
Jangan lupa: **konsistensi > kesempurnaan**. Yang penting **commit tiap hari** — mau di repo publik atau lokal dulu. 💪
