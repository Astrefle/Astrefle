import pygame
from pygame.display import flip
from pygame.version import PygameVersion
from Titre import*
from button import*
from bouton import*
pygame.init()

L = 600
H = 700

pygame.display.set_caption("Brawl 4 Monsters-Choisissez un monde")
screen = pygame.display.set_mode((L, H))

st_desert_img = pygame.image.load('assets/BG_/stage/st_desert.png')
st_desert_btn = Button(20, 100, st_desert_img, 0.8)
st_desert_img_hit = st_desert_img.get_rect()
st_desert_img_hit.y = 0
st_desert_img_hit.x = 50

st_city_img = pygame.image.load('assets/BG_/stage/st_city.png')
st_city_btn = Button(320, 100, st_city_img, 0.8)
st_city_img_hit = st_desert_img.get_rect()
st_city_img_hit.y = 300
st_city_img_hit.x = 50

st_numachi_img = pygame.image.load('assets/BG_/stage/st_numachi.png')
st_numachi_btn = Button(20, 400, st_numachi_img, 0.8)
st_numachi_img_hit = st_numachi_img.get_rect()
st_numachi_img_hit.y = 0
st_numachi_img_hit.x = 350

st_volcano_img = pygame.image.load('assets/BG_/stage/st_volcano.png')
st_volcano_btn = Button(320, 400, st_volcano_img, 0.8)
st_volcano_img_hit = st_volcano_img.get_rect()
st_volcano_img_hit.y = 300
st_volcano_img_hit.x = 350

bg_ = pygame.image.load(
    'assets/BG_/bg/thumb2-4k-sea-moon-digital-art-8-bit.png')

Titre = TITLE()

r = True

while r:
    # Fond d'ecran
    screen.blit(bg_, (0, 0))

    screen.blit(st_desert_img, (st_desert_img_hit.y, st_desert_img_hit.x))
    screen.blit(st_city_img, (st_city_img_hit.y, st_city_img_hit.x))
    screen.blit(st_numachi_img, (st_numachi_img_hit.y, st_numachi_img_hit.x))
    screen.blit(st_volcano_img, (st_volcano_img_hit.y, st_volcano_img_hit.x))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            runn = False
            pygame.quit()

    pygame.display.flip()

    if st_desert_btn.draw(screen):
        bg = pygame.image.load('assets/BG_/bg/desert.png')
        music = pygame.mixer.Sound("assets/SOUND_/desert_song.wav")
        running = True
        r = False
    elif st_city_btn.draw(screen):
        bg = pygame.image.load('assets/BG_/bg/city.png')
        music = pygame.mixer.Sound("assets/SOUND_/city_song.wav")
        running = True
        r = False

    elif st_numachi_btn.draw(screen):
        bg = pygame.image.load('assets/BG_/bg/numachi.png')
        music = pygame.mixer.Sound("assets/SOUND_/numachi_song.wav")
        running = True
        r = False

    elif st_volcano_btn.draw(screen):
        music = pygame.mixer.Sound("assets/SOUND_/volcano_song.wav")
        bg = pygame.image.load('assets/BG_/bg/volcano.png')
        running = True
        r = False
