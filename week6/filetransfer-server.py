#!/usr/bin/env python3
import socket
import sys


L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind(("127.0.0.1", 1234))
L_SOCK.listen()

while True:
    L_CONN, addr = L_SOCK.accept()
    print("Connected to", addr)
    CPY_DATA = open("copyfile.txt", "wb")
    RCV_DATA = L_CONN.recv(1024)
    CPY_DATA.write(RCV_DATA)
    CPY_DATA.close()
    L_CONN.close()
    print("File copied successfully.")
