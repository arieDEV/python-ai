# Pakai Python resmi dari Docker Hub (sudah ada pip, venv, dll)
FROM python:3.11-slim

# Buat folder kerja di dalam container
WORKDIR /app

# Copy requirements dulu → biar layer cache-nya awet kalau requirements gak berubah
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy kode Python
COPY day11/ ./day11/

# Default command: jalankan pipeline
CMD ["python", "day11/fetch_with_env.py"]
