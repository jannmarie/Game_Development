import pygame
import random

black = (0,0,0)
blue = (40,190,200)
red = (255, 0, 0)
white = (255, 255, 255)

class Block(pygame.sprite.Sprite):
    def __init__(self, color = blue, width = 64, height = 64):
        super(Block, self).__init__()
        self.image = pygame.Surface((width, height))
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("intro.wav")
        
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def set_image(self, filename = None):
        if(filename != None):
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()
    def play_sound(self):
        self.sound.play()
    def handle_keys(self):
                
        key = pygame.key.get_pressed()
        dist = 6 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist  # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

        if self.x > window_width - 64:
            self.x = window_width - 64
        if self.x < 0:
            self.x = 0
        if self.y > window_height - 64:
            self.y = window_height - 64
        if self.y < 0:
            self.y = 0
            
        if key[pygame.K_UP]:
            if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
                self.x = 0
            if key[pygame.K_DOWN] or key[pygame.K_UP]:
                self.y = 0
    def draw(self, surface):
            """ Draw on surface """
            # blit yourself at your current position
            surface.blit(self.image, (self.x, self.y))
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


if ( __name__ == "__main__" ):
    pygame.init()

    window_size = window_width, window_height = 640, 480
    window = pygame.display.set_mode( window_size, pygame.RESIZABLE )

    pygame.display.set_caption("Hamster Fall")
    window.fill(white)

    clock = pygame.time.Clock()
    frames_per_second = 60

    block_group = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()

    for i in range(5):
        # This represents a block
        block = Cloud(black, 50, 50)
        block.set_image("cloud.png")
     
        # Set a random location for the block
        block.rect.x = random.randrange(0, window_width)
        block.rect.y = random.randrange(window_height)
        block_list.add(block)
        
     
        # Add the block to the list of objects
        all_sprites_list.add(block)
    for i in range(5):
        block_two = Cloud(red, 50, 50)
        block_two.set_image("cloud.png")
        block_two.rect.x = random.randrange(0, window_width)
        block_two.rect.y = random.randrange(window_height)
        block_list.add(block_two)
         

    a_block = Block()
    a_block.set_image("hammy.png")
    a_block.set_position(window_width/2, window_height/2)
    a_block.play_sound()

    running = True

    while (running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
        a_block.handle_keys()
        window.fill(white)
        a_block.draw(window)
        block_list.update()
        block_list.draw(window)
        clock.tick(frames_per_second)
        pygame.display.update()

    pygame.quit()
