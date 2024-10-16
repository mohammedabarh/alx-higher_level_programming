#!/usr/bin/python3
"""
Reads log entries from standard input and computes various metrics.

This script processes HTTP log entries, extracting and counting the
occurrences of specific status codes. It also calculates the total
size of the responses. The metrics are printed to standard output
every 10 lines processed, including the total file size and the
count of each relevant status code.
"""

if __name__ == "__main__":
    import sys

    stdin = sys.stdin

    c = 0  # Counter for the number of lines processed
    size = 0  # Total file size
    vd = ['200', '301', '400', '401', '403', '404', '405', '500']  # Valid status codes
    st = {}  # Dictionary to count occurrences of status codes

    try:
        for line in stdin:
            # Print metrics every 10 lines
            if c == 10:
                print("File size: {}".format(size))
                for i in sorted(st):
                    print("{}: {}".format(i, st[i]))
                c = 1  # Reset counter after printing
            else:
                c += 1  # Increment line counter

            line = line.split()  # Split the line into components

            try:
                size += int(line[-1])  # Add the size from the last column
            except (IndexError, ValueError):
                pass  # Ignore errors in size extraction

            try:
                # Check if the status code is valid and count it
                if line[-2] in vd:
                    if st.get(line[-2], -1) == -1:
                        st[line[-2]] = 1
                    else:
                        st[line[-2]] += 1
            except IndexError:
                pass  # Ignore lines that do not have enough components

        # Print final metrics after processing all lines
        print("File size: {}".format(size))
        for i in sorted(st):
            print("{}: {}".format(i, st[i]))

    except KeyboardInterrupt:
        # Handle keyboard interrupt gracefully
        print("File size: {}".format(size))
        for i in sorted(st):
            print("{}: {}".format(i, st[i]))
        raise
