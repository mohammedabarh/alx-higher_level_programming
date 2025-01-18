#!/usr/bin/python3
"""
API User Search Utility

This script sends a POST request to a local API endpoint to search for users 
based on a given letter. It demonstrates handling API requests, JSON parsing, 
and basic error handling.

Features:
- Sends a search query to a local API endpoint
- Supports optional letter-based searching
- Handles different response scenarios
- Provides user-friendly output

Usage:
    python3 6-main.py [optional_letter]

Examples:
    ./6-main.py           # Search with empty query
    ./6-main.py a         # Search for users starting with 'a'
    ./6-main.py 'j'       # Search for users starting with 'j'

Dependencies:
    - requests library
"""
import sys
import requests


if __name__ == "__main__":
    # Determine the search letter, defaulting to empty string if no argument
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    
    # Prepare payload for API request
    payload = {"q": letter}

    # Send POST request to the search endpoint
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    
    try:
        # Attempt to parse JSON response
        response = r.json()
        
        # Handle different response scenarios
        if response == {}:
            print("No result")
        else:
            # Display user ID and name if result exists
            print("[{}] {}".format(response.get("id"), response.get("name")))
    
    except ValueError:
        # Handle invalid JSON response
        print("Not a valid JSON")
