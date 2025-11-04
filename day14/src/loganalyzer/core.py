import requests
import csv
import os
from typing import List, Dict, Any

# Validasi & parsing logikanya di sini — reusable
REQUIRED_FIELDS = {
    'id': int,
    'userId': int,
    'title': str,
    'body': str
}

def fetch_posts(url: str) -> List[Dict[str, Any]]:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

def validate_record(record: Dict) -> bool:
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in record:
            return False
        val = record[field]
        if not isinstance(val, expected_type):
            if expected_type == int and isinstance(val, str) and val.isdigit():
                record[field] = int(val)
            else:
                return False
    return True

def save_to_csv(records: List[Dict], output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = list(REQUIRED_FIELDS.keys())
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
