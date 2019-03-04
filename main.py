import sys

import pygame


display_surf = pygame.display.set_mode((400, 444400), pygame.HWSURFACE)
pygame.display.set_caption('hello')
display_surf.fill((1, 2, 2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
