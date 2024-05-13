import pygame
import math


class Zombie:

    def __init__(self, x, y):
        self.x = x
        self.y = y
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
        if direction == "left":
            self.current_direction = "left"
            self.x = self.x + self.delta
        if direction == "up":
            self.y = self.y + self.delta
        if direction == "down":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    
    def move_towards_player(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        if dist < 300:
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            self.x += dx * self.speed
            self.y += dy * self.speed
