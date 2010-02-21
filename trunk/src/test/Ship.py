'''
Created on Feb 11, 2010

@author: Lamneth
'''
from Colors import *
from pygame.locals import *

class Ship:
    walls = []
    floors = []
        
    def getWalls(self):
        global walls
        return self.walls
    
    def addWall(self, wallPoints):
        global walls
        self.walls.append(Wall(wallPoints, 2, self))
    
    def getFloors(self):
        global floors
        return floors
    
    def addFloor(self, floor):
        global floors
        self.floors.append(FloorNode(floor, self))
    
    def applyOffset(self, point):
        return point
    
    def draw(self, screen, pygame):
        global floors
        global walls
        for floor in self.floors:
            floor.draw(screen, pygame)
        for wall in self.walls:
            wall.draw(screen, pygame)
    
class FloorNode:
    verts = []
    parentShip = None
    
    def __init__(self, edgePoints, parent):
        global verts
        global parentShip
        self.verts = edgePoints
        self.parentShip = parent
        
    def getVerts(self):
        global verts
        return self.verts
    
    def getShip(self):
        global parentShip
        return self.parentShip
    
    def draw(self, screen, pygame):
        if len(self.verts) > 2:
            pygame.draw.polygon(screen, DGREY, self.parentShip.applyOffset(self.verts), 0)
            pygame.draw.polygon(screen, WHITE,self. parentShip.applyOffset(self.verts), 2)
    
class Wall:
    verts = (0, 0), (0, 0)
    width = 0
    parent = None
    
    def __init__(self, vert, size, ship):
        global verts
        global width
        global parent
        self.verts = vert
        self.width = size
        self.parent = ship
        
    def get(self, num):
        global verts
        return self.verts[num]
        
    def draw(self, screen, pygame):
        global width
        global parent
        pygame.draw.aaline(screen, BLACK, self.parent.applyOffset(self.get(0)), self.parent.applyOffset(self.get(1)), self.width)
        pygame.draw.circle(screen, RED, self.parent.applyOffset(self.get(0)), 2)
        pygame.draw.circle(screen, RED, self.parent.applyOffset(self.get(1)), 2)
        
    