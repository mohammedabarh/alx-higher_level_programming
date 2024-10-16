#!/usr/bin/python3
"""Script for parsing logs and computing metrics"""

import sys

def print_stats(total_size, status_codes):
    """Print the computed statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """Parse a single line of log"""
    try:
        parts = line.split()
        size = int(parts[-1])
        status = int(parts[-2])
        return size, status
    except (ValueError, IndexError):
        return None, None

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            size, status = parse_line(line)
            if size is not None:
                total_size += size
            if status in status_codes:
                status_codes[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
