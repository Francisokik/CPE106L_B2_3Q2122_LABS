from typing import Any
import numpy as np
import pygame
import sys
import math
from board import gameBoard
from board import piecePlayed
from board import validLoc
from board import nextRow
from board import printBoard
from board import winCondition
from board import checkTie 

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
 
myfont = pygame.font.SysFont("monospace", 75)
 
while not gameOver:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, boxSize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, LIGHTBLUE, (posx, int(boxSize/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, BEIGE, (posx, int(boxSize/2)), RADIUS)
        pygame.display.update()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, boxSize))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/boxSize))
 
                if validLoc(board, col):
                    row = nextRow(board, col)
                    piecePlayed(board, row, col, 1)
 
                    if winCondition(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, LIGHTBLUE)
                        screen.blit(label, (40,10))
                        gameOver = True

            # # Ask for Player 2 Input and Tie
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/boxSize))
 
                if validLoc(board, col):
                    row = nextRow(board, col)
                    piecePlayed(board, row, col, 2)
 
                    if winCondition(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, BEIGE)
                        screen.blit(label, (40,10))
                        gameOver = True
                    
                    if checkTie(board, 1, 2):
                        label = myfont.render("TIE/DRAW", 1, WHITE)
                        screen.blit(label, (40,10))
                        gameOver = True 
                    

            printBoard(board)
            makeBoard(board)

            #players are taking turns
            turn += 1
            turn = turn % 2

        #Game over 
        if gameOver:
            pygame.time.wait(3000)
            
                
                
                        