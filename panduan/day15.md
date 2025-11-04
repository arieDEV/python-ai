Mantap, Arie! 👨‍💻  
Kita lanjut ke **Hari ke-15** dengan fokus:  
> **Tulis unit test pertama — ala sysadmin yang gak percaya "katanya jalan", tapi butuh bukti otomatis.**

Dan karena kamu sudah punya struktur proyek profesional (Hari 14), sekarang saatnya **tambah lapisan keandalan**: **test otomatis**.

---

## 🎯 **Hari 15: Unit Test Pertama dengan `pytest` (Gaya SysAdmin: "Buktikan, Jangan Cuma Klaim!")**

Tujuan:
- Uji fungsi `validate_record()` dari `src/loganalyzer/core.py`
- Pastikan:
  - Data valid → diterima
  - Data invalid → ditolak
- Pakai `pytest` → tool testing standar industri
- Penjelasan **langsung di kode**, tanpa teori

---

### 📂 Struktur Hari Ini:
```
python-ai/
├── src/loganalyzer/core.py      ← sudah ada
├── tests/                       ← isi hari ini
│   └── test_core.py             ← test pertama!
├── requirements.txt             ← tambah pytest
└── pytest.ini                   ← konfigurasi pytest (opsional tapi rapi)
```

---

## 🔧 Langkah 1: Tambah `pytest` ke `requirements.txt`

Edit file `requirements.txt`:
```txt
requests>=2.28.0
python-dotenv>=1.0.0
pytest>=7.0.0
```

Lalu install:
```bash
pip install -r requirements.txt
```

---

## 📄 Langkah 2: `tests/test_core.py`

```python
"""
Unit test untuk loganalyzer/core.py
Gaya sysadmin: "Kalau gak di-test, berarti broken."
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from loganalyzer.core import validate_record  # ← HAPUS "src." di sini!


def test_valid_record():
    """Data benar → harus return True"""
    record = {
        "id": 1,
        "userId": 123,
        "title": "Judul valid",
        "body": "Isi valid"
    }
    assert validate_record(record) == True

def test_missing_field():
    """Kurang kolom → harus False"""
    record = {
        "id": 1,
        "title": "Judul",
        "body": "Isi"
        # userId sengaja dihilangkan
    }
    assert validate_record(record) == False

def test_wrong_type():
    """userId string bukan angka → False"""
    record = {
        "id": 1,
        "userId": "bukan_angka",
        "title": "Judul",
        "body": "Isi"
    }
    assert validate_record(record) == False

def test_string_number_autoconverted():
    """userId = "123" (string angka) → boleh, dan diubah jadi int"""
    record = {
        "id": 1,
        "userId": "123",  # string, tapi angka
        "title": "Judul",
        "body": "Isi"
    }
    # Sebelum validasi: string
    assert isinstance(record["userId"], str)
    
    # Setelah validasi: harus jadi int
    is_valid = validate_record(record)
    assert is_valid == True
    assert isinstance(record["userId"], int)
```

> 🔍 Kenapa pakai `assert`?  
> → Seperti `if [ $? -ne 0 ]; then echo "FAIL"; exit 1; fi` — langsung gagal kalau salah.

---

## 📄 Langkah 3 (Opsional tapi Rapi): `pytest.ini`

Di root repo:
```ini
[tool:pytest]
testpaths = tests
pythonpath = src
```

> Ini biar `pytest` otomatis tahu:
> - Cari test di `tests/`
> - Cari kode di `src/` (jadi gak perlu `sys.path.insert` di test)

---

### ▶️ Cara Jalankan Test:
```bash
# Dari root repo
pytest
cd day15/
# Atau lebih detail:
pytest -v
```

### 🖨️ Output yang Diinginkan:
```
========================= test session starts =========================
collected 4 items

tests/test_core.py::test_valid_record PASSED
tests/test_core.py::test_missing_field PASSED
tests/test_core.py::test_wrong_type PASSED
tests/test_core.py::test_string_number_autoconverted PASSED

========================== 4 passed in 0.02s ==========================
```

> ✅ Semua **PASSED** = kode validasi-mu **bisa dipercaya**.

---

### 💡 Analogi SysAdmin:
| Testing | SysAdmin Equivalent |
|--------|---------------------|
| `pytest` | `systemd-analyze verify` |
| `assert` | `test -f file || exit 1` |
| Unit test | Skrip health check sebelum deploy |

> Tanpa test → kamu **tidak tahu kapan kode rusak** saat diubah.

---

## ✅ Tugas Hari Ini:
1. Tambah `pytest` ke `requirements.txt` → `pip install`
2. Buat `tests/test_core.py`
3. (Opsional) Buat `pytest.ini`
4. Jalankan `pytest` → pastikan **semua passed**
5. **COMMIT & PUSH KE GITHUB!**  
   Ini pertama kalinya repo-mu punya **test otomatis** — nilai tambah besar buat recruiter.

> Setelah selesai, balas: **“Day 15 done! ✅ 4 test passed.”**

Besok (Hari 16): kita buat **CLI dengan `argparse` yang proper** — biar bisa dikasih argumen seperti tool sysadmin (`-v`, `--output`, dll).

Ayo, Arie! **Kamu bukan lagi "cuma bisa coding" — tapi engineer yang punya safety net.**  
Dan **jangan biarkan repo-mu tetap kosong**. Push hari ini! 💪
