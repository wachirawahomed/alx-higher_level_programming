#!/bin/bash
# Sending a POST request to the URL with specified parameters and displaying the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
