import pygame
import random
from settings import WIDTH, HEIGHT, BLACK, WHITE, FPS
from player import Player
from bullet import Bullet
from enemy import Enemy
from utils import check_collision

def show_game_over(screen, font):
    """ 显示 Game Over 画面 """
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

    screen.fill(BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_R:
                    return True  # 返回 True，表示重新开始游戏
                if event.key == pygame.K_Q:
                    pygame.quit()
                    exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Airplane Battle")
    clock = pygame.time.Clock()

    while True:  # 添加外层循环，使得按 R 可以重启游戏
        player = Player()
        bullets = []
        enemies = []

        score = 0
        lives = 3
        font = pygame.font.Font(None, 36)

        running = True
        while running:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()
            player.move(keys)
            player.follow_mouse()

            if keys[pygame.K_SPACE]:  # 按空格键发射子弹
                bullets.append(Bullet(player.rect.centerx, player.rect.top))

            if random.randint(1, max(50 - score // 100, 10)) == 1:
                enemies.append(Enemy())

            for bullet in bullets[:]:
                bullet.move()
                bullet.draw(screen)
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            for enemy in enemies[:]:
                enemy.move()
                enemy.draw(screen)
                if enemy.rect.top > HEIGHT:
                    enemies.remove(enemy)

            score = check_collision(bullets, enemies, score)

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            for enemy in enemies[:]:
                if player.rect.colliderect(enemy.rect):
                    lives -= 1
                    enemies.remove(enemy)
                    if lives <= 0:
                        running = False  # 退出游戏循环

            lives_text = font.render(f"Lives: {lives}", True, WHITE)
            screen.blit(lives_text, (10, 40))

            player.draw(screen)
            pygame.display.update()
            clock.tick(FPS)

        # 游戏结束后，调用 Game Over 界面，等待用户按 R 重新开始
        if not show_game_over(screen, font):
            break  # 用户按 Q 退出游戏

if __name__ == "__main__":
    main()
