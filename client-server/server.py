import zmq

PORT = "12345"

# nova funcionalidade: servidor agora entende alguns "comandos" além do echo original -#
def upper(msg):   return msg.upper()          #-
def reverse(msg): return msg[::-1]             #-
def count(msg):   return str(len(msg))         #-
OPS = {"UPPER": upper, "REV": reverse, "COUNT": count}  #-

context = zmq.Context()
socket  = context.socket(zmq.REP)         # create reply socket
socket.bind("tcp://*:" + PORT)            # bind socket to address (aceita conexões de qualquer máquina)

print("Server started, waiting for requests...")

while True:
  message = socket.recv().decode()        # wait for incoming message
  if message == "STOP":                   # if not to stop...
    break                                 # break out of loop and end

  op, _, arg = message.partition(" ")     # separa "COMANDO argumento" -#
  func = OPS.get(op)                      #-
  reply = func(arg) if func else message + "*"   # mantém comportamento original como padrão -#
  socket.send(reply.encode())             # send it away (encoded)
