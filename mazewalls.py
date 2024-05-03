import pygame


class Mazewalls:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("map1.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2.5
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.image = pygame.mask.from_surface(self.image)

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
