import zmq, time, pickle, sys
from constPipe import *  #-

context = zmq.Context()
me = str(sys.argv[1])
r  = context.socket(zmq.PULL)     # create a pull socket
pm = "tcp://"+ MID +":"+ PORTM    # address of the intermediate stage (novo estágio) -#
r.connect(pm)                     # connect to the intermediate stage -#
#-
print (me + " started") #-

while True:
  work = pickle.loads(r.recv())   # receive work from a source
  print (me + " received " + str(work[1]) + " from " + work[0]) #-
  time.sleep(work[1]*0.01)        # pretend to work
