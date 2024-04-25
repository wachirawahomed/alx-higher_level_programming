#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the request body and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
