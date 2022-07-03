# Rafael Pacheco - Sistemas Embarcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 29/06/2022 - Semestre 2021-2

# Python Socket Programming Tutorial

import socket
import sys

TCP_IP = "192.168.2.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = sys.argv[1]


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))
    sock.send(file_name)
    sock.close()

    print( "Sending %s ..." % file_name)

    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read()
    sock.send(data)

finally:
    sock.close()
    f.close()