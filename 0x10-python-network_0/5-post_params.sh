#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, displays the body of the response of the body
curl -sX POST -d "email=test@email.com&subject=I will always be here for PLD" "$1"
