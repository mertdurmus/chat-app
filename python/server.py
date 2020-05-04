# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:34:11 2020

@author: elifaskvav
"""

#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os

clientss = []
Dict = {} 



def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("*Adını  yaz ve giris yap", "utf8"))
        addresses[client] = client_address
        clientss.append(client_address)
        Thread(target=handle_client, args=(client,)).start()



def handle_client(client):  
    name = client.recv(BUFSIZ).decode("utf8")
    Dict[name]=addresses[client]
    welcome = '*Hosgeldin %s!  cikmak istersen {quit} yaz' % name
    client.send(bytes(welcome, "utf8"))
    clients[client] = name
    
    while True:
        msg = client.recv(BUFSIZ)
        name3=client.recv(BUFSIZ).decode("utf8")
        if msg != bytes("{quit}", "utf8"):
            if msg == bytes("gtr", "utf8"):
                handle_client_name(client)
            else:
                broadcast(msg, name3, "*"+name+": ")            
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s ayrıldı." % name, "utf8"))
            break



def broadcast(msg, name, prefix=""):

    for sock in clients:
        x=Dict[name]
        if(str(x)==str(sock.getpeername())):
            sock.send(bytes(prefix, "utf8")+msg)



def handle_client_name(client2):
    client2.send(bytes('gtr', "utf8"))
    prefix='+'
    for k in  Dict:
        client2.send(bytes(k+prefix, "utf8"))
        


        
clients = {}
addresses = {}

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen()
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
    

    

"""
 for connected in clients:
            response = os.system("ping -c 1 " + str(connected))
            print(response)
            if response == True:
                continue
            else:
                client.send(bytes('user offline', "utf8"))
                clients.remove(connected)
                break

"""























