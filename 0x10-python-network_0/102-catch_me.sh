#!/bin/bash
# This script makes a request to a specific endpoint and captures the response
curl -s -X PUT -L -d "user_id=98" "0.0.0.0:5000/catch_me"
