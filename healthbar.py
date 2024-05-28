import pygame


class Healthbar:

    def __init__(self, x, y, w, h, hp, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = max_hp
        self.image = pygame.image.load("health_bar.png").convert_alpha()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(58, 33, self.image_size[0], self.image_size[1])
        scale_size = (self.image_size[0] * .335, self.image_size[1] * .335)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
    
    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))
      

