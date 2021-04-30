import socket

server_addr = '192.168.0.17'
PORT = 5050
ADDRESS = (server_addr, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTING CLIENT'

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(ADDRESS)


def send(msg):
    if msg == DISCONNECT_MESSAGE:
        client_sock.send(DISCONNECT_MESSAGE.encode(FORMAT))
    else:
        while True:
            print(msg)
            msg = msg.encode(FORMAT)
            msg_length = len(msg)
            send_msg_length = str(msg_length).encode(FORMAT)
            send_msg_length += b' ' * (HEADER - len(send_msg_length))

            client_sock.send(send_msg_length)
            client_sock.send(msg)

            print(client_sock.recv(2054).decode(FORMAT))


send('Hello World!, This message is from the client side')
send('My name is Riya Chaugule')

