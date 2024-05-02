import pygame
from mazewalls import Mazewalls
from mazefloor import Mazefloors
from player import Player

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("Maze Runner")

# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


r = 118
g = 59
b = 54


# render the text for later



# Instantiate the apple
mf = Mazefloors(0, -3200)
mw = Mazewalls(0, -3200)
p = Player(350, 350)

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

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False


    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))
    screen.blit(mf.image, mf.rect)
    screen.blit(mw.image, mw.rect)
    screen.blit(p.image, p.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

