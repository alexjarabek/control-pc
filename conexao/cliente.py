#!/usr/bin/python3
import socket

ip = input("ip >")

porta = int(input("PORTA > "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, porta))
while True:
      cmd = input(">>> ")
      s.send(cmd.encode("utf -8") + "\n".encode("utf -8"))
      print(s.recv(20000).decode("utf -8"))
