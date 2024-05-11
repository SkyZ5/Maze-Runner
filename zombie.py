import pygame
import math


class Zombie:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("zombie.png").convert_alpha()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.5
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.image_mask = pygame.mask.from_surface(self.image)

    def move_direction(self, direction):
        if direction == "right":
            self.current_direction = "right"
            self.x = self.x + self.delta
        if direction == "left":
            self.current_direction = "left"
            self.x = self.x - self.delta
        if direction == "up":
            self.y = self.y + self.delta
        if direction == "down":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    
    # def move_towards_player(self, player_x, player_y):
        # Find direction vector (dx, dy) between enemy and player.
        # dx, dy = player_x - self.x, player_y - self.y
        # dist = math.hypot (dx, dy)
        # dx, dy = dx / dist, dy / dist # Normalize
        # Move along this normalized vector towards the player
        # self.rect.x += dx * self.delta
        # self.rect.y += dy * self.delta