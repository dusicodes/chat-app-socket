import socket
import threading

HOST = ""
PORT = 8000
clients = {}


def handle_client(conn, addr):

    with conn:  # this is used to close the connection
        print("Connected by", addr)
        client_name = conn.recv(1024)
        clients[conn] = client_name.decode("utf-8")
        print(f"{clients[conn]} joined the server")

        while True:  # this is used to keep the connection open
            data = conn.recv(1024)  # this is used to receive data from the client

            if not data:
                break
            conn.sendall(data)  # this is used to send data to the client
            print(
                f"{clients[conn]} sent message to server: ", repr(data.decode("utf-8"))
            )


with socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
) as s:  # this creates a socket s of type socket.AF_INET and socket.SOCK_STREAM. AF_INET is used for IPv4 and SOCK_STREAM is used for TCP protocol
    s.bind((HOST, PORT))  # this binds the socket to the host and port
    s.listen(1)  # this allows the server to listen for incoming connections
    while True:
        conn, addr = (
            s.accept()
        )  # this accepts the incoming connection where the connection is stored in conn and the address is stored in addr
        threading.Thread(target=handle_client, args=(conn, addr)).start()
