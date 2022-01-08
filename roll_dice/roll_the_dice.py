from math import fabs
import random
from pygame import event
from pygame.constants import KEYDOWN
from button import *
import pygame
pygame.init()

# base de la fenetre
run = True
v = 1
pygame.display.set_caption("ROLL_THE_DICE")
screen = pygame.display.set_mode((500, 500))

# image
bg = pygame.image.load("bg.png")
img_d = pygame.image.load("choix.png")

rst = pygame.image.load(f"1-20/{v}.png")
rst_hit = rst.get_rect()
rst_hit.y = 510
rst_hit.x = 510

stop = pygame.image.load("stop.png")
stop_hit = stop.get_rect()
stop_hit.x = 510
stop_hit.y = 510

# bouton
carre = pygame.image.load("carre.png")

id4 = Button(100, 105, carre, 1)
id6 = Button(190, 105, carre, 1)
id8 = Button(324, 105, carre, 1)
id10 = Button(100, 258, carre, 1)
id12 = Button(190, 258, carre, 1)
id20 = Button(324, 258, carre, 1)
stop_btn = Button(100, 400, stop, 1)

# base du lancé
t = True
pressed = 0

# base du programme
while run:
    screen.blit(bg, (0, 0))
    screen.blit(img_d, (50, 100))
    screen.blit(rst, (rst_hit.x, rst_hit.y))
    screen.blit(stop, (stop_hit.x, stop_hit.y))
    pygame.display.flip()

# animation du lancé
    if t == True:
        v = random.randint(1, 20)
        rst = pygame.image.load(f"1-20/{v}.png")

# choix du dé
    if id4.draw(screen):
        t = True
        rst_hit.y = 200
        rst_hit.x = 200
        stop_hit.x = 100
        stop_hit.y = 400
        pressed = 4
    elif id6.draw(screen):
        t = True
        rst_hit.y = 200
        rst_hit.x = 200
        stop_hit.x = 100
        stop_hit.y = 400
        pressed = 6
    elif id8.draw(screen):
        t = True
        rst_hit.y = 200
        rst_hit.x = 200
        stop_hit.x = 100
        stop_hit.y = 400
        pressed = 8
    elif id10.draw(screen):
        t = True
        rst_hit.y = 200
        rst_hit.x = 200
        stop_hit.x = 100
        stop_hit.y = 400
        pressed = 10
    elif id12.draw(screen):
        t = True
        rst_hit.y = 200
        rst_hit.x = 200
        stop_hit.x = 100
        stop_hit.y = 400
        pressed = 12
    elif id20.draw(screen):
        t = True
        rst_hit.y = 200
        rst_hit.x = 200
        stop_hit.x = 100
        stop_hit.y = 400
        pressed = 20

# arret du lancé
    elif stop_btn.draw(screen):
        t = False
        v = random.randint(1, pressed)
        rst = pygame.image.load(f"1-20/{v}.png")
        stop_hit.x = 510
        stop_hit.y = 510

# quitter la fenetre
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
