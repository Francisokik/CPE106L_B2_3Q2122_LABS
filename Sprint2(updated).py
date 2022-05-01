#import numpy 
import numpy as np
import pygame
import sys

#Variables is to make set of array for the game board 6x7
rowCount = 6
columnCount = 7

# function to create the board and return it
def createBoard():
    board = np.zeros((6,7))
    return board

# function for droping what the user choose  
def dropPiece(board,row,col,piece):
    board[row][col]= piece

# function to check if the location is available for playing 
def validLocation(board,col):
    return board[5][col]==0

# function that holds the condition for playing in the next row
def nextRow(board,col):
    for r in range(rowCount):
        if board[r][col]==0:
            return r

# function to display current contents of the board
def printBoard(board):
    print(np.flip(board,0))

# calling the function     
board = createBoard()
printBoard(board)
gameOver = False
turn = 0

while not gameOver:
    #Propmts the first player to make the first move 
    if turn == 0:
        col = int(input("Player 1, Make your Selection(0-6):"))
        #Player 1 will drop a piece on the board
        if validLocation(board,col):
            row = nextRow(board,col)
            dropPiece(board,row,col,1)
         
    #Prompts the second player make the next move 
    else:
        col = int(input("Player 2, Make your Selection(0-6):"))
        #Player 2 will drop a piece on the board
        if validLocation(board,col):
            row = nextRow(board,col)
            dropPiece(board,row,col,2)
    
    #prints the current contents of the board 
    printBoard(board)
             
    turn += 1
    turn = turn % 2

    #initalize pygame
pygame.init()
 
#define our screen size
SQUARESIZE = 100
 
#define width and height of board
width = columnCount * SQUARESIZE
height = (rowCount+1) * SQUARESIZE
 
size = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)
 
screen = pygame.display.set_mode(size)
#Calling function draw_board again
createBoard(board)
pygame.display.update()
 
myfont = pygame.font.SysFont("monospace", 75)
game_over = False
while not game_over:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, PINK, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    #Unfinished code
    #Continuing for the GUI