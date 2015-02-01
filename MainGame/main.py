import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
blue = (16,135,247)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hamster Fall')
clock = pygame.time.Clock()

HamImg = pygame.image.load('hammy.png')
hamster_width = 100
hamster_height = 100

def Hamster(x,y):
    gameDisplay.blit(HamImg,(x,y))
    
def terminate():
    pygame.quit()
    quit()

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.2)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = 600
    thing_speed = 2
    thing_width = 100
    thing_height = 100
    
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            #check for the QUIT event
            if event.type == pygame.QUIT:
                gameExit = True
                terminate()
                
            #check for the directions events when keyboard is pressed    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                    
            #check for the directions events when keyboard is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        x += x_change
        y += y_change
               
        gameDisplay.fill(blue)

        #things(thingx, thingy, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty -= thing_speed
        
        Hamster(x,y)

        if x > display_width - hamster_width:
            x = display_width - hamster_width
        if x < 0:
            x = 0
        if y > display_height - hamster_height:
            y = display_height - hamster_height
        if y < 0:
            y = 0

        if thing_starty < 0 - thing_height:
            thing_starty = 600
            thing_startx = random.randrange(0, display_width)
            
        pygame.display.update()
        clock.tick(100)

game_loop()

