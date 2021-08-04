#!/usr/bin/env python3

import sys
import argparse
import requests
import json

parser = argparse.ArgumentParser(description= "***IP Statistics Script***")
parser.add_argument("-ip", dest="userIP", type=str, metavar="[IPv4 Address]", help="enter a valid IPv4 Address")

if(len(sys.argv) == 1):
    parser.print_help()
else:
    args = parser.parse_args()
    response = requests.get(f"https://ipinfo.io/{args.userIP}/json")

    myDict = json.loads(response.text)

    for key in myDict.keys():
        print(f"{key} : {myDict[key]}")