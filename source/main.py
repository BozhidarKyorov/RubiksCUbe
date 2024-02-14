import pygame
import math
import draw_functions
import rotate_functions
import cube
import buttons
from helpers import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Rubik's Cube")
clock = pygame.time.Clock()

#test_surface = pygame.Surface((300, b))
#test_surface.fill('red')
#test_font = pygame.font.Font(None, b)
#text_surface = test_font.render('text', True, 'Blue')

background_surface = pygame.image.load('images/background.jpg')
background_surface = pygame.transform.scale(background_surface, screen.get_size())
menu = pygame.Surface((300,900))


    


angle = 0
a = 250
b = 100
cube = cube.Cube()
cube.rotate_side_up_clockwise()
cube.rotate_side_left_counterclockwise()

while True:
    screen.blit(background_surface,(0, 0))
    screen.blit(menu,(0,0))
    screen.blit(menu,(1300,0))

    MOUSE_POS = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons.buttons:
                if button[0].collidepoint(event.pos):
                    button[3](cube)

    

    draw_functions.color_cube(screen, cube)
    draw_functions.draw_cube_edges(screen)

    buttons.draw_buttons(screen)

    for button in buttons.buttons:
        if button[0].collidepoint(MOUSE_POS):
            button[1](screen,button[2], 'white')

    #draw_functions.draw_up(screen)
    #draw_functions.draw_left(screen)
    #draw_functions.draw_right(screen)
    #draw_functions.draw_ver(screen)
    #pygame.draw.ellipse(screen, 'white', (550,200,500,200), 3)
    #rotate_functions.rf_rotate_side_back_left_clockwise(cube, screen)

    """
    if(angle<=math.pi/2):
        x=calculate_x_ellipse(a,b,angle)
        y=calculate_y_ellipse(a,b,angle)
    elif(angle<=math.pi):
        x=-calculate_x_ellipse(a,b,angle)
        y=calculate_y_ellipse(a,b,angle)
    elif(angle<=math.pi*3/2):
        x=-calculate_x_ellipse(a,b,angle)
        y=-calculate_y_ellipse(a,b,angle)
    else:
        x=calculate_x_ellipse(a,b,angle)
        y=-calculate_y_ellipse(a,b,angle)
    pygame.draw.line(screen, 'red', (x+800,y+300),(0,200),3)
    angle += math.pi/360
    if(angle>=2*math.pi):
        angle-=2*math.pi

    """
    pygame.display.update()
    clock.tick(60)