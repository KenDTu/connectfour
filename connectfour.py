# This program codes for a game of Connect Four on the terminal
import numpy as np
import pygame
import sys # permits sys.exit 
import math # permits math operations

# ===== Global static variables ===== 
BLUE = (0, 0, 255) # RGB
BLACK = (0, 0, 0)
RED = (255, 0, 0) # Player 1's color
YELLOW = (255, 255, 0) # Player 2's color
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
    pygame.mixer.init()
    sound = pygame.mixer.Sound("coindropsfx.wav")
    sound.play()

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
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # documentation on draw.rect function 
            # https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
            # r*SQUARESIZE+SQUARESIZE offsets to provide the top black strip
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    # Fill in the board with the correct colors for Player 1 and 2
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update() # rerender the display with the changes

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

RADIUS: int = int(SQUARESIZE/2- 5)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update() # updates the display

# documentation for font https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont
myfont = pygame.font.SysFont("monospace", 75)
# ======== end of defining the screen size=======

while not gameOver:

    # in pygame events are all computer inputs e.g. clicks, keys you press, how the mouse is moved etc...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # READ MORE https://www.pygame.org/docs/ref/event.html#pygame.event.custom_type
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            posX = event.pos[0]
            print(posX)
            # print(event.pos)to check the X position for the cursor
            if turn == 0:
                # Draw for Player 1
                pygame.draw.circle(screen, RED, (posX, int(SQUARESIZE/2)), RADIUS)
            else:
                # Draw for Player 2
                pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), RADIUS)
            
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            # print(event.pos[0]) # the X position
            # Ask for Player 1 Input
            if turn == 0:
                posX = event.pos[0]
                col = int(math.floor(posX/SQUARESIZE))
                if isValidLocation(board,col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 1)
                
                    if winningMove(board, 1):
                        label = myfont.render("Player 1 wins!", 1, RED) # 1 is the axis
                        screen.blit(label, (40,10)) # (40,10) is the (x,y) value | .blit updates this specific part of the screen
                        print("Player 1 wins! Congrats!")
                        gameOver = True

                else: 
                    turn += 1 # handles invalid placement error

            # # Ask for Player 2 Input
            else:
                posX = event.pos[0]
                col = int(math.floor(posX/SQUARESIZE))
                if isValidLocation(board,col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 2)
                    

                    if winningMove(board, 2):
                        label = myfont.render("Player 2 wins!", 1, YELLOW) # 1 is the axis
                        screen.blit(label, (40,10)) # (40,10) is the (x,y) value | .blit updates this specific part of the screen
                        print("Player 2 wins! Congrats!")
                        gameOver = True

                else: 
                    turn += 1 # handles invalid placement error
            drawBoard(board)
            printBoard(board)
            turn += 1
            turn = turn % 2 # Mechanism to have the players switch turns

            if gameOver:
                # plays a victory sound
                pygame.time.wait(2000)
                pygame.mixer.init()
                sound = pygame.mixer.Sound("effect.wav")
                sound.play()

                pygame.time.wait(4000)
                
