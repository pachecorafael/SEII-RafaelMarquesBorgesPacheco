# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 29/06/2022 - Semestre 2021-2

# Python Socket Programming Tutorial

import socket

HEADER = 64 #64 BYTES DO CABEÇALHO - tras o tamanho real da mensagem
PORT = 5050
#SERVER = "192.168.56.1" #IP V4 próprio, atuando como servidor
SERVER = socket.gethostbyname(socket.gethostname()) #Busca o IP automaticamente
#print(SERVER)
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
#DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World!")