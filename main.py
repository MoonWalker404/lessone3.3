import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/Копия zivmax13_Star_wars_in_ancient_roman_full-length_star_wars_in_an_b188cb09-7bd6-46c1-a2c7-36d11d4c5482.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


running = True
while running:
    pass

pygame.quit()
