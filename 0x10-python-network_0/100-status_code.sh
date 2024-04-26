#!/bin/bash
# Sending a GET request to the URL and extracting the status code from the response header
curl -sI -o /dev/null -w "%{http_code}" "$1"
