#!/bin/bash
# Simulasi cron: jalan tiap jam (tapi kita jalan manual dulu)
# Simpan di root repo

echo "🕒 [$(date)] Menjalankan data pipeline..."
cd "$(dirname "$0")" || exit 1

# Aktifkan venv dulu (pastikan ada!)
source ~/Desktop/ai-env/bin/activate      # aktifkan

# Jalankan Python
python data_pipeline/fetch_and_convert.py

echo "✅ Simulasi cron selesai."
