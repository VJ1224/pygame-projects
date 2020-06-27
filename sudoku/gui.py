import pygame,sys,sudoku,math

# Window details
WINDOW_MULTIPLIER = 5
WINDOW_SIZE = 90 # Square board 9 tiles down and across
WINDOW_WIDTH = WINDOW_HEIGHT = WINDOW_SIZE * WINDOW_MULTIPLIER # Increase  size

# Grid details
SQUARE_SIZE = int(WINDOW_SIZE / 3) * WINDOW_MULTIPLIER
CELL_SIZE = int(SQUARE_SIZE / 3)
BOARD = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

# Colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)
LIGHTGRAY = (200, 200, 200)
GREEN = (0, 255, 0)

def main():
    pygame.init()
    global DISPLAY, FONT_SIZE, FONT, SELECTED
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    FONT_SIZE = 32
    FONT = pygame.font.Font('roboto.ttf',FONT_SIZE)
    # which cell is currently selected
    SELECTED = [None,None]
    pygame.display.set_caption("Sudoku Solver")
    draw()

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # select a cell when mouse clicked on it
            elif event.type == pygame.MOUSEBUTTONUP:
                draw()
                pos = pygame.mouse.get_pos()
                selectCell(pos[0],pos[1])
            elif event.type == pygame.KEYUP:
                # solve the board when space pressed
                if event.key == pygame.K_SPACE:
                    sudoku.solver(BOARD)
                    draw()
                # quite game when escape pressed
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                # ensure that a cell is selected
                elif SELECTED != [None,None]:
                    # change the number in cell if a number key pressed
                    keys = [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,
                    pygame.K_4,pygame.K_5,pygame.K_6,
                    pygame.K_7,pygame.K_8,pygame.K_9]
                    num = 0
                    if event.key in keys:
                        num = pygame.key.name(event.key)
                        x = SELECTED[0]
                        y = SELECTED[1]
                        pos = getIndex(x,y)
                        BOARD[pos[0]][pos[1]] = int(num)
                        draw()
                        SELECTED = [None,None]

        pygame.display.update()

# draw the grid
def drawGrid():
    for x in range(0,WINDOW_WIDTH,CELL_SIZE):
        pygame.draw.line(DISPLAY,LIGHTGRAY,(x,0),(x,WINDOW_HEIGHT))
    for y in range(0,WINDOW_HEIGHT,CELL_SIZE):
        pygame.draw.line(DISPLAY,LIGHTGRAY,(0,y),(WINDOW_WIDTH,y))

    for x in range(0,WINDOW_WIDTH,SQUARE_SIZE):
        pygame.draw.line(DISPLAY,BLACK,(x,0),(x,WINDOW_HEIGHT))
    for y in range(0,WINDOW_HEIGHT,SQUARE_SIZE):
        pygame.draw.line(DISPLAY,BLACK,(0,y),(WINDOW_WIDTH,y))

# draw the numbers in the grid
def drawNumbers():
    CELL_Y = int (CELL_SIZE / 2)
    CELL_X = int (CELL_SIZE / 2)
    for i in range(9):
        for j in range(9):
            if (BOARD[i][j] != 0):
                text = FONT.render('{}'.format(BOARD[i][j]),True,BLACK)
                textRect = text.get_rect()
                textRect.center = (CELL_X + j * CELL_SIZE,CELL_Y + i * CELL_SIZE)
                DISPLAY.blit(text,textRect)

# draw game
def draw():
    DISPLAY.fill(WHITE)
    drawGrid()
    drawNumbers()

# select a cell in the grid by drawing a box
def selectCell(x, y):
    x = roundCellSize(x)
    y = roundCellSize(y)
    SELECTED[0] = x
    SELECTED[1] = y
    rect = pygame.Rect(x,y,50,50)
    pygame.draw.rect(DISPLAY,GREEN,rect,3)

# round the input to the nearest cell
def roundCellSize(n):
    return math.floor(n / CELL_SIZE) * CELL_SIZE

# return index (i,j) of cell in board list
def getIndex(x,y):
    i = y / CELL_SIZE
    j = x / CELL_SIZE
    return (int(i),int(j))

if __name__ == "__main__":
    main()
