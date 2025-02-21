import pygame
import random
from settings import WIDTH, ENEMY_SPEED

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (60, 60))  # 调整敌机大小
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height  # 让敌机从屏幕上方出现

    def move(self):
        self.rect.y += ENEMY_SPEED  # 敌机向下移动

    def draw(self, screen):
        screen.blit(self.image, self.rect)
