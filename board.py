# This program codes the Board class for the Connect Four game. 

class Board:

    # Default constructor for the Connect Four board
    def __init__(self, rows = 6, columns = 7):
        self.rows = rows
        self.columns = columns
        self.grid = []

        # Make the grid
        for i in range (0, self.columns):
            self.grid.append([" "])

    # ====== Member Functions to Manage Board State Logic ====== 
    # Function: 
    # Input: 
    # Output: 


    # Function: To print the 2D matrix that represents the state of the board
    # Input: Nothing
    # Output: Prints the state of the board the console terminal
    def printBoard() -> None: 
        pass

        
    # Function: To determine whether a player can place a piece in that column
    # Input: Column integer e.g. 0, 1, ..., 6
    # Output: True or False 
    def isValidColumn(column) -> bool:
        pass


    # Function: To update the board state with the correct player's newly placed piece
    # Input: Column integer e.g. 0, 1, ..., 6 & player
    # Output: The updated board with the newly dropped piece
    def dropPiece(column, player):
        pass


    # Function: To check whether the board is full 
    # Input: Board state.
    # Output: True or False 
    def fullBoard(board):
        pass

    # Function: To check whether the game has been won by a player
    # Input: Board state.
    # Output: True or False (True for win and False for no one won yet)
    def gameOver(board):
        pass

    # Function: To check for four in a row in the horizontal direction
    # Input: Board state.
    # Output: True or False & the winner (Player 1 or Player 2)
    def horizontalWin(board):
        pass

    # Function: To check for four in a row in the vertical direction
    # Input: Board state.
    # Output: True or False & the winner (Player 1 or Player 2)
    def verticalWin(board):
        pass

    # Function: To check for four in a row in the diagonal direction
    # Input: Board state.
    # Output: True or False & the winner (Player 1 or Player 2)
    def diagonalWin(board):
        pass





        


    






