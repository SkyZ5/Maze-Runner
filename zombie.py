import pygame
import math


class Zombie:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.top = pygame.Surface((10, 10))
        self.left = pygame.Surface((10, 10))
        self.right = pygame.Surface((10, 10))
        self.bottom = pygame.Surface((10, 10))
        self.top_mask = pygame.mask.from_surface(self.top)
        self.left_mask = pygame.mask.from_surface(self.left)
        self.right_mask = pygame.mask.from_surface(self.right)
        self.bottom_mask = pygame.mask.from_surface(self.bottom)
        self.image = pygame.image.load("zombie.png").convert_alpha()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1
        self.speed = 0.5
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.image_mask = pygame.mask.from_surface(self.image)

    def move_direction(self, direction):
        if direction == "right":
            self.current_direction = "right"
            self.x = self.x - self.delta
            self.init_x = self.init_x - self.delta
        if direction == "left":
            self.current_direction = "left"
            self.x = self.x + self.delta
            self.init_x = self.init_x + self.delta
        if direction == "up":
            self.y = self.y + self.delta
            self.init_y = self.init_y + self.delta
        if direction == "down":
            self.y = self.y - self.delta
            self.init_y = self.init_y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    
    def move_towards_player(self, player):
        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        if dist < 300  and dist> 10:
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            self.x += dx * self.speed
            self.y += dy * self.speed

        if dist < 300 and dist > 10:
            return 0

        if dx >= 0:
            return 3
