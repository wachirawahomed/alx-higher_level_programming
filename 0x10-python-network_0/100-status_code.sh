#!/bin/bash
# Sending a GET request to the URL and extracting the status code from the response header
curl -sI "$1" | grep -oP "(?<=HTTP\/1\.1 )\d+"
