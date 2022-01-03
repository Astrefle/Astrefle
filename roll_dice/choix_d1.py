import random
from button import *
import pygame

pygame.init()
# base de la fenetre

run = True
v =1
pygame.display.set_caption("ROLL_THE_DICE")
screen = pygame.display.set_mode((500, 500))
carre = pygame.image.load("roll_dice/carre.png")
# image 
bg = pygame.image.load("roll_dice/bg.png")
img_d = pygame.image.load("roll_dice/choix.png")
rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
rst_hit=rst.get_rect()
rst_hit.y=510
rst_hit.x=510
#bouton
id4 = Button(55, 105, carre, 1)
id6 = Button(190, 105, carre, 1)
id8 = Button(324, 105, carre, 1)
id10 = Button(55, 258, carre, 1)
id12 = Button(190, 258, carre, 1)
id20 = Button(324, 258, carre, 1)

while run:
    
    screen.blit(bg, (0, 0))
    screen.blit(img_d, (50, 100))
    screen.blit(rst,(rst_hit.x,rst_hit.y))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    if id4.draw(screen):
        v=random.randint(1,4)
        rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
        rst_hit.y=200
        rst_hit.x=200
    elif id6.draw(screen):
         v=random.randint(1, 6)  
         rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
         rst_hit.y=200
         rst_hit.x=200 
    elif id8.draw(screen):
         v=random.randint(1, 8)  
         rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
         rst_hit.y=200
         rst_hit.x=200
    elif id10.draw(screen):
         v=random.randint(1, 10)  
         rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
         rst_hit.y=200
         rst_hit.x=200 
    elif id12.draw(screen):
         v=random.randint(1, 12)  
         rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
         rst_hit.y=200
         rst_hit.x=200 
    elif id20.draw(screen):
         v=random.randint(1,20)  
         rst=pygame.image.load(f"roll_dice/1-20/{v}.png")
         rst_hit.y=200
         rst_hit.x=200 
    