#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
