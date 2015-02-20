import pygame
import random

black = (0,0,0)
blue = (40,190,200) 
red = (255, 0, 0)
white = (255, 255, 255)
         
class Block(pygame.sprite.Sprite):
    def __init__(self, color = blue, width = 100, height = 100):
        super(Block, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("intro.wav")
        self.hspeed = 0
        self.vspeed = 0

    def set_properties(self):
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

    def change_speed(self, hspeed, vspeed):
        self.hspeed += hspeed
        self.vspeed += vspeed
         
        
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def set_image(self, filename = None):
        if(filename != None):
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()
            
    def play_sound(self):
        self.sound.play()
        
    def update(self):
        self.rect.x += self.hspeed #for x                
        self.rect.y += self.vspeed # for y
        
        if self.rect.x > window_width - 100:
            self.rect.x = window_width - 100
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > window_height - 100:
            self.rect.y = window_height - 100
        if self.rect.y < 0:
            self.rect.y = 0


class Cloud(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = 600
        self.rect.x = random.randrange(0, window_width)
        
    def set_image(self, filename = None):
        if(filename != None):
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()
            
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y -= 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y < -100:
            self.reset_pos()
   

def set_message( text ):
    global message, previous_message
    message = font.render(text, True, black)
    previous_message = message


if ( __name__ == "__main__" ):
    pygame.init()

    window_size = window_width, window_height = 800, 600 
    window = pygame.display.set_mode( window_size, pygame.RESIZABLE )
    pygame.display.set_caption("Hamster Fall")
    window.fill(blue)

    clock = pygame.time.Clock()
    frames_per_second = 60

    block_group = pygame.sprite.Group()
    player = pygame.sprite.Group()
 
    for i in range(5):
        cloud = Cloud(red, 100, 100)
        cloud.set_image("cloud.png")
        cloud.rect.x = random.randrange(0, window_width)
        cloud.rect.y = random.randrange(500, window_height+200)
        block_group.add(cloud)
    for i in range(5):
        cloud_two = Cloud(red, 100, 100)
        cloud_two.set_image("cloud.png")
        cloud_two.rect.x = random.randrange(0, window_width)
        cloud_two.rect.y = random.randrange(900, 1200)
        block_group.add(cloud_two)
    
    
    a_block = Block()
    a_block.set_image("hammy.png")
    a_block.set_position(window_width/2, 0)
    player.add(a_block)
#    block_group.add(a_block)
   
    
    font = pygame.font.SysFont("Arial", 90)
    message = previous_message = None
    set_message("")
    a_block.play_sound()

    running = True

    while (running):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
                
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    a_block.change_speed( -5, 0 )
                if (event.key == pygame.K_RIGHT):
                    a_block.change_speed( 5, 0 )
                if (event.key == pygame.K_UP):
                    a_block.change_speed( 0, -5 )
                if (event.key == pygame.K_DOWN):
                    a_block.change_speed( 0, 5 )
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT):
                    a_block.change_speed( 5, 0 )
                if (event.key == pygame.K_RIGHT):
                    a_block.change_speed( -5, 0 )
                if (event.key == pygame.K_UP):
                    a_block.change_speed( 0, 5 )
                if (event.key == pygame.K_DOWN):
                    a_block.change_speed( 0, -5 )
   
        clock.tick(frames_per_second)
        window.fill(blue)
        a_block.update()
        cloud.update()


        if(pygame.sprite.spritecollide(a_block, block_group, False)):
            window.fill(red)
            set_message("There is a collision")
        else:
            set_message("  ")
         
        window.blit(message, (window_width/2 - message.get_rect().width/2, window_height/2-100))
        player.update()
        player.draw(window)
        block_group.update()
        block_group.draw(window)
        
        pygame.display.update()

    pygame.quit()
    
