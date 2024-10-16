#!/usr/bin/python3
"""Reads from standard input and computes metrics.

This script processes log entries from standard input, calculating and
displaying the following statistics after every ten lines or upon 
keyboard interruption (CTRL + C):
    - Total accumulated file size.
    - Count of specified HTTP status codes.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The total file size accumulated so far.
        status_codes (dict): A dictionary containing counts of HTTP status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            # Print stats after every ten lines
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            # Split the line into components
            line = line.split()

            # Try to accumulate the file size
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            # Try to count the HTTP status codes
            try:
                if line[-2] in valid_codes:
                    if line[-2] not in status_codes:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        # Print final stats after all input has been processed
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        # Print stats upon keyboard interruption
        print_stats(size, status_codes)
        raise
