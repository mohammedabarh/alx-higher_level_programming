#!/usr/bin/python3
"""Fetches a URL and handles HTTP errors using requests."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
