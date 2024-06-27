import pygame
import sys
import random


pygame.init()


BLACK = (0,0,0)

DIM = 2
scale = 4
CELL_SIZE = 50 * scale

BLANK = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4



width = DIM*CELL_SIZE 
height = DIM*CELL_SIZE
WINDOW_SIZE = (width,height)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WaveCollapeTeste")

grid = []

tiles = []

rules = {
    BLANK:[
        [BLANK,UP], # UP TILE
        [BLANK,RIGHT], # RIGHT TILE
        [BLANK,DOWN], # DOWN TILE
        [BLANK, LEFT], # LEFT TILE
    ],
    UP:[
        [RIGHT,LEFT,DOWN], # UP TILE
        [LEFT,UP,DOWN], # RIGHT TILE
        [BLANK,DOWN], # DOWN TILE
        [RIGHT,UP,DOWN], # LEFT TILE

    ],
    RIGHT:[
        [RIGHT,LEFT,DOWN], # UP TILE
        [LEFT,UP,DOWN], # RIGHT TILE
        [RIGHT,LEFT,UP], # DOWN TILE
        [BLANK,LEFT], # LEFT TILE
    ],
    DOWN:[
        [BLANK,UP], # UP TILE
        [LEFT,UP,DOWN], # RIGHT TILE
        [RIGHT,LEFT,UP], # DOWN TILE
        [RIGHT,UP,DOWN], # LEFT TILE
    ],
    LEFT:[
        [RIGHT,LEFT,DOWN], # UP TILE
        [UP,DOWN,RIGHT],# RIGHT TILE
        [RIGHT,LEFT,UP], # DOWN TILE
        [BLANK,RIGHT],# LEFT TILE
    ]
}



def checkValid(arr,valid):
    return [item for item in arr if (item in valid)]


def preload():
    
    tiles.append(pygame.transform.scale(pygame.image.load("TileTXT/waveCollapse/Teste/blank.png"), (CELL_SIZE, CELL_SIZE)))
    tiles.append(pygame.transform.scale(pygame.image.load("TileTXT/waveCollapse/Teste/up.png"), (CELL_SIZE, CELL_SIZE)))
    tiles.append(pygame.transform.scale(pygame.image.load("TileTXT/waveCollapse/Teste/right.png"), (CELL_SIZE, CELL_SIZE)))
    tiles.append(pygame.transform.scale(pygame.image.load("TileTXT/waveCollapse/Teste/down.png"), (CELL_SIZE, CELL_SIZE)))
    tiles.append(pygame.transform.scale(pygame.image.load("TileTXT/waveCollapse/Teste/left.png"), (CELL_SIZE, CELL_SIZE)))

def draw_matrix(grid):
    #print()
    #print("firstGRID:"+str(grid))
    gridCopy = grid.copy()
    gridCopy = [i for i in gridCopy if i["collapsed"]==False]
    gridCopy = sorted(gridCopy, key=lambda x: len(x["options"]) )
    
    lenG = len(gridCopy[0]["options"])
    stopIndex = 0
    for i in range(len(gridCopy)):
        if (len(gridCopy[i]["options"])>lenG):
            stopIndex=i
            break
    if stopIndex>0:
        del gridCopy[stopIndex:len(gridCopy)-stopIndex]
    
    cell = random.choice(gridCopy)
    if cell["options"]!=[]:
        cell["collapsed"]=True
        pick = random.choice(cell["options"])
        cell["options"] = [pick]
    

    #print()
   # print("sorted:"+str(gridCopy))
    for row in range(DIM):
        for col in range(DIM):
            cell = grid[col+row*DIM] 
            if cell["collapsed"]:
                tile_index = cell["options"][0]
                tile = tiles[tile_index]
                screen.blit(tile, (col * CELL_SIZE, row * CELL_SIZE))
            else:
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLACK, rect)

    nextGrid = [{"collapsed":False,"options":[BLANK,UP,RIGHT,DOWN,LEFT]} for i in range(DIM*DIM)]
    for row in range(DIM):
        for col in range(DIM):

            index = col+row*DIM
            print("index:"+str(index))
            if grid[index]["collapsed"]:
                nextGrid[index] = grid[index] 
            else:
                opitions=[BLANK,UP,RIGHT,DOWN,LEFT]
                
                # 0 is blank
                # 1 is 
                
                #Look up
                if (row>0):
                    up = grid[col + (row -1) * DIM]
                    print("value OF UP:"+str(up))
                    validOptions=[]
                    for opition in up["options"]:
                        valid = rules[opition][2]
                        validOptions =list(set(validOptions+valid))
                    print("Look up:"+str(validOptions))
                    opitions =checkValid(opitions,validOptions)
                #Look right
                if (col< DIM -1 ):
                    right = grid[(col+1) + row * DIM]
                    print("value OF RIGHT:"+str(right))
                    validOptions=[]
                    for opition in right["options"]:
                        valid = rules[opition][3]
                        validOptions =list(set(validOptions+valid))
                    print("Look right:"+str(validOptions))
                    opitions = checkValid(opitions,validOptions)
                #Look down 
                if (row<DIM - 1):
                    down = grid[col + (row + 1) * DIM]
                    print("value OF DOWN:"+str(down))
                    validOptions=[]
                    for opition in down["options"]:
                        valid = rules[opition][0]
                        validOptions =list(set(validOptions+valid)) 
                    print("Look down:"+str(validOptions))
                    opitions = checkValid(opitions,validOptions)
                #Look left
                if (col>0):
                    left = grid[(col-1) + row * DIM]
                    print("value OF LEFT:"+str(left))
                    validOptions=[]
                    for opition in left["options"]:
                        valid = rules[opition][1]
                        validOptions =list(set(validOptions+valid))
                    print("Look left:"+str(validOptions))
                    opitions = checkValid(opitions,validOptions)

                
                nextGrid[index]["options"] = opitions
                nextGrid[index]["collapsed"]=False
    
    #print()
    #print("CHange GRID:"+str(nextGrid))
    return nextGrid
    

                
preload()

for i in range(DIM*DIM):
    grid.append({"collapsed":False,
             "options":[BLANK,UP,RIGHT,DOWN,LEFT]
             })



print()

def newLOOP(grid):
    screen.fill((255, 255, 255)) 

    grid = draw_matrix(grid)
    
    pygame.display.flip()
    return grid

#for i in range(DIM*DIM):
    #grid=newLOOP(grid)
    #print(grid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid=newLOOP(grid)
            print(grid)

