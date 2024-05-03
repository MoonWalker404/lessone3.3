import pygame
import random

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/Копия zivmax13_Star_wars_in_ancient_roman_full-length_star_wars_in_an_b188cb09-7bd6-46c1-a2c7-36d11d4c5482.jpg")
pygame.display.set_icon(icon)

background_img = pygame.image.load("img/image.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed_x = random.randint(1, 5)
target_speed_y = random.randint(1, 5)

score = 0

running = True
while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.randint(1, 5)
                target_speed_y = random.randint(1, 5)



    target_x += target_speed_x
    target_y += target_speed_y

    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        target_speed_x *= -1
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        target_speed_y *= -1

    screen.blit(target_img, (target_x, target_y))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
