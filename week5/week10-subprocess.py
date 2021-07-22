#!/usr/bin/env python3

import subprocess

myCompletedProcess = subprocess.run(['ps -axco command'], shell=True,stdout=subprocess.PIPE)

myProc = myCompletedProcess.stdout

myProcString = myProc.decode()

myProcList = myProcString.split('\n')

for line in myProcList:
    print(line)

# 1:-1 does not count the field header or the empty last line, for the total number of processes.
print(len(myProcList[1:-1]))