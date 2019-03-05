import sys

import pygame


pygame.init()


window_surface = pygame.display.set_mode((400, 400), pygame.HWSURFACE)
pygame.display.set_caption('mygame')
clock = pygame.time.Clock()

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# set up the text
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
text = basicFont.render('Hello world!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = 100
text_rect.centery = 100

window_surface.fill(BLUE)

img = pygame.image.load('redfighter0004.png')
window_surface.blit(img, (200, 200))

pygame.draw.circle(window_surface, WHITE, (300, 50), 20, 0)

# draw the text onto the surface
window_surface.blit(text, text_rect)
# draw the window onto the screen
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # clock.tick(15)
