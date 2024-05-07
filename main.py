import pygame
from mazewalls import Mazewalls
from mazefloor import Mazefloors
from player import Player


# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("Maze Runner")

# hides mouse
pygame.mouse.set_visible(False)

# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
light = pygame.image.load('circle.png')

r = 118
g = 59
b = 54


# render the text for later


mf = Mazefloors(0, -3200)
mw = Mazewalls(0, -3200)
p = Player(350, 350)
top = pygame.Surface((10, 10))
left = pygame.Surface((10, 10))
right = pygame.Surface((10, 10))
bottom = pygame.Surface((10, 10))
walls_mask = mw.image_mask
player_mask = p.image_mask
wmask_image = walls_mask.to_surface()
pmask_image = player_mask.to_surface()
top_mask = pygame.mask.from_surface(top)
left_mask = pygame.mask.from_surface(left)
right_mask = pygame.mask.from_surface(right)
bottom_mask = pygame.mask.from_surface(bottom)


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
        # Movement
    keys = pygame.key.get_pressed()  # checking pressed keys

    if keys[pygame.K_d]:
        mf.move_direction("right")
        mw.move_direction("right")
            
    if keys[pygame.K_a]:
        mf.move_direction("left")
        mw.move_direction("left")
            
    if keys[pygame.K_w]:
        mf.move_direction("up")
        mw.move_direction("up")
            
    if keys[pygame.K_s]:
        mf.move_direction("down")
        mw.move_direction("down")
        
    pos = (mw.x, mw.y)

    if top_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 350)) is None:
            lastPos = [mw.x, mw.y]
    if top_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 350)):
        mw.y = (lastPos[1] - 1)
        mf.y = (lastPos[1] - 1)
    if left_mask.overlap(walls_mask, (pos[0] - 350, pos[1] - 385)):
        mw.x = (lastPos[0] - 1)
        mf.x = (lastPos[0] - 1)
    if right_mask.overlap(walls_mask, (pos[0] - 420, pos[1] - 385)):
        mw.x = (lastPos[0] + 1)
        mf.x = (lastPos[0] + 1)
    if bottom_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 420)):
        mw.y = (lastPos[1] + 1)
        mf.y = (lastPos[1] + 1)

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
    screen.blit(p.image, p.rect)
    filter = pygame.surface.Surface((640, 480))
    filter.fill(pygame.color.Color('Grey'))
    filter.blit(light, map(lambda x: x - 50, pygame.mouse.get_pos()))
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()