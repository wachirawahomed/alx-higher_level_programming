#!/bin/bash
# Sending a GET request to the URL with a custom header and displaying the body of the response
curl -sL -H "X-School-User-Id: 98" "$1"
