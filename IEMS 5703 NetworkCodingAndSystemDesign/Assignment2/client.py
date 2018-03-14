import socket
import sys
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
import logging

logging.basicConfig(
    format = '[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level = logging.INFO)
if len(sys.argv) == 4:
    #log
    # sys.exit()
    host = sys.argv[1]
    port_num = int(sys.argv[2]) 
    url = sys.argv[3]
    url = url + "[END]"
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    c_socket.connect((host, port_num))   #??? portnum shown in the terminal
    logging.info(" Connected to server at ({}, {})".format(host, port_num))
except Exception as error:
    logging.info(error)
c_socket.send(url.encode('utf-8'))
logging.info("URL sent to the server")
# while True:
data = c_socket.recv(1024)
result = data.decode()
logging.info("Server response: {}".format(result))
c_socket.close()







# def worker():
#     if len(sys.argv) == 4:
#         #log
#         # sys.exit()
#         host = sys.argv[1]
#         port_num = int(sys.argv[2]) 
#         url = sys.argv[3]
#         url = url + "[END]"
#     c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         c_socket.connect((host, port_num))   #??? portnum shown in the terminal
#         logging.info(" Connected to server at ({}, {})".format(host, port_num))
#     except Exception as error:
#         logging.info(error)
#     c_socket.send(url.encode('utf-8'))
#     logging.info("URL sent to the server")
#     # while True:
#     data = c_socket.recv(1024)
#     result = data.decode()
#     logging.info("Server response: {}".format(result))
#     c_socket.close()

# def run():
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         [executor.submit(worker) for _ in range(10)]
#    #worker()


# if __name__ == '__main__':
#     run()