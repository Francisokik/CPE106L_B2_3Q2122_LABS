
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