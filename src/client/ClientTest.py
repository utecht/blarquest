'''
Created on Mar 9, 2010

@author: Lamneth
'''
from socket import *
import pickle
from dataTest import *
from Screen import Screen
import random, time
from threading import Thread


class Client(Thread):
    def __init__(self, model):
        self.model = model
        host = 'localhost'
        port = 8888
        self.buf = 1024
        self.addr = (host, port)
        self.UDPSock = socket(AF_INET, SOCK_DGRAM)
        self.model = model
        Thread.__init__(self)
    
    def run(self):
        index = random.randint(0, 10000)
        self.model.addBlar(index, Blar(0, 0))
        while(True):
            coors = random.randint(0, 500), random.randint(0, 500)
            self.model.getBlar(index).moveTo(coors[0], coors[1])
            msg = (index, 0, coors)
            self.UDPSock.sendto(pickle.dumps(msg), self.addr)
            time.sleep(.1)
            
            
model = EncapsTest()
model.addBlar(1111, Blar(12, 54))
client = Client(model)
client.start()
blar = Screen(model)
