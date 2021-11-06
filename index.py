import pygame
import sys

pygame.init()
SCREEN_SIZE = (1280, 720)
FPS_LIMIT = 60
pygame.display.set_caption("Game #1")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Main Surface
screen = pygame.display.set_mode((SCREEN_SIZE))
clock = pygame.time.Clock()
testFont = pygame.font.Font("src/fonts/Pixelmania.ttf", 48)

#Extra Surfaces
testSurface = pygame.Surface((128, 128))
testSurface.fill("cyan")

imageSurface = pygame.image.load("src/player.png")

textSurface = testFont.render("MY TEXT", False, "white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    screen.blit(testSurface, (SCREEN_SIZE[0] / 2 - 64, SCREEN_SIZE[1] / 2 - 64))
    screen.blit(imageSurface, (SCREEN_SIZE[0] / 2 - 64, SCREEN_SIZE[1] / 2 - 64))
    screen.blit(textSurface, (0,0))

    pygame.display.update()
    clock.tick(FPS_LIMIT)