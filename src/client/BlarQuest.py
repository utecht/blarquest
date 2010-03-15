'''
Created on Feb 21, 2010

@author: Lamneth
'''
from Screen import *
from Model import *
from ClientTest import *
import time


def draw(screen):
    print('Drawing')
    screen.draw

def think(model):
    print('Thinking...')

def main():
    # the main code goes here
    print('Blar Quest')
    # main game will have 2 threads, the neworking and screen thread
    model = Model()
    client = Client(model)
    screen = Screen(model)
    running = True
    client.start()
    while(running):
        think(model, client)
        draw(screen)
        time.sleep(.1)
 
if __name__ == "__main__":
    main()
