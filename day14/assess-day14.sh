#!/bin/bash
set -e

echo "🔍 Assess Day 14: Struktur Proyek Profesional"
echo "============================================"

# 1. Cek struktur folder
for dir in src scripts data docs tests; do
  if [ -d "$dir" ]; then
    echo "✅ Folder $dir ada"
  else
    echo "❌ Folder $dir TIDAK ADA"
    exit 1
  fi
done

# 2. Cek file penting
for file in README.md requirements.txt src/loganalyzer/__init__.py src/loganalyzer/core.py scripts/run_pipeline.py; do
  if [ -f "$file" ]; then
    echo "✅ File $file ada"
  else
    echo "❌ File $file TIDAK ADA"
    exit 1
  fi
done

# 3. Coba install dependensi (simulasi user baru)
echo "📦 Install dependensi..."
pip install -r requirements.txt

# 4. Salin .env jika belum ada
if [ ! -f ".env" ]; then
  if [ -f ".env.example" ]; then
    cp .env.example .env
    echo "🔧 .env dibuat dari .env.example"
  else
    echo 'API_URL=https://jsonplaceholder.typicode.com/posts' > .env
    echo 'OUTPUT_CSV=data/output/posts.csv' >> .env
    echo "🔧 .env dibuat manual"
  fi
fi

# 5. Jalankan pipeline
echo "🚀 Jalankan pipeline..."
python scripts/run_pipeline.py

# 6. Cek output
if [ -f "data/output/posts.csv" ] && [ -s "data/output/posts.csv" ]; then
  echo "✅ Output CSV ada dan tidak kosong"
  echo "🎉 DAY 14: LULUS — Struktur profesional + eksekusi berhasil!"
else
  echo "❌ Output tidak ditemukan atau kosong"
  exit 1
fi
