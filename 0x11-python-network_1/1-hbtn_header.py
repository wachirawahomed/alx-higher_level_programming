#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        request_id = header['X-Request-Id']
        print(request_id)
