import pygame
import button




SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Brawl 4 Monsters')


right_img = pygame.image.load('right.png').convert_alpha()
left_img = pygame.image.load('left.png').convert_alpha()


right_button = button.Button(450, 700, right_img, 0.8)
left_button = button.Button(100, 700, left_img, 0.8)


run = True
while run:

    screen.fill((202, 228, 241))

    if right_button.draw(screen):
        print('right')
    if left_button.draw(screen):
        print('left')


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()