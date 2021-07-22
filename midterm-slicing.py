#!/usr/bin/env python3

print("Name: Quinn Kimball\n")

sliceFile = open("./slicing-file.txt", "r")

sliceString = sliceFile.readlines()

three = sliceString[-3:-4:-1]
threeFive = sliceString[2:5]
tenEnd = sliceString[-10:-16:-2]
elevenThirteen = sliceString[10:13]
nineteenEnd = sliceString[8:5:-1]

quote = ''.join(three + threeFive + tenEnd + elevenThirteen + nineteenEnd)

print(quote.replace("\n", " "))