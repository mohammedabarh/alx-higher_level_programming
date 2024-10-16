#!/usr/bin/python3
"""Reads from standard input and computes metrics"""

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def parse_line(line):
    try:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, None

def main():
    total_size = 0
    line_count = 0
    status_counts = defaultdict(int)
    valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in valid_status_codes:
                    status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
