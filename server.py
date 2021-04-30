import socket
import threading

'''
PORT = 5050, hardcoding port number for server socket.
#SERVER = "192.168.0.17" - Static server ip address. Below is dynamic implementation of getting server ip address.

#This will get the loop back Ipv4 address (local hostname/l0) of our machine.
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER, socket.gethostname())
'''

# To get ip address of the machine on Internet (en0)/ Network Interface Card.
def get_ip_address():
    #Create a socket specifying address family - IPv4 and type of socket - UDP packet.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Start connecting to external IP address (arg 1) at port (arg2)
    sock.connect(('8.8.8.8', 80))

    # Returns IP address and port number of the machine that is used at the network interface
    return sock.getsockname()


ADDR = get_ip_address()[0]
PORT = 5050
ADDRESS = (ADDR, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTING CLIENT'

#Create a server socket and bind the address to the socket.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(ADDRESS)


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_len = int(conn.recv(HEADER).decode(FORMAT))
        if msg_len:

            msg = conn.recv(msg_len).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'Message: {msg}')

            conn.send("Message Received".encode(FORMAT))

    conn.close()


def start():
    server_sock.listen()
    print(f'[LISTENING] Server is listining on {ADDRESS}')
    while True:
        conn, addr = server_sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')


print('[STARTING] Server is starting...')
start()

