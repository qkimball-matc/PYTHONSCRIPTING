#!/usr/bin/env python3
import socket
import sys


C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect(("127.0.0.1", 1234))
print("Connection to the server established ..")
C_FILE = open("testfile.txt", "rb")
SND_DATA = C_FILE.read(1024)

while(SND_DATA):
    C_SOCK.send(SND_DATA)
    SND_DATA = C_FILE.read(1024)
print("testfile successfully copied")

C_SOCK.close()