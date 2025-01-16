#!/bin/bash
# This script takes a URL and displays all accepted HTTP methods by the server.
curl -s -X OPTIONS "$1" -I | grep 'Allow:' | cut -d' ' -f2-
