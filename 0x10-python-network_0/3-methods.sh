#!/bin/bash
# show all acceptable HTTP methods
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
