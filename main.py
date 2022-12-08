''' 
overview of game

Base game: Mouse character must catch the cheese, which moves at random speeds and directions, difficulty can be set
- Can modify characters and objects they are chasing 
'''


# sources: 

#import libraries
import pygame as pg
from pygame.sprite import Sprite 
import random 
import os
from random import randint 
import time
vec = pg.math.Vector2
# build in 

# installed modules or libraries 

# created modules or libraries
from settings import * 
#global variables

#utility

#main body 


def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)


class Player(Sprite):
 def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.r = 0
        self.g = 0
        self.b = 255
        self.image.fill((self.r,self.g,self.b))
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT-45)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
 def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_w]:
             self.acc.y = -5
        if keys[pg.K_s]:
             self.acc.y = 5
        if keys[pg.K_SPACE]:
            self.jump()
def jump(self):
        hits = pg.sprite.spritecollide(self, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
def update(self):
    self.acc = vec(0,PLAYER_GRAV)
    self.controls()
    self.acc.x += self.vel.x * -0.2
    self.acc.y += self.vel.y * -0.2
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
    if self.rect.x > WIDTH:
       self.rect.x = 0
    if self.rect.y > HEIGHT:
        self.rect.y = 0
    self.rect.midbottom = self.pos

# class Cheese

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Cheese Chaser v0.1")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)


# start_ticks = pg.time.get_ticks()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()
    if player.vel.y > 0:
        hits = pg.sprite.spritecollide(player, False)
        if hits:
            # SCORE += 1
            if player.rect.bottom <= hits[0].rect.top + 5:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
    if player.vel.y < 0:
        hits = pg.sprite.spritecollide(player, False)
        if hits:
            # SCORE -= 1
            if player.rect.bottom >= hits[0].rect.top - 5:
                player.rect.top = hits[0].rect.bottom
                player.acc.y = 5
                player.vel.y = 0
    # player.image.fill((player.r,player.g,player.b))
    # all_sprites.update()
    # all_sprites.draw(screen)
    screen.fill(LIGHTGRAY)
    all_sprites.draw(screen)
    # draw_text(22, WHITE, WIDTH / 2, HEIGHT / 24)
    pg.display.flip()  
pg.quit()