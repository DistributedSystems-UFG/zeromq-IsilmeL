import sys
import pickle
import zmq
from constPipe import *  #-

me = str(sys.argv[1])                        # nome desta instância do estágio intermediário

context = zmq.Context()
puller  = context.socket(zmq.PULL)           # recebe workloads dos producers
puller.connect("tcp://"+SRC1+":"+PORT1)      # connect to task source 1
puller.connect("tcp://"+SRC2+":"+PORT2)      # connect to task source 2

pusher  = context.socket(zmq.PUSH)           # reenvia para o consumer final
pusher.bind("tcp://*:"+PORTM)                # bind socket to address

print(me + " started") #-

while True:
  workload  = pickle.loads(puller.recv())          # receive work from a source
  processed = workload * 2                         # nova funcionalidade: processa o dado (dobra o valor) -#
  print(me + " processed " + str(workload) + " -> " + str(processed)) #-
  pusher.send(pickle.dumps((me, processed)))        # send (id, work) to the final consumer
