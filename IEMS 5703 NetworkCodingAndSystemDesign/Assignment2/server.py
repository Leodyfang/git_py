import socket
import sys
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
import logging   #logging have another probem ???
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input  #why pip3 is not avaliable?
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from urllib import request
import tensorflow as tf
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.INFO)
num = 0
def serve_client(socket,graph):
    client = socket[0]
    logging.info("Received Client {}.".format(socket[1]))
    N = socket[2]
    data = client.recv(1024)
    data = data.decode()
    # print(data)
    url = '' + (data[:data.find('[END]')])
    logging.info("Client submitted URL {}".format(url))
    print_local = "image/images000" + str(N + 1) +".jpg"
    local = "./" + print_local
    request.urlretrieve(url, local)
    logging.info("Image saved to {}".format(print_local))
    with graph.as_default():
        model = SqueezeNet()
        img = image.load_img(local, target_size=(227, 227))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)  #type of preds: <class 'numpy.ndarray'>
        preds = decode_predictions(preds)
    result = "(\"{}\", {})".format(preds[0][0][1], preds[0][0][2])
    logging.info("SqueezeNet result: {}".format(result))
    sendit = result.encode()  #why cannot use json?
    # print(sendit)
    client.sendall(sendit)
    client.shutdown(2)  #different between shutdown and close   why??
    logging.info("Client connection closed")
    client.close()


def subprocess(q):
    executor = ThreadPoolExecutor(4)        
    graph = tf.get_default_graph()
    while True:
        # client = q.get()    #lock problem ???
        #address = q.get()
        executor.submit(serve_client, q.get(),graph,)

        
class Server():
    def __init__(self, hostname, port, num):
        self.hostname = hostname
        self.prot = port
        self.num = num
    def start(self):
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_socket.bind((self.hostname, self.prot))
        self.s_socket.listen(10)
        while True:
            (client, address) = self.s_socket.accept()
            logging.info("Client ({}, {}) connected.".format(address[0], address[1]))
            q.put((client, address, self.num))
            self.num = self.num + 1
            #q.put(address)
if __name__ == "__main__":
    if len(sys.argv) == 3:
            port_num = int(sys.argv[1]) 
            max_process = int(sys.argv[2])
    else:
         logging.info("error arguments")
         sys.exit()
    logging.info("Start listening for connections on port {}".format(port_num))
    q = Queue()
    for i in range(max_process):   #???
        p = Process(target=subprocess, args=(q,))
        logging.info("Created process Process-{}".format(i+1))
        p.start()
    #while True:
    Server("localhost", port_num, num).start()
        