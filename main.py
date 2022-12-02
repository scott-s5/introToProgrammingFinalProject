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
pg.init()

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


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Cheese Chaser v0.1")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()

start_ticks = pg.time.get_ticks()
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    all_sprites.update()
    screen.fill(LIGHTGRAY)
#     draw_text("TIME: " + str(TIME), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    player.image.fill((player.r,player.g,player.b))
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()