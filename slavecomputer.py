import time

import socket

import sys

import os

s = socket.socket()

host = "127.0.0.1"

port = 8080

s.connect((host, port))

print ("Connected to Server.")

command = s.recv(1024)

command = command.decode()

if command == "open":

    print("Command is :", command)


    s.send("Command received". encode())

    os.system("ls")