import pygame

pygame.init()

display_width = 400
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hamster Fall')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    pygame.display.update

pygame.quit()
quit()
