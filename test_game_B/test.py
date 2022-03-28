import re
import pygame
import sys
import time
from pygame import*
from pygame.version import PygameVersion
from random import*
from lvl import *
from ennemies import*
from settings import*


while running:

    lvl_stage += 1
    screen.blit(bg, (0, 0))
    screen.blit(p1.p1, (p1.p1_hit.x, p1.p1_hit.y))
    for i in mob.l_p2:
        screen.blit(i.p2, (i.p2_hit.x, i.p2_hit.y))
    for i in mob1.l_p3:
        screen.blit(i.p3, (i.p3_hit.x, i.p3_hit.y))
    for i in mob2.l_ray:
        screen.blit(i.ray, (i.ray_hit.x, i.ray_hit.y))
    for i in mob3.l_rax:
        screen.blit(i.rax, (i.rax_hit.x, i.rax_hit.y))

    if pressed.get(pygame.K_LEFT) and p1.p1_hit.x != 20:
        p1.moove_l()
    if pressed.get(pygame.K_RIGHT) and p1.p1_hit.x != 1900:
        p1.moove_r()
    if pressed.get(pygame.K_UP) and p1.p1_hit.y != 20:
        p1.moove_u()
    if pressed.get(pygame.K_DOWN) and p1.p1_hit.y != 1060:
        p1.moove_d()
    if pressed.get(pygame.K_RETURN):
        running = False
        pygame.quit()

    if next_lvl == 0:
        essaim(lvl_stage)
        if lvl_stage > 3000:
            next_lvl += 1
            lvl_stage = 0
    if next_lvl != 0:
        rayon(lvl_stage)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            pressed[i.key] = True
        if i.type == pygame.KEYUP:
            pressed[i.key] = False

    pygame.display.flip()
