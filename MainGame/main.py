import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

hamster_width = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hamster Fall')
clock = pygame.time.Clock()

HamImg = pygame.image.load('hammy.png')

def Hamster(x,y):
    gameDisplay.blit(HamImg,(x,y))

def text_objects(text, font):
    TextSurface = font.render(text, True, black)
    return TextSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont(None, 25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    
    game_loop()

def crash():
    message_display('You Crashed')


def game_loop():
        
    x = (display_width * 0.45)
    y = (display_height * 0.01)

    x_change = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
                
        gameDisplay.fill(white)
        Hamster(x,y)

        if x > display_width - hamster_width or x < 0:
            crash()
        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
