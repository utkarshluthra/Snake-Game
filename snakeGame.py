import pygame
import time
import random

pygame.init()


# frontend elements:
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)
black = (0, 0, 0)
dw = 600
dh = 400
fontStyle = pygame.font.SysFont("algerian", 14)
scoreStyle= pygame.font.SysFont("comicsansms", 25)

# Creating a screen
disp = pygame.display.set_mode((dw, dh))
# Creating title of display
pygame.display.set_caption("Snake Game by Utkarsh Luthra")


# Snake Dynamics
sBlocks = 10
sSpeed = 15
clock = pygame.time.Clock()

#Creating a Scoring Function:
def sScore(score):
    val=scoreStyle.render("Your Score: "+str(score), True, yellow)
    disp.blit(val, [0,5])

# Creating a Message Function
def mesg(msg, color):
    message = fontStyle.render(msg, True, color)
    a, b = dw/3, dh/2
    disp.blit(message, [a, b])

# Creating a Snake Function for growth of snake
def our_snake(sBlocks, snakeList):
    for x in snakeList:
        pygame.draw.rect(disp, blue, [x[0], x[1], sBlocks, sBlocks])

# Main function
def gameLoop():
    game_over = False
    game_close = False

    x1 = dw/2
    y1 = dh/2

    del_x1 = 0
    del_y1 = 0

    snakeList = []
    snakeLength = 1
    foodx = round(random.randrange(0, dw-sBlocks) / 10.0)*10.0
    foody = round(random.randrange(0, dh-sBlocks) / 10.0)*10.0

    while not game_over:
        while game_close == True:
            disp.fill(black)
            print(score)
            mesg("Press 'Q' to Quit or 'Space' to play again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # So that screen does not close automatically
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    del_x1 = -sBlocks
                    del_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    del_x1 = sBlocks
                    del_y1 = 0
                elif event.key == pygame.K_UP:
                    del_x1 = 0
                    del_y1 = -sBlocks
                elif event.key == pygame.K_DOWN:
                    del_x1 = 0
                    del_y1 = sBlocks

        if x1 >= dw or x1 < 0 or y1 >= dh or y1 < 0:
            game_close = True
        x1 += del_x1
        y1 += del_y1
        disp.fill(black)
        pygame.draw.rect(disp, green, [foodx, foody, sBlocks, sBlocks])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                game_close = True

        our_snake(sBlocks, snakeList)
        sScore(snakeLength-1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dw-sBlocks) / 10.0)*10.0
            foody = round(random.randrange(0, dh-sBlocks) / 10.0)*10.0
            snakeLength += 1
        
        clock.tick(sSpeed)
        
    pygame.quit()
    quit()


gameLoop()
