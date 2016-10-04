import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 63

# Setting the game's resolution
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Setting the window's name
pygame.display.set_caption('Race123')

# Setting the game speed
clock = pygame.time.Clock()

# Loads tge car image
carImg = pygame.image.load('car.png')



# defines obstacles in the game
def things(thingx, thingy,thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy,thingw, thingh])

# defines car's position on the surface
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

# Defines text on screen
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Defines text on screen amd starts game after 3 sec
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(3)

    game_loop()

# Defines what happens on crash event
def crash():
    message_display('You Crashed')

# Defines the beginning of the game
def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0



# defines obstacles' location, size and speed
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

# Game logic

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                x = event.pos[0]

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

# things(thingx, thingy,thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width,thing_height, black)
        thing_starty += thing_speed

        car(x, y)

# defines crash

        if x > display_width - car_width  or x <= 0:
            crash()

# Defines box display
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

# Defines collision

        if y < thing_starty + thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit
quit()