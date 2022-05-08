import pygame
import numpy as np


rowNum = 6
colNum = 7

boxSize = 100

def gameBoard():
    board = np.zeros((rowNum,colNum))
    return board
 
def piecePlayed(board, row, col, piece):
    board[row][col] = piece
 
def validLoc(board, col):
    return board[rowNum-1][col] == 0
 
def nextRow(board, col):
    for r in range(rowNum):
        if board[r][col] == 0:
            return r
 
def printBoard(board):
    print(np.flip(board, 0))
 
def winCondition(board, piece):
    # Check horizontal locations for win
    for c in range(colNum-3):
        for r in range(rowNum):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check vertical locations for win
    for c in range(colNum):
        for r in range(rowNum-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diaganols
    for c in range(colNum-3):
        for r in range(rowNum-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for c in range(colNum-3):
        for r in range(3, rowNum):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
 
def checkTie(board, row, col):
    for c in range(colNum):
        for r in range(rowNum):
            if 0 not in board:
                print('TIE')
                return True


