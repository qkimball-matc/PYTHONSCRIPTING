#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description= "This is Quinn's script")

parser.add_argument("-m", dest="basic", help="Enter some text")
parser.add_argument("-i", "--integer", dest="myInt", nargs=1, type=int, metavar="[an integer]", help="<required> Enter a simple Integer")
parser.add_argument("-d", "--float", dest="myFloat", type=float, metavar="[a float]", help="Enter a simple float")
parser.add_argument("-s", "--string", dest="myString", type=str, metavar="[a string]", help="Enter a simple string")
parser.add_argument("-l", dest="myList", action="append", nargs="+", metavar="[strings]", help="Enter a list of strings (space delimited)")
parser.add_argument("-t", "--set-true", dest="myTrue", action="store_true", default=False, help="Toggle from default False to True")
parser.add_argument("-f", "--setfalse", dest="myFalse", action="store_false", default=True, help="Toggle from default True to False")
parser.add_argument("-v", "--version", dest="version", action="version",version="%(prog)s 1.0", help="show program's version number and exit")

if(len(sys.argv) == 1):
    parser.print_help()
else:
    args = parser.parse_args()
    print(f"My integer is {args.myInt}")
    print(f"My string is {args.myString}")
    print(f"My float is {args.myFloat}")
    print(f"My list is {args.myList}")