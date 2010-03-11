'''
Created on Mar 10, 2010

@author: Lamneth
'''

import pygame, sys, os, math
from pygame.locals import *

RED = (255, 0, 0)
DRED = (255, 30, 30)
BLUE = (0, 0, 255)
GREEN = (100, 255, 0)
LBLUE = (0, 255, 255)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
DGREY = (210, 210, 210)
DDGREY = (220, 220, 220)
BLACK = (0, 0, 0)

class Screen():
    
    # X and Y window size
    xSize = 500
    ySize = 500
    
    def __init__(self, model):
        self.model = model
        pygame.init()
        self.window = pygame.display.set_mode((self.xSize, self.ySize))
        pygame.display.set_caption('blar blar blar')
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.run()
        
    def run(self):
        self.running = True
        while self.running:
            self.input(pygame.event.get())
            self.draw()
            self.clock.tick(60)
    
    def draw(self):
        self.screen.fill(WHITE)
        for blar in self.model.getAll():
            pygame.draw.circle(self.screen, RED, blar.getPos(), 5)
        pygame.display.flip()
            
    def input(self, events):
        for event in events:
            if event.type == QUIT:
                self.close()
                
    def close(self):
        sys.exit()
