''' 

Scott Smith IntroToProgrammingFinal Project

overview of game

Base game: Mouse character must catch the cheese, which moves at random speeds and directions, difficulty can be set
- Can modify characters and objects they are chasing 
'''


# sources: 
# Discussed some aspects with Mr. Cozort, in-class projects, classmate helped me import images

#import libraries
import pygame as pg
from pygame.sprite import Sprite 
import random 
import os
from random import randint 
import time
vec = pg.math.Vector2
from settings import * 

# build in 

# installed modules or libraries 
#Pygame


#utility

#asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'characters')

#main body 

#set up the ability to have text within my game
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# create the Player sprite with controls (set up to be in a 2d plane, so no 'jump' or gravity)
# create it so that every time key gets pressed, character image changes
class Player(Sprite):
 def __init__(self):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'UPMOUSE.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT-45)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
 def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5   
            self.image = pg.image.load(os.path.join(img_folder, 'LEFTMOUSE.png')).convert()
            self.image.set_colorkey(BLACK)
        if keys[pg.K_d]:
            self.acc.x = 5
            self.image = pg.image.load(os.path.join(img_folder, 'RIGHTMOUSE.png')).convert()
            self.image.set_colorkey(BLACK)
        if keys[pg.K_w]:
             self.acc.y = -5
             self.image = pg.image.load(os.path.join(img_folder, 'UPMOUSE.png')).convert()
             self.image.set_colorkey(BLACK)
        if keys[pg.K_s]:
             self.acc.y = 5
             self.image = pg.image.load(os.path.join(img_folder, 'DOWNMOUSE.png')).convert()
             self.image.set_colorkey(BLACK)
 def update(self):
    self.acc = vec(0,)
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

#  set up the 'cheese' class, aka the objective of game
class cheese(Sprite):
    def __init__(self, x, y, w, h,):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'CHEESE.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        print(self.rect.center)

#set up pygame making it ready to run, set the display and name of game 
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Cheese Chaser v0.1")
clock = pg.time.Clock()

#group sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()

#instansiate classes
player = Player()
cheese = cheese(150, 300, 100, 30)

#instances 
all_sprites.add(player)
all_sprites.add(cheese)
all_platforms.add(cheese)

#set up the parameters of game, set up the dark gray background
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()
    screen.fill(DARKGRAY)
    all_sprites.draw(screen)
    pg.display.flip()  

#close pygame
pg.quit()