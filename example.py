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
        x = x or random.randint(100, WINDOW_WIDTH  - 100)
        y = y or random.randint(0, 200)
        self.dx = random.randint(-3,3)
        self.dy = random.randint(-3,3)
        self.rect = pygame.Rect(x, y, self.sprite.get_width(), self.sprite.get_height())

    def draw(self, surface):
        surface.blit(self.sprite, (self.rect.x, self.rect.y))

    def update(self):
        self.rect = self.rect.move(self.dx, self.dy)

    def is_hit_by(self, projectile):
        return self.rect.colliderect(projectile.rect)


class MediumMeteor(BaseMeteor):
    def __init__(self, x=None, y=None):
        self.sprite = pygame.image.load('assets/meteor_med.png')
        super().__init__(x, y)


class BigMeteor(BaseMeteor):
    def __init__(self, x=None, y=None):
        self.sprite = pygame.image.load('assets/meteor_big.png')
        super().__init__(x, y)

    def destroy(self):
        return MediumMeteor(self.rect.x, self.rect.y)


class PlasmaBall:
    WIDTH = 128
    HEIGHT = 128
    sprite_sheet = pygame.image.load('assets/plasmaball.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.sprites = itertools.cycle(self.make_sprites())
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

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
        self.rect = self.rect.move(0, -self.speed)
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

        self.charge_rate = 1
        self.plasma_cost = 40
        self.max_charge = 70
        self.charge = 40

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

    def update(self):
        self.charge = min(self.charge + self.charge_rate, self.max_charge)

    def shoot_plasma(self):
        # https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
        if self.charge >= self.plasma_cost:
            self.charge -= self.plasma_cost
            pygame.mixer.Sound.play(self.shoot_sound)
            return PlasmaBall(self.x, self.y)


pygame.init()


window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption('just game')

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

score = 0
player = Player()

objects = [BigMeteor(), BigMeteor(), BigMeteor(), MediumMeteor(), MediumMeteor(), MediumMeteor(), BigMeteor(), BigMeteor(), BigMeteor(), MediumMeteor(), MediumMeteor(), MediumMeteor()]



while True:
    pygame.time.Clock().tick(30)
    window_surface.fill(BLUE)

    text = basicFont.render(str(score), True, WHITE, BLUE)
    window_surface.blit(text, (0,0))

    player_charge = basicFont.render(str(player.charge), True, WHITE, BLUE)
    window_surface.blit(player_charge, (0, WINDOW_HEIGHT - player_charge.get_height()))

    # check collision
    for obj in objects:
        for target in objects:
            if obj is target:
                continue
            elif isinstance(obj, PlasmaBall) and isinstance(target, BaseMeteor):
                if target.is_hit_by(obj):
                    objects.remove(target)
                    score += 1

    # Draw our objects
    player.draw(window_surface)
    for obj in objects:
        obj.update()
        obj.draw(window_surface)

    player.update()

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
                if pb:
                    objects.append(pb)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
