import pygame, random, sys
from pygame.locals import *

pygame.init()

#initializations
screen_width = 800
screen_height = 600

color = (0, 0, 200)
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 175, 175)

frames_per_second = 40

badcloud_minsize = 50
badcloud_maxsize = 100
badcloud_minspeed = 1
badcloud_maxspeed = 8
addnew_badcloud = 20

hamsterspeed = 5
mainClock = pygame.time.Clock()

#globals
pause = False
highest_score = 0

#Pygame, Window, Mouse cursor
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hamsterfall')
pygame.mouse.set_visible(True)

#Fonts
font = pygame.font.SysFont(None, 48)

#Sounds
gameOverSound = pygame.mixer.Sound('sounds\\gameover.wav')
pygame.mixer.music.load('sounds\\temp_background.wav')

#Images
hamsterImage = pygame.image.load('images\\hammy.png')
hamsterRect = hamsterImage.get_rect()
badcloudsImage = pygame.image.load('images\\cloud.png')
another_badcloudsImage = pygame.image.load('images\\another_cloud.png')

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

def mainmenu():
    background = pygame.image.load('images\\startmenu_background.png')
    screen.blit(background, (0,0))

    play_button = button(65,78,705,15,'images\\play.png','images\\play_mouseover.png',game_loop)
    about_button = button(81,78,705,130,'images\\about.png', 'images\\about_mouseover.png', None)
    highestscore_button = button(75,75,705,255,'images\\highestscore.png', 'images\\highestscore_mouseover.png', None)
    settings_button = button(70,70,705,369, 'images\\settings.png', 'images\\settings_mouseover.png',None)
    quit_button = button(70,70,705,481,'images\\quit.png','images\\quit_mouseover.png',terminate)

    mainClock.tick(frames_per_second)
    pygame.display.update()
    
def button(image_width,image_height,x,y,image_name,image_name_over,action=None):
    global pause
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #check if its a menu button
    filename = image_name
    if filename == 'images\\menu.png':
        pause = True
        
    if x + image_width > mouse[0] > x and y + image_height > mouse[1] > y:
        image = pygame.image.load(image_name_over)

        if click[0] == 1 and action !=None:
            action()
        if action == "play":
            game_loop()
        elif action == "quit":
            terminate()
    else:
        image = pygame.image.load(image_name)

    screen.blit(image, (x,y))
    
def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()

def paused():
    global pause
    pygame.mouse.set_visible(True)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

        transparent = pygame.image.load('pause_transparent.png')
        screen.blit(transparent, (0,0))

        replay_button = pygame.image.load('restart.jpg')
        continue_button = pygame.image.load('replay.png')
        back_button = pygame.image.load('backtomenu.png')

        continue_x = screen_width/2 - continue_button.get_width()/2
        replay_x = continue_x - (replay_button.get_width() + 80)
        back_x = continue_x + continue_button.get_width()/2 + 80
        
        continue_button = button(50,60,continue_x,400,'replay.png','replay_mouseover.png',unpause)
        replay_button = button(50,50,replay_x,400,'restart.jpg','restart_mouseover.jpg', game_loop)
        back_button = button(50,50,back_x,400,'backtomenu.png', 'backtomenu_mouseover.png', game_intro)               
        mainClock.tick(frames_per_second)
        pygame.display.update()
        pygame.mixer.music.pause()
    
def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    intro = False

        mainmenu()         
    terminate()

def game_loop():
    global pause
    
    topScore = 0
    while True:
        
        cloud_group = []
        score = 0
        hamsterRect.topleft = (screen_width / 2, 100)
        moveLeft = moveRight = moveUp = moveDown = False

        appear_cloud = False

        badcloudsAddCounter = 0
        pygame.mixer.music.play(-1, 0.0)

        bgOne = pygame.image.load('images\\background_sample.png')
        bgTwo = pygame.image.load('images\\background_sample.png')

        bgOne_y = 0
        bgTwo_y = bgOne.get_height()

        while True:
            score += 1
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                    if event.key == K_LEFT:
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT:
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP:
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN:
                        moveUp = False
                        moveDown = True
                    if event.key == K_SPACE:
                        pause = True
                        paused()
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        moveLeft = False
                    if event.key == K_RIGHT:
                        moveRight = False
                    if event.key == K_UP:
                        moveUp = False
                    if event.key == K_DOWN:
                        moveDown = False
                if event.type == MOUSEMOTION:
                    hamsterRect.move_ip(event.pos[0] - hamsterRect.centerx, event.pos[1] - hamsterRect.centery)

            
            
            # Add new badclouds at the bottom of the screen, if needed.
            if not appear_cloud:
                badcloudsAddCounter += 1
                
            if badcloudsAddCounter == addnew_badcloud:
                badcloudsAddCounter = 0
                badclouds_size = random.randint(badcloud_minsize, badcloud_maxsize)
                
                new_badclouds = {'rect': pygame.Rect(random.randint(0, screen_width-badclouds_size), screen_height, badclouds_size, badclouds_size), #left,top,width,height
                            'speed': random.randint(badcloud_minspeed, badcloud_maxspeed),
                            'surface':pygame.transform.scale(badcloudsImage, (badclouds_size, badclouds_size)),
                            }

                cloud_group.append(new_badclouds)
                
                another_new_badclouds = {'rect': pygame.Rect(random.randint(0, screen_width-badclouds_size), screen_height, badclouds_size, badclouds_size), #left,top,width,height
                            'speed': random.randint(badcloud_minspeed, badcloud_maxspeed),
                            'surface':pygame.transform.scale(another_badcloudsImage, (badclouds_size, badclouds_size)),
                            }

                cloud_group.append(another_new_badclouds)

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
            #for b in cloud_group:
             #   if not appear_cloud:
              #      b['rect'].move_ip(0, -5)
               # elif appear_cloud:
                #    b['rect'].move_ip(0, b['speed'])
                #elif slowCheat:
                 #   b['rect'].move_ip(0, 1)

             # Delete badclouds that have fallen past the bottom.
            for b in cloud_group[:]:
                if b['rect'].top > screen_height:
                    cloud_group.remove(b)

            screen.blit(bgOne, (0, bgOne_y))
            screen.blit(bgTwo, (0, bgTwo_y))

            #Menu button/Pause
            button(119,59,0,0,'images\\menu.png','images\\menu_mouseover.png',paused)

            bgOne_y -= 2
            bgTwo_y -= 2
            
            if bgOne_y == -1 * bgOne.get_height():
                bgOne_y = bgTwo_y + bgTwo.get_height()
            if bgTwo_y == -1 * bgTwo.get_height():
                bgTwo_y = bgOne_y + bgOne.get_height()

            # Draw the score and top score.
            drawText('Score: %s' % (score), font, screen, 120, 0)
            drawText('Top Score: %s' % (topScore), font, screen, 300, 0)

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
