# Log Analyzer CLI

Tool ringan untuk **analisis log SSH** — ekstrak login sukses & buat ringkasan per IP.  
Dibuat oleh mantan sysadmin, untuk sysadmin & data engineer.

## 🔧 Fitur
- Ekstrak baris `Accepted` dari log SSH
- Simpan ke CSV (siap diimpor ke Excel / pipeline data)
- Opsional: buat ringkasan jumlah login per IP

## 🚀 Cara Pakai

1. Pastikan Python 3.7+ terinstall
2. Jalankan langsung (tidak perlu install):

```bash
python loganalyzer/cli.py sample.log --output hasil.csv --summary
