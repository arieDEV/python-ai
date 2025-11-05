#!/usr/bin/env python3
"""
Pipeline data dengan CLI ala sysadmin:
- Bisa pakai .env
- Bisa override lewat argumen
- Ada --verbose buat debug
"""

import os
import sys
import logging
import argparse  # <-- ini modul bawaan Python buat CLI
from dotenv import load_dotenv

# Pastikan bisa import dari src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from loganalyzer.core import fetch_posts, validate_record, save_to_csv

def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(levelname)s - %(message)s'
    )

def main():
    # Muat .env dulu (sebagai default)
    load_dotenv()

    # Baca default dari .env
    default_url = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")
    default_output = os.getenv("OUTPUT_CSV", "data/output/posts.csv")

    # Setup argparse
    parser = argparse.ArgumentParser(
        description="🔍 Ambil data dari API, validasi, simpan ke CSV.",
        epilog="Contoh: python run_pipeline.py --url https://api.example.com/data --output hasil.csv"
    )
    parser.add_argument(
        "--url", 
        default=default_url,
        help=f"URL API (default: {default_url})"
    )
    parser.add_argument(
        "--output", 
        default=default_output,
        help=f"File output CSV (default: {default_output})"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Tampilkan log detail (DEBUG level)"
    )

    args = parser.parse_args()
    setup_logging(args.verbose)

    logging.info(f"📡 URL: {args.url}")
    logging.info(f"💾 Output: {args.output}")

    try:
        data = fetch_posts(args.url)
        valid = [r for r in data if validate_record(r.copy())]
        save_to_csv(valid, args.output)
        logging.info(f"✅ Berhasil: {len(valid)} record valid disimpan.")
    except Exception as e:
        logging.error(f"💥 Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()