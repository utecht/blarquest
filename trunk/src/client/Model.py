'''
Created on Mar 9, 2010

@author: Lamneth
'''

class Blar:

    # facing is based on cardinal direction
    # 1 2 3
    # 4 * 5
    # 6 7 8
    facing = 7
    # walkFrame is for animation
    walkFrame = 0
    
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
        
class Packet:
    packet = []
    move = 0
    add = 1
    remove = 2

    def __init__(self, id):
        self.id = id

    def getPacket(self):
        return self.id, self.packet

    #move packet will be id 0
    #obj must be a blar
    #packet will be (id, (x, y))
    def addMove(self, id, obj):
        loc = obj.getPos()
        self.packet[len(self.packet)] = self.move, (id, loc)

    def addObj(self, id, obj):
        self.packet[len(self.packet)] = self.add, (id, obj)

    def removeObj(self, id):
        self.packet[len(self.packet)] = self.remove, id
