# This program codes for a game of Connect Four on the terminal
import numpy as np

def createBoard():
    board = np.zeros((6,7))
    return board

board = createBoard()
gameOver: bool = False
turn: int = 0         # This defines whose turn it is to play 

print(board)

while not gameOver:
    # Ask for the Player 1 Input
    
