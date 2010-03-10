'''
Created on Mar 9, 2010

@author: Lamneth
'''

class Blar:
    
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        
    def getPos(self):
        return (self.x, self.y)
    
    def moveTo(self, nX, nY):
        self.x = nX
        self.y = nY
        
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        
    def getID(self):
        return self.id