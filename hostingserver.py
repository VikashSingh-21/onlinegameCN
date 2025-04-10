import socket
import threading
import random

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = (SERVER_ADDRESS, SERVER_PORT)

# Bind the address to the server socket
sock.bind(host)
maxSockets = 16

print('Server is on')

allAddresses = []

hostSocket = []
hostcode = []

def handle_message(data, client_address):
    message = data.decode("utf-8")
    print(message)
    if "HOST:" in message:
        print("bitch")
        host_ip = message.split("HOST:")[1].split(",")[0]
        host_port = message.split(",")[1].split("RNG:")[0]
        host_port = int(host_port)
        host_address = (host_ip,host_port)
        code = message.split("RNG:")[1]
        print(code)
        hostcode.append(code)
        hostSocket.append(host_address)

    if "CODE:" in message:
        peercode = message.split("CODE:")[1].strip().split("ACK:")[0]
        print("Peercode:", peercode)
        print("Hostcode list:", hostcode)
        if peercode in hostcode:
            print("Peercode found in hostcode")
            codeindex = hostcode.index(peercode)
            hostadress = hostSocket[codeindex]
            # tcp
            hostfound = "HOSTCONNECT:" + str(hostadress) + "\n"
            sock.sendto(hostfound.encode("utf-8"), client_address)
            sock.sendto(message.encode("utf-8"),client_address)
            print("Success")
        else:
            print("Peercode not found in hostcode")



def server_loop():
    while True:
        data, client_address = sock.recvfrom(1024)
        handle_message(data, client_address)
        print(f"Received message from {client_address}")
        print(f"Received message from {data}")

server_thread = threading.Thread(target=server_loop)
server_thread.start()
