import pygame
import math
import time
from mazewalls import Mazewalls
from mazefloor import Mazefloors
from player import Player
from zombie import Zombie


# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("Maze Runner")

# hides mouse
# pygame.mouse.set_visible(False)

# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
light = pygame.image.load('circle.png')
filtered = False


r = 118
g = 59
b = 54


# render the text for later


mf = Mazefloors(0, -3200)
mw = Mazewalls(0, -3200)
p = Player(350, 350)
z1 = Zombie(900, 350)
z2 = Zombie(360, 370)
top = pygame.Surface((10, 10))
left = pygame.Surface((10, 10))
right = pygame.Surface((10, 10))
bottom = pygame.Surface((10, 10))
walls_mask = mw.image_mask
player_mask = p.image_mask
z1_mask = z1.image_mask
wmask_image = walls_mask.to_surface()
pmask_image = player_mask.to_surface()
z1_image = z1_mask.to_surface()
top_mask = pygame.mask.from_surface(top)
left_mask = pygame.mask.from_surface(left)
right_mask = pygame.mask.from_surface(right)
bottom_mask = pygame.mask.from_surface(bottom)
filter = pygame.surface.Surface((800, 800))
filter.fill(pygame.color.Color('Grey'))
distance_back = 50
health = 100


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
clock = pygame.time.Clock()
frame = 0

# -------- Main Program Loop -----------
while run:
    clock.tick(165)
    # Movement
    keys = pygame.key.get_pressed()  # checking pressed keys

    if keys[pygame.K_d]:
        mf.move_direction("right")
        mw.move_direction("right")
        z1.move_direction("right")
        z2.move_direction("right")
            
    if keys[pygame.K_a]:
        mf.move_direction("left")
        mw.move_direction("left")
        z1.move_direction("left")
        z2.move_direction("left")
            
    if keys[pygame.K_w]:
        mf.move_direction("up")
        mw.move_direction("up")
        z1.move_direction("up")
        z2.move_direction("up")
            
    if keys[pygame.K_s]:
        mf.move_direction("down")
        mw.move_direction("down")
        z1.move_direction("down")
        z2.move_direction("down")
    
    pos = (mw.x, mw.y)

    if top_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 350)) is None:
        lastPos = [mw.x, mw.y]
        lastPosz1 = [z1.x, z1.y]
        lastPosz2 = [z2.x, z2.y]
    if top_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 350)):
        mw.y = (lastPos[1] - 1)
        mf.y = (lastPos[1] - 1)
        z1.y = (lastPosz1[1] - 1)
        z2.y = (lastPosz2[1] - 1)
    if left_mask.overlap(walls_mask, (pos[0] - 350, pos[1] - 385)):
        mw.x = (lastPos[0] - 1)
        mf.x = (lastPos[0] - 1)
        z1.x = (lastPosz1[0] - 1)
        z2.x = (lastPosz2[0] - 1)
    if right_mask.overlap(walls_mask, (pos[0] - 420, pos[1] - 385)):
        mw.x = (lastPos[0] + 1)
        mf.x = (lastPos[0] + 1)
        z1.x = (lastPosz1[0] + 1)
        z2.x = (lastPosz2[0] + 1)
    if bottom_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 420)):
        mw.y = (lastPos[1] + 1)
        mf.y = (lastPos[1] + 1)
        z1.y = (lastPosz1[1] + 1)
        z2.y = (lastPosz2[1] + 1)
    
    # Mob Movement
    z1.move_towards_player(p)

    if z1_mask.overlap(walls_mask, (pos[0] - z1.x, pos[1] - z1.y)):
        z1.x = z1.init_x
        z1.y = z1.init_y

    if z1_mask.overlap(left_mask, (350 - z1.x, 385 - z1.y)):
        z1.x -= 100
        health -= 10
    if z1_mask.overlap(right_mask, (420 - z1.x, 385 - z1.y)):
        z1.x += 100
        health -= 10
    if z1_mask.overlap(top_mask, (385 - z1.x, 350 - z1.y)):
        z1.y -= 100
        health -= 10
    if z1_mask.overlap(bottom_mask, (385 - z1.x, 420 - z1.y)):
        z1.y += 100
        health -= 10
    
    print(health)
    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False



    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))
    screen.blit(mw.image, mw.rect)
    screen.blit(mf.image, mf.rect)
    screen.blit(z1.image, (z1.x, z1.y))
    screen.blit(z2.image, z2.rect)
    screen.blit(p.image, p.rect)
    if not filtered:
        filter.blit(light, (-100, -100))
        filtered = True
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    pygame.display.update()
    pygame.display.flip()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
