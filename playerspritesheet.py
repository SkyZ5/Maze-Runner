import pygame


class Playerspritesheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, scale, colour):
        image = pygame.Surface((16, 16)).convert_alpha()
        image.blit(self.sheet(0, 0), ((frame * 16), 0, 16, 16))
        image = pygame.transform.scale(image, (16 * scale, 16 * scale))
        image.set_colorkey(colour)

        return image