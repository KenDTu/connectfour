# This program codes for a game of Connect Four on the terminal
import numpy as np
import pygame

ROW_COUNT: int = 6
COLUMN_COUNT: int = 7

# Create the Connect Four Board
def createBoard():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# Flips the board so the piece build upwards
def printBoard(board):
    print(np.flip(board, 0))

# Drops the piece into column
def dropPiece(board, row, col, piece):
    board[row][col] = piece

# Verifies that the column is a valid location for the piece
def isValidLocation(board, col):
    return board[ROW_COUNT-1][col] == 0 

# Obtains the next open column by checking each column
def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winningMove(board, piece):
    # Check all the horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
        
    # Check all vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
         
    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            
    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
# Draw the board to the pygame graphics
def drawBoard(board):
    pass
            
board = createBoard()
print(board)
gameOver: bool = False
turn: int = 0         # This defines whose turn it is to play 

pygame.init()

# ====== Defining the  screen size =========
SQUARESIZE: int = 100 # each square size is 100 pixels
width: int = COLUMN_COUNT * SQUARESIZE
height: int = (ROW_COUNT+1) * SQUARESIZE

size: tuple = (width, height)

screen = pygame.display.set_mode(size)
# ======== end of defining the screen size=======

while not gameOver:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1, make your selection (0-6)"))
        if isValidLocation(board,col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
        
            if winningMove(board, 1):
                print("Player 1 wins! Congrats!")
                gameOver = True
                break
        else: 
            turn += 1 # handles invalid placement error

    # Ask for Player 2 Input
    else:
        col = int(input("Player 2, make your selection (0-6)"))

        if isValidLocation(board,col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
            

            if winningMove(board, 2):
                print("Player 2 wins! Congrats!")
                gameOver = True
                break
        else: 
            turn += 1 # handles invalid placement error

    printBoard(board)
    turn += 1
    turn = turn % 2 # Mechanism to have the players switch turns


