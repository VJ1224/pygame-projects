import pygame,sys,math,random
from player import Player
from obstacle import Obstacle

# Winow details
WINDOW_MULTIPLIER = 10
WINDOW_WIDTH = 80 * WINDOW_MULTIPLIER
WINDOW_HEIGHT = 24 * WINDOW_MULTIPLIER
WINDOW_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT)

# Colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)
LIGHTGRAY = (200, 200, 200)

# main game loop
def main():
    pygame.init()
    clock = pygame.time.Clock()
    global DISPLAY,FONT, SCORE, PLAYER, OBSTACLE, RECT_OBSTACLE, RECT_PLAYER

    SCORE = 0
    Player.height *= WINDOW_MULTIPLIER
    Player.width *= WINDOW_MULTIPLIER
    Player.jumpCount *= WINDOW_MULTIPLIER
    Player.jumpHeight *= WINDOW_MULTIPLIER
    Obstacle.height *= WINDOW_MULTIPLIER
    Obstacle.width *= WINDOW_MULTIPLIER
    Obstacle.size *= WINDOW_MULTIPLIER
    PLAYER = Player(int(WINDOW_WIDTH/WINDOW_MULTIPLIER / 2),
    WINDOW_HEIGHT-int(WINDOW_HEIGHT/WINDOW_MULTIPLIER) - Player.height)
    OBSTACLE = Obstacle(WINDOW_WIDTH,
    WINDOW_HEIGHT - int(WINDOW_HEIGHT/WINDOW_MULTIPLIER) - Obstacle.height)
    RECT_OBSTACLE = pygame.Rect(int(OBSTACLE.x),int(OBSTACLE.y),int(OBSTACLE.width),int(OBSTACLE.height))
    RECT_PLAYER = pygame.Rect(int(PLAYER.x),int(PLAYER.y),int(PLAYER.width),int(PLAYER.height))

    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    FONT = pygame.font.Font('roboto.ttf',24)

    pygame.display.set_caption("Chrome Dino")
    draw()

    # main game loop
    while True:
        timedelta = clock.tick(60)
        timedelta /= 1000
        SCORE += 1
        OBSTACLE.x -= timedelta * (SCORE / 2)
        RECT_OBSTACLE = pygame.Rect(int(OBSTACLE.x),int(OBSTACLE.y),int(OBSTACLE.width),int(OBSTACLE.height))
        RECT_PLAYER = pygame.Rect(int(PLAYER.x),int(PLAYER.y),int(PLAYER.width),int(PLAYER.height))

        if(RECT_PLAYER.colliderect(RECT_OBSTACLE)):
            print(SCORE)
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not PLAYER.isJump:
                        PLAYER.jump()
                elif event.key == pygame.K_DOWN:
                    PLAYER.height /= 2
                    PLAYER.y += PLAYER.height
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    PLAYER.y -= PLAYER.height
                    PLAYER.height *= 2

        if PLAYER.isJump:
            if PLAYER.jumpCount >= -PLAYER.jumpHeight:
                PLAYER.y -= PLAYER.jumpCount * abs(PLAYER.jumpCount)
                PLAYER.jumpCount -= PLAYER.jumpHeight / 15
            else:
                PLAYER.jumpCount = PLAYER.jumpHeight
                PLAYER.isJump = False

        draw()

        pygame.display.update()

# draw game screen with sprites
def draw():
    DISPLAY.fill(WHITE)
    pygame.draw.line(DISPLAY,LIGHTGRAY,(0,
    WINDOW_HEIGHT-int(WINDOW_HEIGHT/WINDOW_MULTIPLIER)),
    (WINDOW_WIDTH,WINDOW_HEIGHT-int(WINDOW_HEIGHT/WINDOW_MULTIPLIER)))
    drawScore()
    clearPlayer()
    drawPlayer()
    drawObstacle()

def drawObstacle():
    if (OBSTACLE.x) <= - WINDOW_WIDTH / 10:
        OBSTACLE.x = WINDOW_WIDTH
        OBSTACLE.y = WINDOW_HEIGHT - int(WINDOW_HEIGHT/WINDOW_MULTIPLIER) - Obstacle.height
        OBSTACLE.changeY(Obstacle.height + Obstacle.height / 2)
    pygame.draw.rect(DISPLAY,BLACK,RECT_OBSTACLE)

def drawScore():
    text = FONT.render('SCORE: {}'.format(SCORE),True,BLACK)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH - int(WINDOW_WIDTH/WINDOW_MULTIPLIER),
    int(WINDOW_HEIGHT/WINDOW_MULTIPLIER))
    DISPLAY.blit(text,textRect)

def drawPlayer():
    pygame.draw.rect(DISPLAY,BLACK,RECT_PLAYER)

def clearPlayer():
    pygame.draw.rect(DISPLAY,WHITE,RECT_PLAYER)

if __name__ == "__main__":
    main()
