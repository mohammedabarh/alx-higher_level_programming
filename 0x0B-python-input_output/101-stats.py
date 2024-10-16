#!/usr/bin/python3
import sys
from collections import defaultdict


def print_metrics(total_size, status_codes):
    """Print accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def main():
    """Main processing function."""
    total_size = 0
    status_codes = defaultdict(int)
    lines_count = 0

    try:
        for line in sys.stdin:
            lines_count += 1
            parts = line.split()
            if len(parts) < 6:
                continue
            
            # Extract file size and status code
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total size and status code count
            total_size += file_size
            status_codes[status_code] += 1

            # Print metrics every 10 lines
            if lines_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
