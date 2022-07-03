# Rafael Pacheco - Sistemas Embarcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 29/06/2022 - Semestre 2021-2

# Python Socket Programming Tutorial

import socket
import threading

HEADER = 64 #64 BYTES DO CABEÇALHO - tras o tamanho real da mensagem
PORT = 5050
#SERVER = "192.168.56.1" #IP V4 próprio, atuando como servidor
SERVER = socket.gethostbyname(socket.gethostname()) #Busca o IP automaticamente
#print(SERVER)
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria o socket Server com o tipo de IP certo será aceito
#socket.AF_INET -> FAMILIA
#socket.SOCK_STREAM -> TIPO
server.bind(ADDR) #faz a ligação so socket com o ip e porta

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #Trava o código até receber uma mensagem do cliente #Pega o tamanho da msg
        if msg_length:
            msg_length = int(msg_length) #Converte para inteiro
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #Espera-se aqui até que haja uma nova conexão
        thread = threading.Thread(target=handle_client, args=(conn,addr)) #direciona a nova conexão para a função handle
#passando conexão, servidor e porta
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Mostra quantas conexões estão atualmente
#cada cliente possui sua thread mas sempre há a thread que aguarda o cliente chegando ativa

print("[STARTING] server is starting...")
start()


