#import numpy 
import numpy as np

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

    #Unfinished code
    #Continuing for the GUI