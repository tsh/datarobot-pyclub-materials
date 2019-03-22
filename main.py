import pygame
import sys
from itertools import cycle

BLACK = (0,0,0)

class MeteorBase:

    def draw (self, surface):
        surface.blit(self.img, (self.x, self.y))

    def move (self):
        self.x += 1

class MeteoritBig(MeteorBase):
    def __init__ (self):
        self.img = pygame.image.load('assets/meteor_big.png')
        self.x = 100
        self.y = 100


class MeteoritMed(MeteorBase):
    def __init__ (self):
        self.img = pygame.image.load('assets/meteor_med.png')
        self.x = 90
        self.y = 150

    def move (self):
        self.y += 1

class Ball:

    def __init__ (self):
        self.img_ball = pygame.image.load('assets/plasmaball.png')
        self.x = 200
        self.y = 100
        self.width = 128
        self.height = 128

        self.image_coordinates = []

        for row in range(4):
            x = row * self.width
            img_coord = (x, 0, self.width, self.height)
            self.image_coordinates.append(img_coord)
        print(self.image_coordinates)

    def draw(self, surface):
        surface.blit(self.img_ball, (self.x, self.y), self.image_coordinates[3])

class Player:

    STATE_LEFT = 'left'
    STATE_RIGHT = 'right'
    STATE_MAIN = 'main'

    def __init__ (self):
        img_main = pygame.image.load('assets/redfighter0004.png')
        img_left = pygame.image.load('assets/redfighter0001.png')
        img_right = pygame.image.load('assets/redfighter0009.png')
        self.img_main = pygame.transform.scale(img_main, (170, 160))
        self.img_left = pygame.transform.scale(img_left, (170, 160))
        self.img_right = pygame.transform.scale(img_right, (170, 160))
        self.x = 200
        self.y = 200
        self.state = Player.STATE_MAIN

    def draw(self, surface):
        if self.state == Player.STATE_MAIN:
            surface.blit(self.img_main, (self.x, self.y))
        elif self.state == Player.STATE_LEFT:
            surface.blit(self.img_left, (self.x, self.y))
        elif self.state == Player.STATE_RIGHT:
            surface.blit(self.img_right, (self.x, self.y))

    def move_left(self):
         self.x = self.x - 10
         self.state = Player.STATE_LEFT

    def move_right(self):
        self.x = self.x + 10
        self.state = Player.STATE_RIGHT

    def set_main(self):
        self.state = Player.STATE_MAIN

player = Player()

ball = Ball()

pygame.init()

pygame.display.set_caption('mygame')

window_surface = pygame.display.set_mode((900, 900), pygame.HWSURFACE)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('0', True, (255,255,0), BLACK)
window_surface.blit(text, (0,0))

meteors = [MeteoritMed(), MeteoritBig()]

while True:
    window_surface.fill(BLACK)
    player.draw(window_surface)
    pygame.time.Clock().tick(20)
    ball.draw(window_surface)

    for meteor in meteors:
        meteor.draw(window_surface)
        meteor.move()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_SPACE:
                for meteor in meteors:
                    if isinstance(meteor, MeteoritBig):
                        meteors.remove (meteor)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
