#!/bin/bash
# This script takes a URL and displays the size of the response body.
curl -s "$1" | wc -c
