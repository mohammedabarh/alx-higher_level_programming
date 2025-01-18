#!/usr/bin/python3
"""Fetches the GitHub user ID using Basic Authentication."""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
