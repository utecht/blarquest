'''
Created on Mar 9, 2010

@author: Lamneth
'''

class Blar:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getPos(self):
        return (self.x, self.y)
    
    def moveTo(self, nX, nY):
        self.x = nX
        self.y = nY
        
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
    
class EncapsTest:
    set = {}
        
    def addBlar(self, index, blar):
        self.set[index] = blar
        
    def getBlar(self, index):
        return self.set[index]
    
    def getAll(self):
        return self.set.values()
    
    def has(self, index):
        return index in self.set.keys()
        