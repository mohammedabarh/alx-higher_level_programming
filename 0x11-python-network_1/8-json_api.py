#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a specified letter.

Usage: ./8-json_api.py <letter>
  - The specified letter is sent as the value of the variable `q`.
  - If no letter is provided, `q=""` will be sent by default.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]  # Get the letter from command line arguments
    payload = {"q": letter}  # Prepare the payload for the POST request

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)  # Send the POST request
    try:
        response = r.json()  # Parse the JSON response
        if response == {}:  # Check if the response is empty
            print("No result")  # Inform the user if there are no results
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))  # Display the result
    except ValueError:
        print("Not a valid JSON")  # Handle cases where the response is not valid JSON
