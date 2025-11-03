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
