# This program codes for a game of Connect Four on the terminal
import numpy as np

ROW_COUNT: int = 6
COLUMN_COUNT: int = 7

# Create the Connect Four Board
def createBoard():
    board = np.zeros((6,7))
    return board

# Flips the board so the piece build upwards
def printBoard(board):
    print(np.flip(board, 0))

# Drops the piece into column
def dropPiece(board, row, col, piece):
    board[row][col] = piece

# Verifies that the column is a valid location for the piece
def isValidLocation(board, col):
    return board[5][col] == 0 #should the row be the 0?

# Obtains the next open column by checking each column
def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


board = createBoard()
print(board)
gameOver: bool = False
turn: int = 0         # This defines whose turn it is to play 

while not gameOver:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1, make your selection (0-6)"))
        print(col)
        print(type(col))
        
        if isValidLocation(board,col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
        else: 
            print("Not a valid location.")


    # Ask for Player 2 Input
    else:
        col = int(input("Player 2, make your selection (0-6)"))
        print(col)
        print(type(col))

        if isValidLocation(board,col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)

    printBoard(board)
    turn += 1
    turn = turn % 2 # Mechanism to have the players switch turns


