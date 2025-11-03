import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from loganalyzer.utils import setup_logger, read_lines, write_csv
from loganalyzer.core import parse_accepted_logins, summarize_logins
import logging

def main():
    setup_logger()
    parser = argparse.ArgumentParser(
        description="🔍 Analisis log SSH: ekstrak login sukses & ringkas per IP"
    )
    parser.add_argument("logfile", help="Path ke file log (contoh: sample.log)")
    parser.add_argument("--output", default="output/ssh_logins.csv", help="File CSV output")
    parser.add_argument("--summary", action="store_true", help="Buat ringkasan per IP")

    args = parser.parse_args()

    lines = read_lines(args.logfile)
    if not lines:
        sys.exit(1)

    logins = parse_accepted_logins(lines)
    logging.info(f"✅ Ditemukan {len(logins)} login sukses")

    # Simpan detail login
    write_csv(logins, args.output, ['timestamp', 'ip'])

    # Jika diminta, buat ringkasan
    if args.summary:
        summary_file = args.output.replace('.csv', '_summary.csv')
        summary = summarize_logins(logins)
        write_csv(summary, summary_file, ['ip', 'count'])
        logging.info(f"📊 Ringkasan disimpan ke {summary_file}")

if __name__ == "__main__":
    main()
