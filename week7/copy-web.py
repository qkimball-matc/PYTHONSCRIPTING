#!/usr/bin/env python3

import requests

response = requests.get("https://notpurple.com")

try:
    response.raise_for_status()
    with open("my_web_file.html", "w") as myWeb:
        myWeb.write(response.text)
except Exception as exc:
    print("There was an error: {exc}")