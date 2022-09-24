#!/usr/bin/python3
"""
- takes in a URL,
- sends a request to the URL, displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request


url = sys.argv[1]

request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
