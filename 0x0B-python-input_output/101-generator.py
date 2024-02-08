#!/usr/bin/python3
"""Log parsing script."""
import sys
import random
from datetime import datetime
from time import sleep


def generate_log_line():
    """Generate a random log line."""
    return "{:d}.{:d}.{:d}.{:d} - [{}] \"GET/projects\
            /260 HTTP/1.1\" {} {}\n".format(
                random.randint(1, 255), random.randint(1, 255),
                random.randint(1, 255), random.randint(1, 255),
                datetime.now(),
                random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
                random.randint(1, 1024))


def main():
    """Main function."""
    try:
        while True:
            print(generate_log_line(), end="")
            sys.stdout.flush()
            sleep(random.random())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
