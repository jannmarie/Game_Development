import pygame
import time
import random

blue = (16,135,247)

class Hamster(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Hamster, self).__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.hspeed = 0
        self.vspeed = 0

    def change_speed(self, hspeed, vspeed):
        self.hspeed += hspeed
        self.vspeed += vspeed

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, imagename):
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()

#    def play_sound(self):
#        self.sound.play()

    def update(self):
        self.rect.x += self.hspeed            
        self.rect.y += self.vspeed

        if self.rect.x > screen_width - self.width:
            self.rect.x = screen_width - self.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > screen_height - self.height:
            self.rect.y = screen_height - self.height
        if self.rect.y < 0:
            self.rect.y = 0

class BadCloud(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = 600
        self.rect.x = random.randrange(0, screen_width)

    def set_image(self, imagename):
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 1
        if self.rect.y < 0 - self.height:
            self.reset_pos()

def terminate():
    pygame.quit()
    quit()

if( __name__ == "__main__" ):
    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Hamster Fall')
    icon = pygame.image.load('hammy.png')
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()
    frames_per_second = 60

    playergroup = pygame.sprite.Group()
    badcloudsgroup = pygame.sprite.Group()

    hammy = Hamster(130, 172)
    hammy.set_image("hammy.png")
    hammy.set_position(screen_width/2, 0)
    playergroup.add(hammy)

    for i in range(2):
        badcloud1 = BadCloud(100, 100)
        badcloud1.set_image("badcloud1.png")
        badcloud1.rect.x = random.randrange((50-badcloud1.width), screen_width)
        badcloud1.rect.y = screen_height
        badcloudsgroup.add(badcloud1)
    for i in range(3):
        badcloud2 = BadCloud(202, 179)
        badcloud2.set_image("badcloud2.png")
        badcloud2.rect.x = random.randrange((50-badcloud1.width), screen_width)
        badcloud2.rect.y = screen_height
        badcloudsgroup.add(badcloud2)
        

    running = True

    while (running):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
                terminate()
                    
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    hammy.change_speed( -5, 0 )
                if (event.key == pygame.K_RIGHT):
                    hammy.change_speed( 5, 0 )
                if (event.key == pygame.K_UP):
                    hammy.change_speed( 0, -5 )
                if (event.key == pygame.K_DOWN):
                    hammy.change_speed( 0, 5 )

            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT):
                    hammy.change_speed( 5, 0 )
                if (event.key == pygame.K_RIGHT):
                    hammy.change_speed( -5, 0 )
                if (event.key == pygame.K_UP):
                    hammy.change_speed( 0, 5 )
                if (event.key == pygame.K_DOWN):
                    hammy.change_speed( 0, -5 )
            

        clock.tick(frames_per_second)
        screen.fill(blue)
        hammy.update()
        badcloud1.update()
        badcloud2.update()

        if(pygame.sprite.spritecollide(hammy, badcloudsgroup, False)):
            running = False
            terminate()
        
        playergroup.update()
        playergroup.draw(screen)
        badcloudsgroup.update()
        badcloudsgroup.draw(screen)
                
        pygame.display.update()

