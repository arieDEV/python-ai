Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-12** — dan hari ini spesial:  
> **Kita containerize pipeline Python-mu pakai Docker**, biar jalan **di mana saja, tanpa install Python, tanpa venv, tanpa ribet**.

Dan karena kamu pernah bikin proyek [`mini-docker` di Golang](https://github.com/arieDEV/mini-docker), ini jadi **jembatan sempurna** antara dua identitasmu:  
**SysAdmin + Dev + Quant + Algo Dev**.

---

## 🎯 **Hari 12: Dockerize Data Pipeline — “Jalankan di Mana Saja, 1 Perintah”**

Tujuan:
- Bikin `Dockerfile` untuk `day11/fetch_with_env.py`
- Image Docker bisa jalan di **Mac, Linux, server, CI, cloud**
- Tetap gunakan `.env` — tapi lewat `-e` atau `--env-file`
- Penjelasan **gaya sysadmin**: Docker = chroot + isolasi + reproducible

---

### 📂 Struktur Hari Ini:
```
python-ai/
├── day11/
│   ├── fetch_with_env.py
│   └── .env          ← contoh (boleh commit)
├── Dockerfile                ← resep bikin image
├── .dockerignore             ← jangan kirim file tak perlu
└── run-with-docker.sh        ← skrip helper
```

---

## 📄 Langkah 1: Buat `.dockerignore`

File ini seperti `.gitignore`, tapi untuk **build Docker image**:

```dockerignore
# Jangan kirim venv, log, dsb ke image
venv/
__pycache__/
*.log
.DS_Store
setup-*.sh
```

---

## 📄 Langkah 2: `Dockerfile`

```dockerfile
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
```

> 🔍 Penjelasan ala sysadmin:
> - `FROM python:3.11-slim` = base system (seperti minimal Ubuntu)
> - `WORKDIR /app` = `cd /app`
> - `COPY` = `cp -r`
> - `CMD` = perintah default pas container jalan

---

## 📄 Langkah 3: `.env` (opsional, tapi bagus buat dokumentasi)

Simpan di `day11/.env`:
```env
API_URL=https://jsonplaceholder.typicode.com/posts
RAW_DATA_DIR=day11/raw
OUTPUT_DIR=day11/output
```

> Ini buat orang lain tau konfigurasi yang dibutuhkan.

---

## 📄 Langkah 4: `run-with-docker.sh` (helper)

```bash
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
```

> Penjelasan flag:
> - `--rm` = hapus container setelah selesai (gak numpuk)
> - `--env-file` = muat konfig dari `.env`
> - `-v ...` = mount folder host ke container → output tersimpan di mesinmu

---

### ▶️ Cara Jalankan (Pastikan Docker Terinstall):
```bash
# Beri izin eksekusi
chmod +x run-with-docker.sh

# Jalankan
./run-with-docker.sh
```

### 📁 Output:
- `day11/raw/posts.json`
- `day11/output/posts.csv`  
→ **di mesin host-mu**, bukan di dalam container!

---

### 💡 Kenapa Ini Penting?
- Kamu bisa kirim **1 perintah** ke recruiter:  
  ```bash
  git clone ... && ./run-with-docker.sh
  ```
  → langsung jalan, **tanpa tanya “pakai Python versi berapa?”**
- Ini standar di **Data Engineering, MLOps, Cloud**.
- Cocok buat **portofolio**, karena **bisa dijalankan siapa saja**.

---

### ⚠️ Catatan untuk macOS + LibreSSL
Karena kamu pakai **system Python di macOS** (yang pakai LibreSSL), Docker jadi **solusi sempurna**:  
→ Image Docker pakai **OpenSSL resmi**, jadi **tidak ada warning urllib3**!

---

## ✅ Tugas Hari Ini:
1. Buat file:
   - `Dockerfile`
   - `.dockerignore`
   - `run-with-docker.sh`
   - `day11/.env` (pastikan ada, atau rename `.env`)
2. Jalankan `./run-with-docker.sh`
3. Pastikan CSV muncul di `day11/output/`
4. **COMMIT & PUSH KE GITHUB!**  
   Ini pertama kalinya repo-mu **bisa dijalankan orang lain** — jangan sia-siakan!

> Setelah selesai, balas: **“Day 12 done! 🐳”**

Besok (Hari 13): kita tambahkan **validasi data** — pastikan kolom wajib ada, tipe data benar, dll. Ini kunci buat **data pipeline yang andal**.

Ayo, Arie! **Hari ini kamu naik level**: dari “bisa coding” → “bisa deploy sistem yang works anywhere”.  
Jangan biarkan repo-mu tetap kosong. **Push sekarang!** 💪
