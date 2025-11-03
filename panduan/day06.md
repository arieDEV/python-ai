Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-6** dengan fokus:  
> **Bikin proyek Python yang bisa di-install & dijalankan siapa saja — ala sysadmin yang peduli pada reproducibility.**

---

## 🎯 **Hari 6: Virtual Environment + `requirements.txt` (No Magic, Just Works)**

Tujuan hari ini:
- Pisahkan dependensi proyek dari sistem (biar gak bentrok kayak `apt` vs `pip`)
- Buat `requirements.txt` → supaya orang lain (atau kamu 6 bulan lagi) bisa `install` & jalanin dengan **1 perintah**
- Ini standar wajib di semua proyek profesional — termasuk untuk AI Trainer, Data Eng, dll.

Dan tetap: **penjelasan gaya mantan sysadmin**, langsung di terminal & file.

---

### 📂 Struktur Akhir Hari Ini:
```
python-ai/
├── requirements.txt        ← daftar paket yang dibutuhkan
├── .gitignore              ← jangan commit folder env
├── day02/sample.log        ← (sudah ada)
├── day05/...               ← (sudah ada)
└── venv/                   ← folder virtual environment (tidak di-commit!)
```

---

## 🔧 Langkah 1: Buat `requirements.txt`

File ini seperti **`package.list`** di Debian atau **`Dockerfile RUN pip install`** — daftar semua library yang dipakai.

Buka terminal di root repo (`python-ai/`), lalu buat file:

### 📄 `requirements.txt`
```txt
# Paket yang kita pakai sejauh ini
pandas>=2.0.0
```

> Kenapa cuma `pandas`?  
> - `re`, `csv`, `os`, `logging` → bawaan Python (**built-in**), gak perlu install  
> - `pandas` → satu-satunya external package yang kita pakai (di Day 3)

Kalau nanti pakai `requests`, `numpy`, dll → tambah di sini.

---

## 🔧 Langkah 2: Buat Virtual Environment (venv)

Ini **isolasi lingkungan Python** — mirip `chroot`, `container`, atau `namespace`, tapi khusus untuk Python.

### ▶️ Jalankan di terminal (Linux/macOS):
```bash
# Masuk ke folder proyek
cd python-ai

# Buat folder virtual env (namanya bebas, tapi umumnya "venv")
python3 -m venv venv

# Aktifkan environment-nya
source venv/bin/activate

# Sekarang prompt terminal berubah jadi: (venv) $
# Artinya: semua perintah python/pip pakai versi di venv, bukan sistem
```

> ⚠️ Jangan commit folder `venv/`! Kita atur di `.gitignore`.

---

## 🔧 Langkah 3: Install dari `requirements.txt`

Dalam keadaan **venv aktif** (`(venv) $`):

```bash
# Install semua paket dari requirements.txt
pip install -r requirements.txt

# Cek apa yang terinstall
pip list
```

Output harus ada:
```
pandas    2.x.x
...
```

---

## 🔧 Langkah 4: Tambahkan `venv/` ke `.gitignore`

Supaya folder `venv/` **tidak ikut ke GitHub** (karena berat & spesifik mesin lokal).

### 📄 Edit `.gitignore` (di root repo):
```gitignore
# Virtual environment
venv/
.env

# Setup script (dari Day 1)
setup-github.sh
```

> `.env` juga di-ignore karena biasanya berisi password/API key.

---

## 🔁 Cara Orang Lain (atau Kamu di Mesin Baru) Pakai Proyek Ini:

```bash
git clone https://github.com/arieDEV/python-ai.git
cd python-ai

# Buat & aktifkan venv
python3 -m venv venv
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt

# Jalankan program
python day05/main.py
```

✅ **Langsung jalan — tanpa error “module not found”**.

---

## 💡 Analogi SysAdmin:
| Konsep Python | Analogi SysAdmin |
|--------------|------------------|
| `venv` | `chroot` / container ringan — isolasi dependensi |
| `requirements.txt` | `apt install -y $(cat packages.list)` |
| `pip install -r` | `dpkg --set-selections < packages.list && apt-get dselect-upgrade` |
| `.gitignore` | `.dockerignore` — jangan kirim sampah ke repo |

---

## ✅ Tugas Hari Ini:
1. Di root repo (`python-ai/`), buat:
   - `requirements.txt` (isi: `pandas>=2.0.0`)
   - Edit `.gitignore` → tambahkan `venv/` dan `.env`
2. Jalankan:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python day05/main.py  # pastikan masih jalan
   ```
3. **JANGAN** commit folder `venv/`!
4. Commit hanya:
   - `requirements.txt`
   - `.gitignore` (update)
5. Push ke GitHub

> Setelah selesai, balas: **“Day 6 done!”**

Besok (Hari 7): kita **gabung semua jadi 1 proyek CLI utuh** — dengan README, struktur rapi, dan bisa dijalankan dari mana saja. Ini jadi **kartu nama teknismu**!

Ayo, Arie — proyekmu sudah mulai terlihat seperti **karya engineer profesional**! 🚀
