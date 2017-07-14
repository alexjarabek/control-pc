#!/usr/bin/python3
import socket
from subprocess import Popen, PIPE
import os


def _terminal_(c, cliente):
    print("conectado com",cliente)
 
    while True:

        dados = c.recv(2000).decode("utf -8")
        if dados.split(" ")[0] == "cd":
           try:
               pasta = (dados.split(" ")[1])
               pasta1 = os.chdir(pasta.rstrip("\n"))
               local = os.getcwd()
               c.send(local.encode("utf -8"))
           except:
                 c.send("error".encode("utf -8"))

           #TROCA DE PASTA
        else:
             sh = Popen(dados, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
             res = sh.stdout.read() + sh.stderr.read()
#             TERMINAL
             c.send(res)


ip = input("host > ")
porta = int(input("port > "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,porta))
s.listen(10)

c, cliente = s.accept()

_terminal_(c,cliente)

