import sys

import pygame


# set up the text
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
WIDTH = 1200
HEIGHT = 1000


class Player:
    STATE_NEUTRAL = 0
    STATE_TURNING_LEFT = 1
    STATE_TURNING_RIGHT = 2

    def __init__(self):
        neutral = pygame.image.load('redfighter0004.png')
        neutral = pygame.transform.scale(neutral, (170, 160))

        self.x = 200
        self.y = 200
        self.speed = 10
        self.sprite = neutral

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def shoot(self):
        pass


pygame.init()


window_surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption('just game')

# set up fonts
basicFont = pygame.font.SysFont(None, 48)


score = 0
player = Player()



while True:
    window_surface.fill(BLUE)

    text = basicFont.render(str(score), True, WHITE, BLUE)
    window_surface.blit(text, (0,0))

    player.draw(window_surface)

    pygame.draw.circle(window_surface, WHITE, (300, 50), 20, 0)

    pygame.display.update()
    # https://www.pygame.org/docs/ref/key.html
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

