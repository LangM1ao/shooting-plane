import pygame
from settings import WIDTH, PLAYER_SPEED

class Player:
    def __init__(self):
        self.image = pygame.image.load("your_avatar.png")
        self.image = pygame.transform.scale(self.image, (60, 60))  # 你可以调整 (宽度, 高度)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 700)  # 让玩家初始位置在屏幕底部

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

    def follow_mouse(self):
        """ 让飞机跟随鼠标 """
        mouse_x, _ = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
