import pygame
import time
import random
import os

black = (0,0,0)
blue = (40,190,200)
red = (255, 0, 0)
white = (255, 255, 255)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        self.rect.y = 600
        self.rect.x = random.randrange(0, display_width)
     
    def update(self):
        self.rect.y -= 1
        if self.rect.y < 0:
            self.reset_pos()

img_path = os.path.join('C:\Python34', 'hammy.png')

class Player(object):  # represents the bird, not the game
    def __init__(self):
        self.image = pygame.image.load(img_path)
        self.x = 350
        self.y = 20

    def handle_keys(self):
        """ Handles Keys """
        
        key = pygame.key.get_pressed()
        dist = 60 
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

        if self.x > display_width - 100:
            self.x = display_width - 100
        if self.x < 0:
            self.x = 0
        if self.y > display_height - 100:
            self.y = display_height - 100
        if self.y < 0:
            self.y = 0
            
        if key[pygame.K_UP]:
            if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
                self.x = 0
            if key[pygame.K_DOWN] or key[pygame.K_UP]:
                self.y = 0
            

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
pygame.init()

black = (0,0,0)
blue = (40,190,200)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hamster Fall')
clock = pygame.time.Clock()

player = Player()
clock = pygame.time.Clock()


all_sprites_list = pygame.sprite.Group()

for i in range(10):
    # This represents the cloud
    block = Cloud(black, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(0, display_width)
    block.rect.y = random.randrange(display_height)
    
 
    # Add the block to the list of objects
    all_sprites_list.add(block)
    
for i in range(10):
    block_two = Cloud(red, 20, 15)
    block_two.rect.x = random.randrange(0, display_width)
    block_two.rect.y = random.randrange(display_height)
    all_sprites_list.add(block_two)
       
def terminate():
    pygame.quit()
    quit()

clock = pygame.time.Clock()

def game_loop():

    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            #check for the QUIT event
            if event.type == pygame.QUIT:
                gameExit = True
                terminate()

            player.handle_keys()
               
        gameDisplay.fill(blue)
        all_sprites_list.update()
     
        player.draw(gameDisplay) # draw the bird to the screen
        all_sprites_list.update()
        all_sprites_list.draw(gameDisplay)
         
        pygame.display.update()
        clock.tick(100)

game_loop()

