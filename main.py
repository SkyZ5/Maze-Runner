import pygame
from mazewalls import Mazewalls
from mazefloor import Mazefloors
from player import Player

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("Maze Runner")

#hides mouse
pygame.mouse.set_visible(False)

# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
movement = True
collided = False
hit_top = False
hit_right = False
hit_left = False
hit_down = False


r = 118
g = 59
b = 54


# render the text for later



# Instantiate the apple
mf = Mazefloors(0, -3200)
mw = Mazewalls(0, -3200)
p = Player(350, 350)
walls_mask = mw.image_mask
player_mask = p.image_mask
wmask_image = walls_mask.to_surface()
pmask_image = player_mask.to_surface()


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
        # Movement
    keys = pygame.key.get_pressed()  # checking pressed keys
    if movement:
        if keys[pygame.K_d]:
            mf.move_direction("right")
            mw.move_direction("right")
            if collided:
                hit_right = True
        if keys[pygame.K_a]:
            mf.move_direction("left")
            mw.move_direction("left")
            if collided:
                hit_left = True
        if keys[pygame.K_w]:
            mf.move_direction("up")
            mw.move_direction("up")
            if collided:
                hit_top = True
        if keys[pygame.K_s]:
            mf.move_direction("down")
            mw.move_direction("down")
            if collided:
                hit_down = True
        pos = (mw.x, mw.y)
        
    
    if player_mask.overlap(walls_mask, (pos[0] - 350, pos[1] - 350)):
        print("colliding")
        collided = True
    else:
        print("not colliding")
        collided = False
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
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

