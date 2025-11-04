import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from loganalyzer.core import validate_record  # ← HAPUS "src." di sini!

"""
Unit test untuk loganalyzer/core.py
Gaya sysadmin: "Kalau gak di-test, berarti broken."
"""

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
