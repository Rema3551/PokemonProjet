import pygame

class VieBarre():
    """
    dessine les barres de vie
    """
    def __init__(self, x, y, w, h, pv, pvMax):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = pv
        self.max_hp = pvMax

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))