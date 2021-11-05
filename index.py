import pygame
import sys

pygame.init()
SCREEN_SIZE = (1280, 720)
FPS_LIMIT = 75
screen = pygame.display.set_mode((SCREEN_SIZE))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    pygame.display.update()
    clock.tick(FPS_LIMIT)