# tests/conftest.py
# Tambahkan src/ ke Python path → biar pytest bisa import dari sana
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
