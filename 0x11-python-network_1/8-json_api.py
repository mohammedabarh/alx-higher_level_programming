#!/usr/bin/python3
"""Sends a POST request to a specified URL with a letter as a parameter.

This script sends a POST request to http://0.0.0.0:5000/search_user with a letter
as the value of the `q` parameter. If no letter is provided, it sends an empty string.

Usage: ./8-json_api.py <letter>
  - The letter is passed as the value of the `q` parameter.
  - If no letter is provided, the script defaults to `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    # Set the letter to an empty string if no argument is provided, otherwise use the provided argument
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    # Send a POST request to the specified URL with the payload
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Attempt to parse the response as JSON
        response = r.json()
        if response == {}:
            print("No result")
        else:
            # Print the ID and name from the JSON response
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # Handle the case where the response is not valid JSON
        print("Not a valid JSON")
