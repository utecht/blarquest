'''
Created on Mar 9, 2010

@author: Lamneth
'''
from socket import *
import pickle
from dataTest import Blar

host = 'localhost'
port = 8888
buf = 1024
addr = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)
msg = Blar(7, 3, 1)
UDPSock.sendto(pickle.dumps(msg), addr)
UDPSock.close()