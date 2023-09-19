"""Begin license text.
Copyright 2022 'DON BOSCO INSTITUTE OF TECHNOLOGY', 'AUTOMATA RESEARCH LABORATORY'

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """

import sys
import random
import time

import pygame as pg
from pygame.locals import *
import pygame.display
from pygame import mixer

from button import Button

pg.init()
mixer.init()
mixer.music.load('bg_music.mp3')
mixer.music.play(loops=1)
mixer.music.set_volume(0.0)

# window = pg.display.set_mode((600, 388))
pg.display.set_caption("game")
bg = pg.image.load('pics1/BG.png')

screen_width = 612
screen_height = 388
SCREEN = pygame.display.set_mode((screen_width, screen_height))

d_running = [pg.image.load('pics1//NR1.png'), pg.image.load('pics1//NR2.png'), pg.image.load('pics1//NR3.png'),
             pg.image.load('pics1//NR4.png'), pg.image.load('pics1//NR0.png')]
d_jumping = pg.image.load('pics1//NR6.png')

t_running = [pg.image.load('pics1//tr1.png'), pg.image.load('pics1//tr2.png')]

t_jumping = pg.image.load('pics1//tr3.png')

stone = pg.transform.scale(pg.image.load('pics1//stone.png'), (500, 500))

box = [pg.transform.scale(pg.image.load('pics1//ob3.png'), (75, 75)),
       pg.transform.scale(pg.image.load('pics1//ob1.png'), (75, 75))]

coin = [pg.transform.scale(pg.image.load('pics1//coin.png'), (25, 25)),
        pg.transform.scale(pg.image.load('pics1//coin.png'), (25, 25))]


class Stone(object):
    img = pg.transform.scale(pg.image.load('pics1//stone.png'), (50, 50))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit_box = (x, y, width, height)

    def draw(self, win):
        self.hit_box = (self.x + 10 , self.y + 5, self.width - 30, self.height - 15)
        win.blit(self.img, (self.x, self.y))
        pg.draw.rect(win, (255, 0, 0), self.hit_box, 1)


class Shield(object):
    img = pg.transform.scale(pg.image.load('pics1//shield.png'), (70, 70))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit_box = (x, y, width, height)

    def draw(self, win):
        self.hit_box = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        win.blit(self.img, (self.x, self.y))
        pg.draw.rect(win, (255, 0, 0), self.hit_box, 1)


class Sword(object):
    img = pg.transform.scale(pg.image.load('pics1//attack.png'), (70, 70))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit_box = (x, y, width, height)

    def draw(self, win):
        self.hit_box = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        win.blit(self.img, (self.x, self.y))
        pg.draw.rect(win, (255, 0, 0), self.hit_box, 1)


class Point:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 500

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            points.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Coin(Point):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 350


class THIEF:
    x_pos = 500
    y_pos = 300
    T_JUMP_VEL = 8.5

    def __init__(self):
        self.t_run_img = t_running
        self.t_jump_img = t_jumping

        self.x = self.x_pos
        self.y = self.y_pos

        self.t_run = True
        self.t_jump = False
        self.step = 0

        self.t_jump_vel = self.T_JUMP_VEL
        self.image = self.t_run_img[0]
        self.t_rect = self.image.get_rect()
        self.t_rect.x = self.x_pos
        self.t_rect.y = self.y_pos

        self.current_health = 1000
        self.maximum_health = 1000
        self.health_bar_length = 200
        self.health_ratio = self.maximum_health / self.health_bar_length

        self.stones = []

    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount

        if self.current_health <= 0:
            self.current_health = 0

    def basic_health(self):
        pg.draw.rect(SCREEN, (255, 0, 0), (400, 10, self.current_health / self.health_ratio, 25))
        pg.draw.rect(SCREEN, (255, 255, 255), (400, 10, self.health_bar_length, 25), 4)

    def health_update(self):
        self.basic_health()

    def update(self, userInput):
        if self.t_run:
            self.run()
        if self.t_jump:
            self.jump()

        if self.step >= 10:
            self.step = 0

        if userInput[pg.K_ASTERISK] and not self.t_jump:
            self.t_jump = True
            self.t_run = False
        elif not self.t_jump:
            self.t_jump = False
            self.t_run = True

    def run(self):
        x_pos = 500
        y_pos = 300
        self.image = self.t_run_img[self.step // 5]
        self.t_rect = self.image.get_rect()
        self.t_rect.x = x_pos
        self.t_rect.y = y_pos
        self.step += 1

    def jump(self):
        self.image = self.t_jump_img
        if self.t_jump:
            self.t_rect.y -= self.t_jump_vel * 4
            self.t_jump_vel -= 0.8
        if self.t_jump_vel < -self.T_JUMP_VEL:
            self.t_jump = False
            self.t_jump_vel = self.T_JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.t_rect.x, self.t_rect.y))


player1 = THIEF()


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

            if player1.t_run:
                player1.run()
            if player1.t_jump:
                player1.jump()

            if player1.step >= 10:
                player1.step = 0

            if not player1.t_jump:
                player1.t_jump = True
                player1.t_run = False
            elif not player1.t_jump:
                player1.t_jump = False
                player1.t_run = True

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Box(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 330


class DOG:
    x_pos = 20
    y_pos = 320
    JUMP_VEL = 8.5

    def __init__(self):
        self.d_run_img = d_running
        self.d_jump_img = d_jumping

        self.dog_run = True
        self.dog_jump = False
        self.jump_vel = self.JUMP_VEL

        self.step = 0
        self.image = self.d_run_img[0]
        self.dog_rect = self.image.get_rect()
        self.dog_rect.x = self.x_pos
        self.dog_rect.y = self.y_pos

        self.current_health = 1000
        self.maximum_health = 1000
        self.health_bar_length = 200
        self.health_ratio = self.maximum_health / self.health_bar_length

    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount

        if self.current_health <= 0:
            self.current_health = 0

    def basic_health(self):
        pg.draw.rect(SCREEN, (255, 0, 0), (10, 10, self.current_health / self.health_ratio, 25))
        pg.draw.rect(SCREEN, (255, 255, 255), (10, 10, self.health_bar_length, 25), 4)

    def health_update(self):
        self.basic_health()

    def update(self, ip):

        if self.dog_run:
            self.run()

        if self.dog_jump:
            self.jump()

        if self.step >= 10:
            self.step = 0

        if ip[pg.K_SPACE] and not self.dog_jump:
            self.dog_run = False
            self.dog_jump = True

        elif not self.dog_jump:
            self.dog_jump = False
            self.dog_run = True

    def jump(self):

        self.image = self.d_jump_img
        if self.dog_jump:
            self.dog_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dog_jump = False
            self.jump_vel = self.JUMP_VEL

    def run(self):
        x_pos = 20
        y_pos = 310
        self.image = self.d_run_img[self.step // 2]
        self.dog_rect = self.image.get_rect()
        self.dog_rect.x = x_pos
        self.dog_rect.y = y_pos
        self.step += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dog_rect.x, self.dog_rect.y))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


font = get_font(20)


def show_score(x, y):
    score_text = font.render("score :" + str(score), True, (255, 255, 255))
    SCREEN.blit(score_text, (x, y))


def back():
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    PLAY_BACK = Button(image=None, pos=(500, 50), text_input="BACK", font=get_font(20), base_color="White",
                       hovering_color="Green")
    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_BACK.update(SCREEN)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if action.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                mixer.music.stop()
                import main
                main.main_menu()

    # pygame.display.update()


bg1 = pg.image.load('pics1//bg.png')
stand = pg.image.load('pics1//NR0.png')

clock = pg.time.Clock()

game_speed = 10  # background movement speed
x_pos_bg = 0
y_pos_bg = 0

obstacles = []
points = []

score = 0
score_x = 10
score_y = 40

walkCount = 0
run = True


def background():
    pg.time.delay(40)
    global x_pos_bg, y_pos_bg
    image_width = bg.get_width()
    SCREEN.blit(bg, (x_pos_bg, y_pos_bg))
    SCREEN.blit(bg, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        SCREEN.blit(bg, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= game_speed

    # attack.draw(SCREEN)
    # health.draw(SCREEN)
    # for stone in player1.stones:
    #     stone.draw_stone()
    back()


def redraw():
    for powerup in swords:
        powerup.draw(SCREEN)

    for shield in shields:
        shield.draw(SCREEN)

    for projectile in stones:
        projectile.draw(SCREEN)


def game_over_d():
    game_over_text = font.render("YOU LOSE!", True, (255, 255, 255))
    score_text = font.render(f'SCORE = {score}', True, (255, 255, 255))
    SCREEN.blit(game_over_text, (
        screen_width / 2 - (game_over_text.get_width() / 2), (screen_height / 2 - game_over_text.get_height() / 2)))
    SCREEN.blit(score_text, (
        screen_width / 2 - (score_text.get_width() / 2), (screen_height / 2 + score_text.get_height() * 1.5)))

    pg.display.update()
    time.sleep(5)
    pg.quit()


def game_over_t():
    game_over_text = font.render("YOU WIN!", True, (255, 255, 255))
    score_text = font.render(f'SCORE = {score}', True, (255, 255, 255))
    SCREEN.blit(game_over_text, (
        screen_width / 2 - (game_over_text.get_width() / 2), (screen_height / 2 - game_over_text.get_height() / 2)))
    SCREEN.blit(score_text, (
        screen_width / 2 - (score_text.get_width() / 2), (screen_height / 2 + score_text.get_height() * 1.5)))

    pg.display.update()
    time.sleep(5)
    pg.quit()


# attack = Sword(200, 150, 75, 65)
# health = Shield(300, 150, 75, 65)
swords = []
shields = []
stones = []
player = DOG()

pg.time.set_timer(USEREVENT + 1, random.randrange(700, 800))
pg.time.set_timer(USEREVENT, random.randrange(700, 800))
pg.time.set_timer(USEREVENT + 2, random.randrange(400, 600))

while run:
    clock.tick(64)  # frame rate
    redraw()

    for item in swords:
        item.x -= game_speed
        if item.x < item.width * -1:
            swords.pop(swords.index(item))

    for item in stones:
        item.x -= game_speed
        if item.x < item.width * -1:
            stones.pop(stones.index(item))

    for item in shields:
        item.x -= game_speed
        if item.x < item.width * -1:
            shields.pop(shields.index(item))

    for event in pg.event.get():
        if event.type == pg.quit:
            run = False
        if event.type == USEREVENT + 1:
            swords.append(Sword(810, 150, 75, 65))
        if event.type == USEREVENT:
            shields.append(Shield(810, 150, 75, 65))
        if event.type == USEREVENT + 2:
            stones.append(Stone(player1.x_pos, player1.y_pos, 75, 65))

    for catch in swords:
        if player.dog_rect.colliderect(catch.hit_box):
            swords.pop(swords.index(catch))
            player1.get_damage(200)

    for catch in stones:
        if player.dog_rect.colliderect(catch.hit_box):
            stones.pop(stones.index(catch))
            player.get_damage(150)

    for collect in shields:
        if player.dog_rect.colliderect(collect.hit_box):
            shields.pop(shields.index(collect))
            if player.current_health < player.maximum_health:
                player.current_health += 100
            if player.current_health > player.maximum_health:
                player.current_health = player.maximum_health

    ip = pg.key.get_pressed()

    background()
    if len(obstacles) == 0:
        if random.randint(0, 2) == 0:
            obstacles.append(Box(box))

    for obstacle in obstacles:
        obstacle.draw(SCREEN)
        obstacle.update()

        if player1.t_rect.colliderect(obstacle.rect):
            pass

        if player.dog_rect.colliderect(obstacle.rect):
            # pg.draw.rect(SCREEN, (255, 0, 0), player.dog_rect, 2)
            player.get_damage(25)

        if len(points) == 0:
            x = random.randint(0, 1)
            if x == 1:
                if random.randint(0, 1) == 0:
                    points.append(Coin(coin))

        for point in points:
            point.draw(SCREEN)
            point.update()

            if player1.t_rect.colliderect(point.rect):
                pass
                # pg.draw.rect(SCREEN, (255, 0, 0), player1.t_rect, 2)

            if player.dog_rect.colliderect(point.rect):
                pg.draw.rect(SCREEN, (255, 0, 0), player.dog_rect, 2)
                points.pop()
                score += 1
                # player.get_damage(25)

    player1.health_update()
    player.health_update()

    if player.current_health == 0:
        game_over_d()

    if player1.current_health == 0:
        game_over_t()

    show_score(score_x, score_y)

    player1.draw(SCREEN)
    player1.update(ip)
    # player1.shoot()

    player.draw(SCREEN)
    player.update(ip)

    for sword in swords:
        sword.draw(SCREEN)

    for shield in shields:
        shield.draw(SCREEN)

    for thing in stones:
        thing.draw(SCREEN)

    pg.display.update()

pg.quit()
sys.exit()
