import pygame
import sys

BLACK = (0,0,0)


pygame.init()

pygame.display.set_caption('mygame')

window_surface = pygame.display.set_mode((700, 400), pygame.HWSURFACE)
window_surface.fill(BLACK)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('0', True, (255,255,0), BLACK)
window_surface.blit(text, (0,0))

img = pygame.image.load('redfighter0004.png')
img = pygame.transform.scale(img, (170, 160))
window_surface.blit(img, (200, 200))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()