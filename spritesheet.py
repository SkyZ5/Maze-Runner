import pygame


class Spritesheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, scale, colour):
        image = pygame.Surface((16, 16), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * 16), 0, 16, 16))
        image = pygame.transform.scale(image, (16 * scale, 16 * scale))
        image.set_colorkey(colour)

        return image

    def get_image_32(self, frame, scale, colour):
        image = pygame.Surface((32, 32), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * 32), 0, 32, 32))
        image = pygame.transform.scale(image, (32 * scale, 32 * scale))
        image.set_colorkey(colour)

        return image
