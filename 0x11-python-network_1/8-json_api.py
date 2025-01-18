#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

if __name__ == "__main__":
    # Check if a letter is provided as a command-line argument
    if len(sys.argv) == 1:
        letter = ""  # Default to an empty string if no letter is provided
    else:
        letter = sys.argv[1]  # Use the provided letter

    # Prepare the payload with the letter as the value for the 'q' parameter
    payload = {'q': letter}

    # Send a POST request to the server with the payload
    request = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        # Attempt to parse the response as JSON
        response = request.json()
        # Check if the JSON response is empty
        if response == {}:
            print('No result')
        else:
            # Print the ID and name from the JSON response
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        # Handle the case where the response is not valid JSON
        print('Not a valid JSON')
