#!/usr/bin/python3
import sys
from collections import defaultdict

def print_stats(total_size, status_count):
    print(f"File size: {total_size}")
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")

def main():
    total_size = 0
    status_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) < 6:
                continue  # Skip invalid lines

            # Extract the file size and status code
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size and status count
            total_size += file_size
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_count[status_code] += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        sys.exit(0)

if __name__ == "__main__":
    main()
