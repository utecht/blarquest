'''
Created on Mar 9, 2010

@author: Lamneth
'''

from socket import *
import pickle
from ..client.dataTest import *


host = 'localhost'
port = 8888
buf = 1024
addr = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

print('Server running')
while(True):
    data, addr = UDPSock.recvfrom(buf)
    print(data)
    print(pickle.loads(data).getCors()) 