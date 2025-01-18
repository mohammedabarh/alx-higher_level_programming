#!/usr/bin/python3
"""Script to send a POST request to a specified URL with a letter as a parameter.

This script sends a letter to the server at http://0.0.0.0:5000/search_user.
If no letter is provided, it sends an empty string.
"""
import sys
import requests


if __name__ == "__main__":
    # Set the letter to an empty string if no argument is provided
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    # Send a POST request to the server
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
        # Handle cases where the response is not valid JSON
        print("Not a valid JSON")
