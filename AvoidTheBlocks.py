import pygame
import time
import random
import speech


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

car_width = 63

# Setting the game's resolution
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Setting the window's name
pygame.display.set_caption('Avoid The Blocks')

# Setting the game speed
clock = pygame.time.Clock()

# Loads tge car image
carImg = pygame.image.load('car.png')

# defines score
def things_dodged(count):
    font = pygame.font.SysFont(None, 25 )
    text = font.render("Dodged: " +str(count), True, black)
    # Display score
    gameDisplay.blit(text, (0,0))

# defines obstacles in the game
def things(thingx, thingy,thingw, thingh, color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy,thingw, thingh])

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

# Defines button
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(

    )
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
        #         game_loop()
        #     elif action == "quit":
        #         pygame.quit()
        #         quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smalltext = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smalltext)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

# defines game menu

def game_intro():
    intro = True

# Game music
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(loops=-1, start=0.0)
    pygame.mixer.music.set_volume(0.1)

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Avoid The Blocks", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

#        mouse = pygame.mouse.get_pos()

        button('GO!', 150, 450, 100, 50, green, bright_green, game_loop)

        button('Quit', 550, 450, 100, 50, red, bright_red, quit)

# manual buttons settings
        '''
        if 150 + 100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50 ))

        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('GO!', smalltext)
        textRect.center = ( (150 + (100/2)),(450 + (50/2)) )
        gameDisplay.blit(textSurf, textRect)

        if 500 + 100 > mouse[0] > 550 and 450 +50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (550, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
        '''


        pygame.display.update()
        clock.tick(15)


# Defines the beginning of the game
def game_loop():


    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

# defines obstacles' location, size and speed
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 #   thingCount = 1
    dodged = 0
    gameExit = False

# Game logic

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Mouse is inactive for now until issue is resolved
            pygame.mouse.set_visible(False)

#           if event.type == pygame.MOUSEMOTION:
#                x = event.pos[0]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if dodged == 20:
                message_display("You Won")

        x += x_change

        gameDisplay.fill(white)

# things(thingx, thingy,thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width,thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

# defines crash

        if x > display_width - car_width  or x <= 0:
            crash()

# Defines box display
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

# Defines collision

        if y < thing_starty + thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)

game_intro()

game_loop()

pygame.quit
quit()