import pygame
import math
import time
import spritesheet
from mazewalls import Mazewalls
from mazefloor import Mazefloors
from player import Player
from zombie import Zombie
from healthbar import Healthbar


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
z2 = Zombie(600, 150)
health = 100
health_bar = Healthbar(100, 50, 300, 40, health, 100)
top = pygame.Surface((10, 10))
left = pygame.Surface((10, 10))
right = pygame.Surface((10, 10))
bottom = pygame.Surface((10, 10))
walls_mask = mw.image_mask
player_mask = p.image_mask
z1_mask = z1.image_mask
z2_mask = z2.image_mask
wmask_image = walls_mask.to_surface()
pmask_image = player_mask.to_surface()
z1_image = z1_mask.to_surface()
z2_image = z2_mask.to_surface()
top_mask = pygame.mask.from_surface(top)
left_mask = pygame.mask.from_surface(left)
right_mask = pygame.mask.from_surface(right)
bottom_mask = pygame.mask.from_surface(bottom)
filter = pygame.surface.Surface((800, 800))
filter.fill(pygame.color.Color('Grey'))
distance_back = 50

# Spritesheets
player_sheet_image = pygame.image.load("player_sheet.png").convert_alpha()
player_sheet = spritesheet.Spritesheet(player_sheet_image)

zombie_sheet_image = pygame.image.load("zombie_sheet.png").convert_alpha()
zombie_sheet = spritesheet.Spritesheet(zombie_sheet_image)

animation_list = []
zombie_list = []
animation_steps = [4, 4, 4, 4, 4]
action = 0
z1_action = 0
z2_action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0
step_counter = 0

for i in animation_steps:
    temp_list = []
    for z in range(i):
        temp_list.append(player_sheet.get_image(step_counter, 5, (255, 255, 255)))
        step_counter += 1
    animation_list.append(temp_list)

step_counter = 0

for i in animation_steps:
    temp_list = []
    for z in range(i):
        temp_list.append(zombie_sheet.get_image(step_counter, 5, (0, 0, 0)))
        step_counter += 1
    zombie_list.append(temp_list)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while run:
    clock.tick(165)
    # Movement
    keys = pygame.key.get_pressed()  # checking pressed keys

    action = 0

    if keys[pygame.K_d]:
        mf.move_direction("right")
        mw.move_direction("right")
        z1.move_direction("right")
        z2.move_direction("right")
        action = 3
        moving = True

    if keys[pygame.K_a]:
        mf.move_direction("left")
        mw.move_direction("left")
        z1.move_direction("left")
        z2.move_direction("left")
        action = 4
        moving = True

    if keys[pygame.K_w]:
        mf.move_direction("up")
        mw.move_direction("up")
        z1.move_direction("up")
        z2.move_direction("up")
        action = 2
        moving = True

    if keys[pygame.K_s]:
        mf.move_direction("down")
        mw.move_direction("down")
        z1.move_direction("down")
        z2.move_direction("down")
        action = 1
        moving = True

    pos = (mw.x, mw.y)
    lastPos = [mw.x, mw.y]
    lastPosz1 = [z1.x, z1.y]
    lastPosz2 = [z2.x, z2.y]

    if top_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 350)) is None:
        lastPos = [mw.x, mw.y]
        lastPosz1 = [z1.x, z1.y]
        lastPosz2 = [z2.x, z2.y]
    if top_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 350)):
        mw.y = (lastPos[1] - 1)
        mf.y = (lastPos[1] - 1)
        z1.y = (lastPosz1[1] - 1)
        z2.y = (lastPosz2[1] - 1)
        z1.init_y -= 1
        z2.init_y -= 1
    if left_mask.overlap(walls_mask, (pos[0] - 350, pos[1] - 385)):
        mw.x = (lastPos[0] - 1)
        mf.x = (lastPos[0] - 1)
        z1.x = (lastPosz1[0] - 1)
        z2.x = (lastPosz2[0] - 1)
        z1.init_x -= 1
        z2.init_x -= 1
    if right_mask.overlap(walls_mask, (pos[0] - 420, pos[1] - 385)):
        mw.x = (lastPos[0] + 1)
        mf.x = (lastPos[0] + 1)
        z1.x = (lastPosz1[0] + 1)
        z2.x = (lastPosz2[0] + 1)
        z1.init_x += 1
        z2.init_x += 1
    if bottom_mask.overlap(walls_mask, (pos[0] - 385, pos[1] - 420)):
        mw.y = (lastPos[1] + 1)
        mf.y = (lastPos[1] + 1)
        z1.y = (lastPosz1[1] + 1)
        z2.y = (lastPosz2[1] + 1)
        z1.init_y += 1
        z2.init_y += 1
    
    # Mob Movement
    z1_action = z1.move_towards_player(p)
    z2_action = z2.move_towards_player(p)

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

    if z2_mask.overlap(walls_mask, (pos[0] - z2.x, pos[1] - z2.y)):
        z2.x = z2.init_x
        z2.y = z2.init_y
    if z2_mask.overlap(left_mask, (350 - z2.x, 385 - z2.y)):
        z2.x -= 100
        health -= 10
    if z2_mask.overlap(right_mask, (420 - z2.x, 385 - z2.y)):
        z2.x += 100
        health -= 10
    if z2_mask.overlap(top_mask, (385 - z2.x, 350 - z2.y)):
        z2.x -= 100
        health -= 10
    if z2_mask.overlap(bottom_mask, (385 - z2.x, 420 - z2.y)):
        z2.y += 100
        health -= 10

    # --- Main event loop
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            temp_x = x - 400
            temp_y = y - 400
            if temp_x < 0 and abs(temp_x) >= abs(temp_y):
                print("left")
            elif temp_x > 0 and temp_x >= abs(temp_y):
                print("right")
            elif temp_y > 0:
                print("down")
            elif temp_y < 0:
                print("up")

    # Blit
    screen.fill((r, g, b))
    screen.blit(mw.image, mw.rect)
    screen.blit(mf.image, mf.rect)

    # Animation
    current_time = pygame.time.get_ticks()

    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(zombie_list[z1_action]):
            frame = 0
    screen.blit(zombie_list[z1_action][frame], (z1.x, z1.y))

    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(zombie_list[z2_action]):
            frame = 0
    screen.blit(zombie_list[z2_action][frame], (z2.x, z2.y))

    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
    screen.blit(animation_list[action][frame], (350, 350))

    # Lighting
    if not filtered:
        filter.blit(light, (-100, -100))
        filtered = True
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    # Health
    health_bar.hp = health
    health_bar.draw(screen)
    screen.blit(health_bar.image, health_bar.rect)

    pygame.display.update()
    pygame.display.flip()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
