import pygame, random, sys
from pygame.locals import *

pygame.init()

#initializations
screen_width = 800
screen_height = 600

color = (0,255,0)
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 175, 175)

frames_per_second = 40

badcloud_minsize = 50
badcloud_maxsize = 100
badcloud_minspeed = 1
badcloud_maxspeed = 8
addnew_badcloud = 6

hamsterspeed = 5

mainClock = pygame.time.Clock()


#Pygame, Window, Mouse cursor
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hamsterfall')
pygame.mouse.set_visible(True)

#Fonts
font = pygame.font.SysFont(None, 48)

#Sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

#Images
hamsterImage = pygame.image.load('hammy.png')
hamsterRect = hamsterImage.get_rect()
badcloudsImage = pygame.image.load('cloud.png')

#Background


def terminate():
    pygame.quit()
    sys.exit()

def hamsterHasHitBadclouds(hamsterRect, cloud_group):
    for b in cloud_group:
        if hamsterRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
class startscreen():
    def __init__(self, background):
        self.image = pygame.Surface((screen_width, screen_height))
        self.image = pygame.image.load(background)
        screen.blit(self.image, (0,0))

    def button(self, image_width,image_height,x,y,image_name,image_name_over,action=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.image = pygame.Surface((image_width, image_height))

        if x + image_width > self.mouse[0] > x and y + image_height > self.mouse[1] > y:
            self.image = pygame.image.load(image_name_over)

            if self.click[0] == 1 and action !=None:
                action()
            if action == "play":
                game_loop()
            elif action == "quit":
                terminate()
        else:
            self.image = pygame.image.load(image_name)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        screen.blit(self.image, (self.rect.x, self.rect.y))

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
        
        start = startscreen('startmenu_background.png')
        play_button = start.button(96,103,700,10,'play.png','play_mouseover.png',game_loop)
        quit_button = start.button(104,103,700,450,'quit.png','quit_mouseover.png',terminate)

        mainClock.tick(frames_per_second)
        pygame.display.update()
        
def game_loop():
    topScore = 0
    while True:
        # set up the start of the game
        
        cloud_group = []
        score = 0
        hamsterRect.topleft = (screen_width / 2, 100)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        badcloudsAddCounter = 0
        pygame.mixer.music.play(-1, 0.0)

        bgOne = pygame.image.load('background_sample.png')
        bgTwo = pygame.image.load('background_sample.png')

        bgOne_y = 0
        bgTwo_y = bgOne.get_height()

        while True: # the game loop runs while the game part is playing
            score += 1 # increase score
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    if event.key == ord('z'):
                        reverseCheat = True
                    if event.key == ord('x'):
                        slowCheat = True
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP or event.key == ord('w'):
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveUp = False
                        moveDown = True

                if event.type == KEYUP:
                    if event.key == ord('z'):
                        reverseCheat = False
                        score = 0
                    if event.key == ord('x'):
                        slowCheat = False
                        score = 0
                    if event.key == K_ESCAPE:
                            terminate()

                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False

                if event.type == MOUSEMOTION:
                    # If the mouse moves, move the player where the cursor is.
                    hamsterRect.move_ip(event.pos[0] - hamsterRect.centerx, event.pos[1] - hamsterRect.centery)

            
            
            # Add new badclouds at the top of the screen, if needed.
            if not reverseCheat and not slowCheat:
                badcloudsAddCounter += 1
                
            if badcloudsAddCounter == addnew_badcloud:
                badcloudsAddCounter = 0
                badclouds_size = random.randint(badcloud_minsize, badcloud_maxsize)
                new_badclouds = {'rect': pygame.Rect(random.randint(0, screen_width-badclouds_size), screen_height, badclouds_size, badclouds_size), #left,top,width,height
                            'speed': random.randint(badcloud_minspeed, badcloud_maxspeed),
                            'surface':pygame.transform.scale(badcloudsImage, (badclouds_size, badclouds_size)),
                            }

                cloud_group.append(new_badclouds)

            # Move the hamster around.
            if moveLeft and hamsterRect.left > 0:
                hamsterRect.move_ip(-1 * hamsterspeed, 0)
            if moveRight and hamsterRect.right < screen_width:
                hamsterRect.move_ip(hamsterspeed, 0)
            if moveUp and hamsterRect.top > 0:
                hamsterRect.move_ip(0, -1 * hamsterspeed)
            if moveDown and hamsterRect.bottom < screen_height:
                hamsterRect.move_ip(0, hamsterspeed)

            # Move the mouse cursor to match the player.
       #     pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

            # Move the badclouds up.
            for b in cloud_group:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0, -5)
                elif reverseCheat:
                    b['rect'].move_ip(0, b['speed'])
                elif slowCheat:
                    b['rect'].move_ip(0, 1)

             # Delete badclouds that have fallen past the bottom.
            for b in cloud_group[:]:
                if b['rect'].top > screen_height:
                    cloud_group.remove(b)

            screen.blit(bgOne, (0, bgOne_y))
            screen.blit(bgTwo, (0, bgTwo_y))

            bgOne_y -= 2
            bgTwo_y -= 2
            
            if bgOne_y == -1 * bgOne.get_height():
                bgOne_y = bgTwo_y + bgTwo.get_height()
            if bgTwo_y == -1 * bgTwo.get_height():
                bgTwo_y = bgOne_y + bgOne.get_height()

            # Draw the score and top score.
            drawText('Score: %s' % (score), font, screen, 10, 0)
            drawText('Top Score: %s' % (topScore), font, screen, 10, 40)

            # Draw the hamster rectangle
            screen.blit(hamsterImage, hamsterRect)

            # Draw each bad cloud
            for b in cloud_group:
                screen.blit(b['surface'], b['rect'])


            pygame.display.update()
            
            # Check if any of the bad clouds have hit the hamster.
            if hamsterHasHitBadclouds(hamsterRect, cloud_group):
                if score > topScore:
                    topScore = score # set new top score
                break

            mainClock.tick(frames_per_second)
                

        # Stop the game and show the "Game Over" screen.
        pygame.mixer.music.stop()
        gameOverSound.play()

        drawText('GAME OVER', font, screen, (screen_width / 3), (screen_height / 3))
        drawText('Press a key to play again.', font, screen, (screen_width / 3) - 80, (screen_height / 3) + 50)

       

        pygame.display.update()

        gameOverSound.stop()

game_intro()
game_loop()
