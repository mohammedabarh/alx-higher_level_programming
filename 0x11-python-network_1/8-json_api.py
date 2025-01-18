#!/usr/bin/python3
"""Sends a POST request with a letter parameter and processes the JSON response."""
import requests
import sys

if __name__ == "__main__":
    # Define the URL
    url = "http://0.0.0.0:5000/search_user"
    
    # Get the letter from command-line arguments
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Prepare the data to send in the POST request
    data = {"q": letter}

    try:
        # Send the POST request
        response = requests.post(url, data=data)
        
        # Check if the response is valid JSON
        try:
            json_response = response.json()
            
            # Check if the JSON is not empty
            if json_response:
                print(f"[{json_response.get('id')}] {json_response.get('name')}")
            else:
                print("No result")
        except ValueError:
            # Handle invalid JSON
            print("Not a valid JSON")
    except requests.exceptions.ConnectionError:
        # Handle connection errors
        print("Error: Failed to connect to the server. Is it running?")
