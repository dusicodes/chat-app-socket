import socket
import time
import uuid

HOST = "127.0.0.1"  # this is the ip address of the server
PORT = 8000


class Client:
    def __init__(self, name):
        self.name = name
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def connect(self):
        self.s.connect((HOST, PORT))

    def recieve(self):
        return print(self.s.recv(1024).decode("utf-8"))

    def disconnect(self):
        self.s.close()

    def send(self, data):
        self.s.sendall(data.encode("utf-8"))


name = input("Enter your name: ")
client = Client(name)
client.send(client.name)
while True:

    message = input(f"Enter message : ")

    if message.lower() == "quit":
        print("Disconnecting...")
        client.disconnect()
    client.send(message)
    client.recieve()
