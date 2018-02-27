import socket
import sys
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
import logging
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.INFO)

if len(sys.argv)!=3:
    print("arguments input error")
       sys.exit()
    port_num = int(sys.argv[1]) 