#!/usr/bin/python3

import urllib.request

def fetch_status():
    try:
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
            html = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(html.decode('utf-8')))
    except Exception as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    fetch_status()
