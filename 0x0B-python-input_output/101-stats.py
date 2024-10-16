#!/usr/bin/python3
import sys

def main():
    total_file_size = 0
    status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) < 6:
                continue  # Skip lines that don't have enough parts
            
            # Extract file size and status code
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except ValueError:
                continue  # Skip lines where conversion fails

            total_file_size += file_size
            
            # Increment the count for the status code if it's in our list
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_file_size, status_codes_count)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_codes_count)

def print_stats(total_file_size, status_codes_count):
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        if status_codes_count[status_code] > 0:
            print(f"{status_code}: {status_codes_count[status_code]}")

if __name__ == "__main__":
    main()
