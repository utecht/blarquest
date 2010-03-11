'''
Created on Mar 9, 2010

@author: Lamneth
'''

import sys, os
from socket import *
sys.path.append( os.path.join( os.getcwd(), '../client' ) )
from Screen import *
from dataTest import *
import pickle
from threading import Thread



  
class Server(Thread):

    def __init__(self, model):
        host = 'localhost'
        port = 8888
        self.buf = 1024
        addr = (host, port)
        self.UDPSock = socket(AF_INET, SOCK_DGRAM)
        self.UDPSock.bind(addr)
        self.model = model
        Thread.__init__(self)
        
    def run(self):
        print('Server running')
        while(True):
            data, addr = self.UDPSock.recvfrom(self.buf)
            print(data)
            self.process(pickle.loads(data))
    
    def process(self, packet):
        index = packet[0]
        function = packet[1]
        data = packet[2]
        
        if self.model.has(index) == False:
            self.model.addBlar(index, Blar(data[0], data[1]))
        
        if function == 0:
            print(data)
            self.model.getBlar(index).moveTo(data[0], data[1])
        

model = EncapsTest()

server = Server(model)
server.start()

blar = Screen(model)
