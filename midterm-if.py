#!/usr/bin/env python3

print("Name: Quinn Kimball")

midFile = open("/home/student/Documents/weekly-assignments-qkimball-matc/Midterm-if.txt", "r")

Total = 0

for line in midFile:
    docList = line.split(",")
    if 'gmeach18@ed.gov' in str(docList):
        Total += int(docList[0])
    elif '248.253.63.149' in str(docList):
        Total += int(docList[0])
    elif 'Whiteland' in str(docList):
        Total += int(docList[0])
    elif '80.222.19.190' in str(docList):
        Total += int(docList[0])
    elif 'Kayley' in str(docList):
        Total += int(docList[0])
    elif 'dcassyqw@microsoft.com' in str(docList):
        Total += int(docList[0])

print(Total)


