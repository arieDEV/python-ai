Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-3** dengan semangat yang sama:  
> **Python yang mudah dicerna mantan sysadmin** → jelas, langsung jalan, relevan, dan *no magic*.

---

## 🎯 **Hari 3: Data Exploration dengan Pandas (SysAdmin Style)**  
**Tujuan**:  
Baca dataset YouTube (CSV) → hitung **rata-rata views per kategori** → tampilkan & simpan hasil.  

Ini dasar **Data Engineering / Analytics**, tapi kita pakai cara yang familiar:
- Seperti `awk`, `sort`, `uniq` — tapi di Python
- Output jelas: angka, tabel, file
- Tanpa teori berat

---

### 📂 Struktur Hari Ini:
- Folder: `day03/`
- File:
  - `youtube_top.csv` ← dataset (kita sediakan contoh kecil)
  - `explore_yt.py` ← script utama

---

### 📄 Langkah 1: Buat `day03/youtube_top.csv`  
(Supaya gak perlu download dari internet — langsung jalan)

```csv
video_id,category,views,likes
v1,Music,1500000,45000
v2,Entertainment,950000,25000
v3,Music,2100000,60000
v4,News,300000,8000
v5,Entertainment,1200000,32000
v6,Music,800000,22000
v7,News,400000,10000
```

> 7 baris aja — cukup buat latihan.

---

### 📄 Langkah 2: `day03/explore_yt.py`  
**Semua penjelasan ada di komentar — langsung di baris kode.**

```python
# Pandas = seperti "awk + sort + uniq" tapi di Python, untuk data terstruktur
import pandas as pd

def analyze_youtube_data(csv_path, output_path):
    # Baca file CSV → jadi tabel di memori (mirip database kecil)
    df = pd.read_csv(csv_path)
    # df = "data frame" → tabel dengan baris & kolom

    # Tampilkan 3 baris pertama (seperti `head -3`)
    print("🔍 3 baris pertama:")
    print(df.head(3))
    print()

    # Hitung rata-rata views per category
    # groupby("category") → kelompokkan berdasarkan kolom 'category'
    # .mean(numeric_only=True) → hitung rata-rata hanya kolom angka (views, likes)
    avg_by_cat = df.groupby("category").mean(numeric_only=True)
    
    # Reset index → biar 'category' jadi kolom biasa (bukan label baris)
    # Ini biar gampang disimpan ke CSV nanti
    avg_by_cat = avg_by_cat.reset_index()

    print("📊 Rata-rata per kategori:")
    print(avg_by_cat)
    print()

    # Simpan hasil ke file CSV (bisa dibuka di Excel / dipakai pipeline lain)
    avg_by_cat.to_csv(output_path, index=False)
    # index=False → jangan tulis nomor baris (kayak `awk '{print $0}'` tanpa NR)

    print(f"✅ Hasil disimpan ke: {output_path}")

# Jalankan hanya kalau file ini di-run langsung (bukan di-import)
if __name__ == "__main__":
    analyze_youtube_data("day03/youtube_top.csv", "day03/avg_views_by_category.csv")
```

---

### ▶️ Cara Jalankan:
```bash
python day03/explore_yt.py
```

### 🖨️ Output yang Diharapkan:
```
🔍 3 baris pertama:
  video_id     category   views  likes
0       v1        Music 1500000  45000
1       v2 Entertainment  950000  25000
2       v3        Music 2100000  60000

📊 Rata-rata per kategori:
     category        views        likes
0 Entertainment  1075000.0  28500.0
1        Music  1466666.67  42333.33
2         News   350000.0   9000.0

✅ Hasil disimpan ke: day03/avg_views_by_category.csv
```

Dan file `avg_views_by_category.csv` akan berisi:
```csv
category,views,likes
Entertainment,1075000.0,28500.0
Music,1466666.6666666667,42333.333333333336
News,350000.0,9000.0
```

---

### 🔧 Instalasi Pandas (Kalau Belum)
```bash
pip install pandas
```
> Pandas otomatis bawa `numpy` — cukup ini aja.

---

### 💡 Kenapa Ini Relevan Buat Kamu?
- Kamu sering lihat log, metrics, data numerik → ini cara **otomasi analisis**.
- Output CSV bisa dipakai buat:
  - Grafik di Grafana
  - Input model AI (nanti)
  - Laporan mingguan otomatis
- Ini **dasar Data Engineering**: baca → proses → simpan → pakai.

---

### ✅ Tugas Hari Ini:
1. Buat folder `day03/`
2. Simpan `youtube_top.csv` dan `explore_yt.py`
3. Jalankan script
4. Commit & push ke GitHub

> Setelah selesai, balas: **“Day 03 done!”**  
> Besok kita tambah **error handling + logging** (mirip syslog tapi di Python) — biar jadi tool production-grade.

Ayo, Arie! Ini sudah mulai mirip **tools internal** yang biasa kamu bangun di lingkungan sysadmin, hanya saja sekarang skalanya bisa ke **data besar**. 💪
