import sys
import zmq

SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "localhost"  # IP da máquina do servidor
PORT = "12345"

context = zmq.Context()
socket  = context.socket(zmq.REQ)                    # create request socket
socket.connect("tcp://" + SERVER_IP + ":" + PORT)     # block until connected

# nova funcionalidade: envia algumas mensagens usando os novos comandos do servidor -#
mensagens = ["Hello world", "UPPER hello world", "REV hello world", "COUNT hello world"]  #-

for msg in mensagens:                     #-
  socket.send(msg.encode())               # send message
  reply = socket.recv()                   # block until response
  print(msg + " -> " + reply.decode())    # print result

socket.send(b"STOP")                      # tell server to stop
