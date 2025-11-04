#!/bin/bash
# Jalankan pipeline di dalam Docker — tanpa install Python di host!

set -e  # berhenti kalau ada error

echo "🐳 Build Docker image..."
docker build -t loganalyzer-pipeline .

echo "📁 Buat folder output di host..."
mkdir -p ./day11/raw ./day11/output

echo "🚀 Jalankan container dengan akses ke folder local..."
docker run \
  --rm \
  --env-file ./day11/.env \
  -v "$(pwd)/day11:/app/day11" \
  loganalyzer-pipeline

echo "✅ Selesai! Cek folder day11/output/"
