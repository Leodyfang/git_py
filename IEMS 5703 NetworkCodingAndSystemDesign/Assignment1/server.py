import socket
import sys
import json
import nltk
#check the input argument
if len(sys.argv) != 2:
    print("arguments input error")
    sys.exit()
port = int(sys.argv[1])    #qa port is a num   
# create an INET socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #TCP KEEP ALIVE qa
# bind the socket to the host and a port
server_socket.bind(("localhost", port))
print("Listening for incoming connections on port {}".format(port))
# Listen for incoming connections from clients
server_socket.listen(10)
# A indefinite loop
while True:
    # accept connections from outside
    try:
        (client_socket, address) = server_socket.accept()
        print("Client {} connected.".format(str(address[0]))) #qa  address is a tuple
        content = []
    except Exception as error:
        sys.exit()
    # finally:
    #     client_socket.close()
    # Read data from client and send it back
    while True:
        data = client_socket.recv(2048)
        data = data.decode("utf-8")  #qa must using ~=~.decode to carry the result
        #print(data)
        if data == '':
            print("Client disconnected.")
            client_socket.close()   #！！！
        if data.find('[END]'):#！！！
            content.append(data[:data.find('[END]')])
            content = ''.join(content)
            break
        content.append(data)
    print (content)
    #POS tag
    tokens = nltk.word_tokenize(content)
    tagged = nltk.pos_tag(tokens)
    # print(tagged)
    sendit = json.dumps(tagged)
    # print(sendit)
    # sendit = json.loads(sendit)
    # print(sendit)
    # sendit = json.dumps(sendit)
    # print(sendit)
    client_socket.sendall(sendit.encode('utf-8'))
    # Close the socket
    print("Client disconnected.")
    client_socket.close()
    # sys.exit()  
