import re
import logging

def extract_ssh_logins(lines):
    """
    Ambil baris yang mengandung 'Accepted', ekstrak timestamp & IP.
    Input: list baris log
    Output: list dict [{'timestamp': ..., 'ip': ...}]
    """
    if not lines:
        logging.warning("Tidak ada baris untuk diproses")
        return []

    logins = []
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Accepted.*from\s+([0-9.]+)'

    for i, line in enumerate(lines, 1):
        try:
            match = re.search(pattern, line)
            if match:
                logins.append({
                    'timestamp': match.group(1),
                    'ip': match.group(2)
                })
        except Exception as e:
            logging.warning(f"Baris {i} error: {e}")
    return logins
