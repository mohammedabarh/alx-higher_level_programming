#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every 10 lines or upon receiving a keyboard interrupt (CTRL + C),
it prints:
- Total file size: sum of all previous file sizes
- Number of occurrences of each status code in sorted order
"""

import sys

# Initialize global variables
total_file_size = 0
status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def print_stats():
    """Prints cumulative metrics: total file size and status codes count."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


if __name__ == "__main__":
    line_count = 0

    try:
        # Read from stdin line by line
        for line in sys.stdin:
            parts = line.split()

            # Ensure the line has the expected format
            try:
                file_size = int(parts[-1])
                status_code = parts[-2]

                # Update metrics
                total_file_size += file_size
                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1

            except (IndexError, ValueError):
                # Skip lines with incorrect format
                continue

            # Print metrics every 10 lines
            line_count += 1
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        # Print final stats on keyboard interruption (CTRL + C)
        print_stats()
        raise

