import pygame, sys, os, math
from pygame.locals import *
from SimpleFontManager import cFontManager
from Colors import *
from Ship import *

    
ship = None

curFloor = [] 
# A line is being drawn
newLine = False
# Snap to is enabled
snapTo = True
# The starting point of the line to be drawn
startingPoint = 0, 0
# Scaling value of the screen
scale = 1
# Grid scale
gridScale = 10
# X and Y offsets
xOffset = 0
yOffset = 0
# X and Y window size
xSize = 500
ySize = 500
# current placement mode
mode = 'WALL'
# mans pos
mans = -20, -20
mansGoal = -20, -20



def startLine(point):
    global startingPoint
    global newLine
    if snapTo:
        startingPoint = snapPoint(point)
    else:
        startingPoint = point    
    newLine = True
            
def endLine(point):
    global startingPoint
    global newLine
    global ship
    newLine = False
    if snapTo:
        point = snapPoint(point) 
    if startingPoint != point:
        ship.addWall((startingPoint, point))
        #lines.append((applyOffset(startingPoint), applyOffset(point)))
    
def addFloorPoint(point):
    global curFloor
    global ship
    if snapTo:
        point = snapPoint(point) 
    if doesPointExist(point):
        if curFloor.count(point) > 0:
            #floors.append(curFloor)
            if len(curFloor) > 2:
                ship.addFloor(curFloor)
            curFloor = []
        else:
            curFloor.append(applyOffset(point))           
        
def doesPointExist(point):
    global ship
    for wall in ship.getWalls():
        if point == wall.get(0) or point == wall.get(1):
            return True
    return False
    
def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

def applyOffset(startingPoint):
    offsetPoint = startingPoint[0] + xOffset, startingPoint[1] + yOffset
    return offsetPoint

def snapPoint(point):
    xDiff = point[0] % gridScale
    if xDiff > (gridScale / 2):
        xDiff -= gridScale
    yDiff = point[1] % gridScale
    if yDiff > (gridScale / 2):
        yDiff -= gridScale        
    snappedPoint = (point[0] - xDiff), (point[1] - yDiff)
    return snappedPoint

def placeMans(point):
    global mans
    mans = applyOffset(point)
    
def placeMansGoal(point):
    global mansGoal
    mansGoal = applyOffset(point)

def draw():
    global ship
    screen.fill(WHITE)
    #draw Ship
    fillGrid()
    ship.draw(screen, pygame)
    drawFloors()
    # draw mans and mansGoal
    pygame.draw.circle(screen, BLUE, mans, 10)
    pygame.draw.circle(screen, GREEN, mansGoal, 10)

    if newLine:
        drawCurrentLine()
    drawStats()
    pygame.display.flip()

def drawStats():
    fontMgr.Draw(screen, None, 16, 'Grid Size: ' + str(gridScale), (5, 10), RED, True)
    fontMgr.Draw(screen, None, 16, mode, (5, 25), RED, True)


def fillGrid():
    for x in range(int(xSize / gridScale)):
        pygame.draw.line(screen, GREY, (x * gridScale, 0), (x * gridScale, ySize), 1)
    for y in range(int(ySize / gridScale)):
        pygame.draw.line(screen, GREY, (0, y * gridScale), (xSize, y * gridScale), 1)
    
def drawCurrentLine():
    global startingPoint
    if snapTo:
        endingPoint = snapPoint(pygame.mouse.get_pos())
    else:
        endingPoint = pygame.mouse.get_pos()
    pygame.draw.aaline(screen, RED, startingPoint, endingPoint, 2)
    
def drawFloors():
    global curFloor
    for point in curFloor:
        pygame.draw.circle(screen, BLACK, point, 4, 2)
    if len(curFloor) > 2:
        pygame.draw.polygon(screen, LBLUE, curFloor, 0)
        
def input(events):
    global gridScale
    global mode
    for event in events:
        if event.type == QUIT:
            close()
        elif event.type == MOUSEBUTTONDOWN:
            if mode == 'WALL':
                startLine(pygame.mouse.get_pos()) 
        elif event.type == MOUSEBUTTONUP:
            if mode == 'WALL':
                endLine(pygame.mouse.get_pos())
            elif mode == 'FLOOR':
                addFloorPoint(pygame.mouse.get_pos())
            elif mode == 'MANS':
                placeMans(pygame.mouse.get_pos())
            elif mode == 'MANS GOAL':
                placeMansGoal(pygame.mouse.get_pos())
        elif event.type == KEYDOWN:
            if event.key == K_PAGEUP:
                gridScale += 1
            elif event.key == K_PAGEDOWN:
                gridScale -= 1       
            elif event.key == K_1:
                mode = 'WALL'
            elif event.key == K_2:
                mode = 'FLOOR'
            elif event.key == K_3:
                mode = 'MANS'
            elif event.key == K_4:
                mode = 'MANS GOAL'
                
def startEditor(edShip):
    global ship
    global window
    global screen
    global pygame
    global fontMgr
    ship = edShip
    pygame.init()
    window = pygame.display.set_mode((xSize, ySize))
    pygame.display.set_caption('blar blar blar')
    screen = pygame.display.get_surface()

    fontMgr = cFontManager((('arial', 16), (None, 16), ('arial', 24)))
    clock = pygame.time.Clock()
    while True:
        input(pygame.event.get())
        draw()
        clock.tick(60)
        
def close():
    sys.exit()

    