import pygame
from settings import BULLET_SPEED

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self):
        self.rect.y -= BULLET_SPEED  # 子弹向上移动

    def draw(self, screen):
        screen.blit(self.image, self.rect)
