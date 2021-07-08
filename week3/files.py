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
fileList = [myFile.read()]

print(len(fileList))
print("The len() function counts the total number of lists contained in fileList.")
print("You would use this read function to ensure you're file made it all into one list.")

myFile.close()

# Question 3:
myFile =open("/etc/passwd", "r")
lines = myFile.readlines()

total = 0
    
for char in lines:
    total += len(char)

print(total)

print("This function would be useful if you needed to access other contents line by line, easy to slip in extra code.")

myFile.close()


