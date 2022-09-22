#!/bin/bash
# size of the body of response from request to URL
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
