#!/usr/bin/env python3

# Question 1:
myFile = open("/etc/passwd", "r")

fileString = myFile.read()

print(len(fileString))
print("The len() function counts the total characters in the /etc/passwd file.")
print("You would use the read function if you wanted to calculate the total characters of a file efficiently.")

myFile.close()

# Question 2:
myFile = open("/etc/passwd", "r")
fileList = myFile.readlines()

print(len(fileList))
print("The len() function counts the total number of lines contained in file.")
print("You would use this read function to count the number of lines in a file.")

myFile.close()

# Question 3:
with open("/etc/passwd", "r") as myFile:

    totalFileLength = 0

    for line in myFile:
        totalFileLength += len(line)

    print(totalFileLength)
    print("The len function grabs the total number of characters in each line.")
    print("This would be used to grab the total number of characters in the document line by line.")



