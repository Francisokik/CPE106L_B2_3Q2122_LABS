#import numpy 
import numpy as np
import pygame

#Variables is to make set of array for the game board 6x7
black = (0, 0, 0)
rowCount = 6
columnCount = 7

#function to draw GUI
def drawBoard(board):
    for c in range(columnCount):
        for r in range(rowCount):
            pygame.draw.rect(screen, black, (c*sqrSize, r*sqrSize+sqrSize, sqrSize, sqrSize))
            pygame.draw.circle(screen, black, (int(c*sqrSize+sqrSize/2), int(r*sqrSize+sqrSize+sqrSize/2)), radius)
    pygame.display.update()

    #initalize pygame
pygame.init()
 
#define our screen size
sqrSize = 100
 
#define width and height of board
width = columnCount * sqrSize
height = (rowCount+1) * sqrSize
 
size = (width, height)
 
radius = int(sqrSize/2 - 5)
 
screen = pygame.display.set_mode(size)
 
myfont = pygame.font.SysFont("monospace", 75)

gameOver = False
turn = 0


    #Unfinished code
    #Continuing for the GUI