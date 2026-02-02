import socket
import socketserver
import pickle
import struct
import logging

class LogKeeper(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack(">L", chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
               chunk += self.connection.recv(slen - len(chunk))   


            obj = pickle.loads(chunk) 
            record = logging.makeLogRecord(obj)


logging.basicConfig(
    filename='server_received_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

server = socketserver.TCPServer(("127.0.0.1", 12345), LogKeeper)
print("Server is listening for logs...")
server.serve_forever()