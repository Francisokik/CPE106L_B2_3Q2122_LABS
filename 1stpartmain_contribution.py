from typing import Any
import numpy as np
import pygame
import sys
import math
from board_part2 import gameBoard
from board_part2 import piecePlayed
from board_part2 import validLoc
from board_part2 import nextRow
from board_part2 import printBoard
from board_part2 import winCondition
from board_part2 import checkTie 

#Colors used
DARK = (15,32,67)
BLACK = (0,0,0)
LIGHTBLUE = (122,207,221)
BEIGE = (213,164,88)
WHITE = (255, 255, 255)

rowNum = 6
colNum = 7

#function to make the board 
def makeBoard(board):
    for c in range(colNum):
        for r in range(rowNum):
            pygame.draw.rect(screen, DARK, (c*boxSize, r*boxSize+boxSize, boxSize, boxSize))
            pygame.draw.circle(screen, BLACK, (int(c*boxSize+boxSize/2), int(r*boxSize+boxSize+boxSize/2)), RADIUS)
     
    for c in range(colNum):
        for r in range(rowNum):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, LIGHTBLUE, (int(c*boxSize+boxSize/2), height-int(r*boxSize+boxSize/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, BEIGE, (int(c*boxSize+boxSize/2), height-int(r*boxSize+boxSize/2)), RADIUS)
    pygame.display.update()


board = gameBoard()
printBoard(board)
gameOver = False
turn = 0
 
#initalize pygame
pygame.init()
 
#define our screen size
boxSize = 100
 
#define width and height of board
width = colNum * boxSize
height = (rowNum+1) * boxSize
#define size and raidus
size = (width, height)
RADIUS = int(boxSize/2 - 5)
 

screen = pygame.display.set_mode(size)

#Calling function makeBoard again
makeBoard(board)
pygame.display.update()
 
myfont = pygame.font.SysFont("Comic Sans MS", 70)