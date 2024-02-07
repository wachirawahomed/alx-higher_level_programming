#!/usr/bin/python3
"""Log parsing script."""
import sys

total_size = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}


def print_stats():
    """Function that prints a summary of the statistics."""
    print("Total file size: {}".format(total_size))
    for code, count in sorted(codes.items()):
        if count > 0:
            print("Number of lines with status code\
                    {}: {}".format(code, count))


try:
    for line_number, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) >= 3:
            status_code = parts[-2]
            try:
                file_size = int(parts[-1])
            except ValueError:
                print("Error: Line {}: Invalid file size\
                        format: {}".format(line_number, parts[-1]))
                continue

            if status_code in codes:
                codes[status_code] += 1
            else:
                print("Error: Line {}: Unknown status\
                        code: {}".format(line_number, status_code))
                continue

            total_size += file_size

        if line_number % 10 == 0:
            print("\nStatistics at line {}: ".format(line_number))
            print_stats()

    print("\nFinal statistics: ")
    print_stats()

except KeyboardInterrupt:
    print("\nFinal statistics (interrupted): ")
    print_stats()
