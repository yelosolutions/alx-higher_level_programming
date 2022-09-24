#!/usr/bin/python3
"""
- takes in a URL 
- sends request to URL
- displays the body of the response (decoded in utf-8).
"""


import sys
from urllib import request, error

try:
    with request.urlopen(sys.argv[1]) as res:
        print(res.read().decode('UTF-8'))
except error.HTTPError as er:
    print('Error code:', er.code)
