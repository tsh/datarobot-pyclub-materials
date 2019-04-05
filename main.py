"""
When I see patterns in my programs, I consider it a sign of trouble. The shape of a
program should reflect only the problem it needs to solve.
--Paul Graham, Lisp hacker and venture capitalist
"""

import pygame
import sys
from itertools import cycle

BLACK = (0,0,0)

class MeteorBase:

    #def __init__(self):
        #self.rectangle = pygame.Rect(x, y, self.width, self.height)

    def draw (self, surface):
        surface.blit(self.img, (self.x, self.y))

    def move (self):
        self.x += 1

class MeteoritBig(MeteorBase):
    def __init__ (self):
        self.img = pygame.image.load('assets/meteor_big.png')
        self.rectangle = pygame.Rect(100, 100, self.img.get_width(), self.img.get_height())

    def draw (self, surface):
        surface.blit(self.img, (self.rectangle.x, self.rectangle.y))

    def move (self):
        self.rectangle.x += 1

    def is_hit(self, shot):
        return self.rectangle.colliderect(shot.rectangle)


class MeteoritMed(MeteorBase):
    def __init__ (self):
        self.img = pygame.image.load('assets/meteor_med.png')
        self.x = 90
        self.y = 150

    def move (self):
        self.y += 1


class Ball:

    IMG_BALL = pygame.image.load('assets/plasmaball.png')

    def __init__ (self, x, y):
        self.width = 128
        self.height = 128
        self.rectangle = pygame.Rect(x, y, self.width, self.height)

        self.image_coordinates = []

        for row in range(4):
            x = row * self.width
            img_coord = (x, 0, self.width, self.height)
            self.image_coordinates.append(img_coord)
        print(self.image_coordinates)

        self.cycled_coordinates = cycle(self.image_coordinates)

    def draw(self, surface):
        surface.blit(Ball.IMG_BALL, (self.rectangle.x, self.rectangle.y), next(self.cycled_coordinates))

    def move(self):
        self.rectangle.y -= 10


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
        self.x = 700
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


    def shoot(self):
        return Ball(self.x, self.y - 70)


class Enemy:

    img_main = pygame.image.load('assets/Enemy_animation/spaceship_enemy_start.png')
    img_main = pygame.transform.flip(img_main, False, True)
    img1 = pygame.image.load('assets/Enemy_animation/1.png')
    img2 = pygame.image.load('assets/Enemy_animation/2.png')
    img3 = pygame.image.load('assets/Enemy_animation/3.png')
    img4 = pygame.image.load('assets/Enemy_animation/4.png')
    img5 = pygame.image.load('assets/Enemy_animation/5.png')
    img6 = pygame.image.load('assets/Enemy_animation/6.png')
    img7 = pygame.image.load('assets/Enemy_animation/7.png')
    IMAGES = [img1, img2, img3, img4, img5, img6, img7]
    ANIMATIONS = []



    def __init__ (self):
        self.img_main = pygame.transform.scale(Enemy.img_main, (150, 140))

        self.x = 400
        self.y = 100
        self.iterable_animations = cycle(Enemy.ANIMATIONS)


    def transform_and_scale_pictures(self):
        for img in Enemy.IMAGES:
            scaled_img = pygame.transform.scale(img, (150, 140))
            flipped_img = pygame.transform.flip(scaled_img, False, True)
            Enemy.ANIMATIONS.append(flipped_img)


    def draw_animation(self, surface):
        surface.blit(next(self.iterable_animations), (self.x, self.y))

    def draw(self, surface):
        surface.blit(self.img_main, (self.x, self.y))

    def move(self):
        self.y += 4


enemy = Enemy()
enemy.transform_and_scale_pictures()

player = Player()

pygame.init()

pygame.display.set_caption('mygame')

window_surface = pygame.display.set_mode((900, 900), pygame.HWSURFACE)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('0', True, (255,255,0), BLACK)
window_surface.blit(text, (0,0))

all_game_objects = [MeteoritMed(), MeteoritBig(), enemy]

while True:
    window_surface.fill(BLACK)
    pygame.time.Clock().tick(20)
    enemy.draw_animation(window_surface)


    for obj in all_game_objects:
        obj.draw(window_surface)
        obj.move()
        if isinstance(obj, Ball):
            for space_obj in all_game_objects:
                if isinstance(space_obj, MeteoritBig):
                    if space_obj.is_hit(obj):
                        all_game_objects.remove(space_obj)

    player.draw(window_surface)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_SPACE:
                ball = player.shoot()
                all_game_objects.append(ball)



        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
