import sys
import zmq

SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "localhost"  # IP da máquina do publisher

context = zmq.Context()
socket = context.socket(zmq.SUB)                     # create a subscriber socket
socket.connect("tcp://" + SERVER_IP + ":12345")       # connect to the server
socket.setsockopt(zmq.SUBSCRIBE, b"TIME")             # subscribe to TIME messages
socket.setsockopt(zmq.SUBSCRIBE, b"TEMP")             # nova funcionalidade: assina também TEMP -#

for i in range(10):             # Dez iterações (TIME e TEMP alternados) -#
  msg = socket.recv()           # receive a message related to subscription
  print(msg.decode())           # print the result
