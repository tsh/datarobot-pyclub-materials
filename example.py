import sys
import random
import itertools

import pygame


# set up the text
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1000


class BaseMeteor:
    def __init__(self, x, y):
        self.x = x or random.randint(100, WINDOW_WIDTH  - 100)
        self.y = y or random.randint(0, 200)
        self.dx = random.randint(-3,3)
        self.dy = random.randint(-3,3)

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def update(self):
        self.x += self.dx
        self.y += self.dy


class MediumMeteor(BaseMeteor):
    def __init__(self, x=None, y=None):
        super().__init__(x, y)
        self.sprite = pygame.image.load('assets/meteor_med.png')


class BigMeteor(BaseMeteor):
    def __init__(self, x=None, y=None):
        super().__init__(x, y)
        self.sprite = pygame.image.load('assets/meteor_big.png')

    def destroy(self):
        return MediumMeteor(self.x, self.y)

class PlasmaBall:
    WIDTH = 128
    HEIGHT = 128

    def __init__(self, x, y):
        self.sprite_sheet = pygame.image.load('assets/plasmaball.png')
        self.x = x
        self.y = y
        self.speed = 2
        self.sprites = itertools.cycle(self.make_sprites())

    def make_sprites(self):
        sprites = []
        for col in range(4):
            for row in range(4):
                x = self.WIDTH * col
                y = self.HEIGHT * row
                sprites.append((x, y, self.WIDTH, self.HEIGHT))
        return sprites

    def draw(self, surface):
        coord = next(self.sprites)
        surface.blit(self.sprite_sheet, (self.x, self.y), area=coord)

    def update(self):
        self.y -= self.speed


class Player:
    STATE_NEUTRAL = 0
    STATE_TURNING_LEFT = 1
    STATE_TURNING_RIGHT = 2

    SPRITE_WIDTH = 170
    SPRITE_HEIGHT = 160

    def __init__(self):
        neutral = pygame.image.load('assets/redfighter0004.png')
        self.neutral = pygame.transform.scale(neutral, (self.SPRITE_WIDTH, self.SPRITE_HEIGHT))

        left = pygame.image.load('assets/redfighter0001.png')
        self.left = pygame.transform.scale(left, (self.SPRITE_WIDTH, self.SPRITE_HEIGHT))

        right = pygame.image.load('assets/redfighter0009.png')
        self.right = pygame.transform.scale(right, (self.SPRITE_WIDTH, self.SPRITE_HEIGHT))

        self.shoot_sound = pygame.mixer.Sound('assets/shoot.wav')

        self.state = self.STATE_NEUTRAL

        self.x = (WINDOW_WIDTH / 2) - (self.SPRITE_WIDTH / 2)
        self.y = WINDOW_HEIGHT - self.SPRITE_HEIGHT
        self.speed = 5

    def draw(self, surface):
        if self.state == self.STATE_TURNING_LEFT:
            sprite = self.left
        elif self.state == self.STATE_TURNING_RIGHT:
            sprite = self.right
        else:
            sprite = self.neutral

        surface.blit(sprite, (self.x, self.y))

    def move_left(self):
        self.state = self.STATE_TURNING_LEFT
        self.x -= self.speed

    def move_right(self):
        self.state = self.STATE_TURNING_RIGHT
        self.x += self.speed

    def set_neutral(self):
        self.state = self.STATE_NEUTRAL

    def shoot_plasma(self):
        # https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
        pygame.mixer.Sound.play(self.shoot_sound)
        return PlasmaBall(self.x, self.y)


pygame.init()


window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption('just game')

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

score = 0
player = Player()

objects = [BigMeteor(), MediumMeteor()]



while True:
    pygame.time.Clock().tick(30)
    window_surface.fill(BLUE)

    text = basicFont.render(str(score), True, WHITE, BLUE)
    window_surface.blit(text, (0,0))

    # Draw our objects
    player.draw(window_surface)
    for obj in objects:
        obj.update()
        obj.draw(window_surface)

    pygame.draw.circle(window_surface, WHITE, (300, 50), 20, 0)

    pygame.display.update()
    # https://www.pygame.org/docs/ref/key.html
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        player.set_neutral()

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pb = player.shoot_plasma()
                objects.append(pb)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

