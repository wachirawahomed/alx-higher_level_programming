#!/bin/bash
# Sending an OPTIONS request to the URL and displaying the Allow header, which contains the accepted methods
curl -sI "$1" | grep -i Allow | cut -d' ' -f2-
