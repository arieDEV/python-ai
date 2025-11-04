#!/usr/bin/env python3
# scripts/run_pipeline.py
import os
import sys
import logging
from dotenv import load_dotenv

# Pastikan bisa import dari src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from loganalyzer.core import fetch_posts, validate_record, save_to_csv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def main():
    API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")
    OUTPUT = os.getenv("OUTPUT_CSV", "data/output/posts.csv")

    try:
        data = fetch_posts(API_URL)
        valid = [r for r in data if validate_record(r.copy())]
        save_to_csv(valid, OUTPUT)
        logging.info(f"✅ {len(valid)} record valid disimpan ke {OUTPUT}")
    except Exception as e:
        logging.error(f"💥 Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
