import pygame

pygame.init()
mainClock=pygame.time.Clock()
running = True
pygame.display.set_caption("nt")
screen = pygame.display.set_mode((760,540))
bg = pygame.image.load("bg.jpg")
pressed = {}
lvl_stage = 0
next_lvl=0