import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Rubik's Cube")
clock = pygame.time.Clock()

test_surface = pygame.Surface((300, 100))
test_surface.fill('red')
test_font = pygame.font.Font(None, 100)

background_surface = pygame.image.load('images/background.jpg')
background_surface = pygame.transform.scale(background_surface, screen.get_size())
text_surface = test_font.render('text', True, 'Blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface,(0, 0))
    screen.blit(text_surface, (500, 200))

    pygame.display.update()
    clock.tick(60)