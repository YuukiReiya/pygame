import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # ここに描画コードを追加する
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 100)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
