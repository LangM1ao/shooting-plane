def check_collision(bullets, enemies, score):
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
    return score
