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
collisiony=False
collisionx=False
COLLISION_DIRECTION_X = "RIGHT"
COLLISION_DIRECTION_y = "UP"


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

        if keys[pygame.K_w]:
            COLLISION_DIRECTION_Y = "UP"
        elif keys[pygame.K_s]:
            COLLISION_DIRECTION_Y = "DOWN"

        if keys[pygame.K_d]:
            COLLISION_DIRECTION_X = "RIGHT"
        elif keys[pygame.K_a]:
            COLLISION_DIRECTION_X = "LEFT"
        
    
    if player_mask.overlap(walls_mask, (pos[0] - 350, pos[1] - 350)) is None:
        print("not colliding")
        collided = True
        lastPos = [mw.x, mw.y]
        collisiony=False
        collisionx=False
    else:
        print("colliding")
        if not collisionx and collided:
            if COLLISION_DIRECTION_Y == "UP":
                collisiony = True
                mw.y = (lastPos[1]-0.5)
                mf.y = (lastPos[1]-0.5)
            elif COLLISION_DIRECTION_Y == "DOWN":
                collisiony = True
                mw.y = (lastPos[1]+0.5)
                mf.y = (lastPos[1]+0.5)

        if not collisiony and collided:
            if COLLISION_DIRECTION_X == "LEFT":
                collisionx = True
                mw.x = (lastPos[0]-0.5)
                mf.x = (lastPos[0]-0.5)
            elif COLLISION_DIRECTION_X == "RIGHT":
                collisionx = True
                mw.x = (lastPos[0]+0.5)
                mf.x = (lastPos[0]+0.5)

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

