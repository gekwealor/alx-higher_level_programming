#!/bin/bash
# Sends JSON POST request to the  given URL with a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
