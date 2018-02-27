import socket
import sys
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
import logging
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.INFO)
executor = ThreadPoolExecutor(max_workers=4)
def serve_client():
    **
def subprocess(q,i,):
    while True:
        client = q.get()
        address = q.get()
        executor.submit(serve_client, client, address)
        client.sendall("Hello".encode())
        client.close()
class Server(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.prot = port
    def start(self):
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_socket.bind(self.hostname, self.prot)
        self.s_socket.listen()
        while True:
            (client, address) = self.s_socket.accept()
            q.put(client)
            q.put(address)
if __name__ == "__main__":
    q = Queue()
    for i in range(4):
        p = Process(target=subprocess, args=(q,i))
        p.start()
    if len(sys.argv) != 3:
        print("arguments input error")
        sys.exit()
        port_num = int(sys.argv[1]) 
    while True:
        Server("0.0.0.0", port_num)
    