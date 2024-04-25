#!/bin/bash
# Sends a GET request to a URL and displays the body of the response if the status code is 200
curl -sL -w "%{http_code}" -X GET "$1" -o /dev/null | if [ "$(tail -n 1)" == "200" ]; then curl -sL "$1"; fi
