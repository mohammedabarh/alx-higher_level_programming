#!/bin/bash
# This script takes a URL as an argument and displays the body size of the response.
curl -s "$1" | wc -c
