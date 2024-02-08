#!/usr/bin/python3
"""Log parsing script."""
import sys
import random
import datetime
from time import sleep


def generate_log_line():
    """Generate a random log line."""
    return "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        random.randint(1, 255), datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024))


def main():
    """Main function to generate log lines."""
    for i in range(10000):
        sleep(random.random())
        sys.stdout.write(generate_log_line())
        sys.stdout.flush()


if __name__ == "__main__":
    main()
