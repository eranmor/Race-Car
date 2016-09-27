import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 63

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Race123')

clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(3)

    game_loop()

def crash():
    message_display('You Crashed')


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0



        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width  or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit
quit()