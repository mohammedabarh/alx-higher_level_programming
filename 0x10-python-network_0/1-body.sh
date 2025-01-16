#!/bin/bash
# This script takes a URL and displays the body of the response if the status code is 200.
curl -s -X GET "$1"
