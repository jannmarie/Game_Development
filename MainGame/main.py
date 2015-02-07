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
hamster_width = 130
hamster_height = 172

cloud = pygame.image.load('Cloud_1.png')
cloud_width = 202
cloud_height = 179 

def Hamster(x,y):
    gameDisplay.blit(HamImg,(x,y))

def Cloud(cloud_x,cloud_y):
    gameDisplay.blit(cloud, (cloud_x,cloud_y))
    
def terminate():
    pygame.quit()
    quit()

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.2)

    x_change = 0
    y_change = 0

    cloud_startx = random.randrange(0, display_width)
    cloud_starty = 600
    cloud_speed = 2
    
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

        Cloud(cloud_startx, cloud_starty)
        cloud_starty -= cloud_speed
        
        Hamster(x,y)

        if x > display_width - hamster_width:
            x = display_width - hamster_width
        if x < 0:
            x = 0
        if y > display_height - hamster_height:
            y = display_height - hamster_height
        if y < 0:
            y = 0

        if cloud_starty < 0 - cloud_height:
            cloud_starty = 600
            cloud_startx = random.randrange(0, display_width)

#Collision Detector
    #Bottom   
#-------------------------------A-----------------------------|    |-----------------------------------D-----------------------------------------------------------------|
        if x > cloud_startx and x < cloud_startx + cloud_width and y + hamster_height > cloud_starty and y + hamster_height < cloud_starty + cloud_starty + cloud_height:
            terminate()
#----------------------------------------------------------B----------------------------------|    |----------------------------------C---------------------------------------------------|
        if x + hamster_width < cloud_startx + cloud_width and x + hamster_width > cloud_startx and y + hamster_height > cloud_starty and y + hamster_height < cloud_starty + cloud_height:
            terminate()
    #Top
#-----------------------------------------A------------------------------------------------|    |-----------------------------------D------------------------------------------------|
        if cloud_startx + cloud_width > x and cloud_startx + cloud_width < x + hamster_width and cloud_starty + cloud_height > y and cloud_starty + cloud_height < y + hamster_height:
            terminate()
#-----------------------------------------B---------------------|  |-----------------------------------C------------------------------------------------|
        if cloud_startx < x + hamster_width and cloud_startx > x and cloud_starty + cloud_height > y and cloud_starty + cloud_height < x + hamster_height:
            terminate()
            
        pygame.display.update()
        clock.tick(100)

game_loop()

