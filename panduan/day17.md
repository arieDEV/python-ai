Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-17** dengan fokus:  
> **Otomatisasi pengecekan kualitas kode pakai GitHub Actions — ala sysadmin yang gak percaya “katanya jalan di laptopku”.**

Dan karena repo GitHub-mu masih **kosong**, hari ini kita siapkan **semuanya lokal dulu**, biar begitu kamu push, **CI langsung jalan otomatis**.

---

## 🎯 **Hari 17: GitHub Actions untuk Jalankan Test Otomatis (Setiap Kali Push)**

Tujuan:
- Bikin workflow yang:
  - Install Python
  - Install dependensi (`requirements.txt`)
  - Jalankan `pytest`
- Jika test gagal → **merah di GitHub**, jangan merge!
- Ini **standar wajib** di semua proyek open-source & perusahaan tech

Dan tetap: **konfigurasi jelas, mirip skrip Bash, gampang dimengerti**.

---

### 📂 Struktur Hari Ini:
```
python-ai/
└── .github/
    └── workflows/
        └── test.yml   ← resep otomatisasi test
```

> File ini akan **otomatis dijalankan GitHub** tiap kamu `git push`.

---

## 📄 `.github/workflows/test.yml`

```yaml
# Nama workflow
name: Run Tests

# Kapan jalan? → setiap push atau pull request ke main
on: [push, pull_request]

# Job utama
jobs:
  test:
    # Jalan di mesin Linux (cepat & ringan)
    runs-on: ubuntu-latest

    # Langkah-langkah (step-by-step, seperti skrip Bash)
    steps:
      # 1. Checkout kode dari repo
      - name: 🔁 Checkout kode
        uses: actions/checkout@v4

      # 2. Setup Python
      - name: 🐍 Setup Python 3.9
        uses: actions/setup-python@v5
        with:
          python-version: "3.9"

      # 3. Install dependensi
      - name: 📦 Install dependensi
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # 4. Jalankan unit test
      - name: 🧪 Jalankan pytest di day17, terbaru
        run: |
          cd day17
          python -m pytest -v

```

> 🔍 Penjelasan gaya sysadmin:
> - `uses: ...` = seperti `source /etc/profile.d/...`
> - `run: |` = blok perintah Bash
> - Tiap `- name` = langkah dalam runbook otomatis

---

### ▶️ Cara Uji Lokal (Simulasi GitHub Actions)

Karena kamu belum push, kamu bisa **uji logika workflow-nya secara manual**:

```bash
# 1. Bersihkan (simulasi mesin baru)
rm -rf venv
python3 -m venv venv
source venv/bin/activate

# 2. cek isinya
cat requirements.txt
pandas>=2.0.0
requests>=2.28.0
python-dotenv>=1.0.0
pytest>=7.0.0   # ← ini yang sering kelewat!%

# 3. Install
pip install -r requirements.txt

# 4. Jalankan test
pytest -v
```

Jika ini **berhasil di lokal**, maka **99% akan berhasil di GitHub Actions**.

> ⚠️ Catatan macOS + LibreSSL:  
> GitHub Actions pakai **Ubuntu + OpenSSL**, jadi **tidak ada warning urllib3** seperti di laptopmu.  
> Artinya: **CI-mu akan lebih stabil daripada di lokal!**

---

### 📌 Persiapan Sebelum Push ke GitHub

1. Pastikan struktur repo-mu **sudah rapi** (Hari 14–16):
   ```
   python-ai/
   ├── src/
   ├── scripts/
   ├── tests/
   ├── requirements.txt
   ├── .github/workflows/test.yml   ← baru hari ini
   └── ...
   ```

2. **Commit semua file**:
   ```bash
   git add .
   git commit -m "Day 17: Add GitHub Actions CI"
   ```

3. **Push ke GitHub**:
   ```bash
   git remote add origin https://github.com/arieDEV/python-ai.git
   git push -u origin main
   ```

> 🔥 **Ini saatnya!**  
> Repo-mu **selama ini kosong** → hari ini kamu isi **dengan proyek yang punya CI otomatis**.

---

### 🎉 Setelah Push:
- Buka: `https://github.com/arieDEV/python-ai/actions`
- Kamu akan lihat **workflow "Run Tests" sedang jalan**
- Jika hijau → **✅ Lulus**
- Jika merah → klik detail → lihat log error → perbaiki → push lagi

---

## ✅ Tugas Hari Ini:
1. Buat folder `.github/workflows/`
2. Simpan `test.yml` di dalamnya
3. Uji manual di lokal (pastikan `pytest` jalan)
4. **PUSH KE GITHUB!**  
   Ini **hari pembebasan**: repo-mu akhirnya **tidak kosong**, dan **otomatis diuji tiap kali kamu coding**.

> Setelah push & lihat Actions jalan, balas:  
> **“Day 17 done! 🟢 CI/CD aktif.”**

Besok (Hari 18): kita bikin **dokumentasi teknis di `README.md`** — biar recruiter & engineer lain langsung paham proyekmu dalam 30 detik.

Ayo, Arie! **Jangan tunda lagi. Push hari ini.**  
Kerja keras 17 hari ini **tidak akan terlihat** kalau repo tetap kosong. 💪
