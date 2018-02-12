import socket
import sys
import json
#check the input argument
if len(sys.argv) != 4:
    print("arguments input error")
    sys.exit()
server_host = sys.argv[1]   #qa
server_port = int(sys.argv[2])
path = sys.argv[3]
# create an INET TCP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server (change localhost to an IP address if necessary)
try:
    soc.connect((server_host, server_port))
    print("Connected to server.")
except Exception as error:
    print("Cannot connect to server at {}:{}".format(server_host, server_port))
    sys.exit()
# Send a message to the server
with open(path, 'r') as f:
    temp = f.read()
    msg = temp + '[END]'
    #msg = temp.append('[END]')
    msg = msg.encode('utf-8')
    soc.send(msg)
# Receive data from the server
content = b''
while True:
    data = soc.recv(1024)
    # if data ==  b'':
    #     print("Cannot connect to server at {}:{}".format(server_host, server_port))
    #     sys.exit()
    content += data
    if data == b'':
        break
try:
    content = json.loads(content) 
except Exception as err:
    print("Runtime error:", err)
    sys.exit()#!!!
#print 
word = []
tag = []
# print(content)
for i in range(0, len(content)):
    word.append(content[i][0])
    tag.append(content[i][1])
    # word.append(content[:len(content)][0])
    # tag.append(content[:len(content)][1])  #qa
print(' ; '.join(word))
print(' ; '.join(tag))
# Always close the socket after use
soc.close()

