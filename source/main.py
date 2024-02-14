import pygame
import math
import draw_functions
import rotate_functions
import cube
from helpers import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Rubik's Cube")
clock = pygame.time.Clock()

#test_surface = pygame.Surface((300, 100))
#test_surface.fill('red')
#test_font = pygame.font.Font(None, 100)
#text_surface = test_font.render('text', True, 'Blue')

background_surface = pygame.image.load('images/background.jpg')
background_surface = pygame.transform.scale(background_surface, screen.get_size())
menu = pygame.Surface((300,900))


    


angle = 0
a=250
b=100
cube = cube.Cube()
cube.rotate_side_up_clockwise()
cube.rotate_side_left_counterclockwise()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                pygame.quit()
                exit()

    left_buttons = [draw_functions.draw_button_left(screen,(550, 350)),
                draw_functions.draw_button_left(screen,(550, 450)),
                draw_functions.draw_button_left(screen,(550, 550))]

    right_buttons = [draw_functions.draw_button_right(screen,(1050, 350)),
                        draw_functions.draw_button_right(screen,(1050, 450)),
                        draw_functions.draw_button_right(screen,(1050, 550))]

    down_left_buttons = [draw_functions.draw_button_down_left(screen, (550+250*(1/6), 600+100*(1/6))),
                            draw_functions.draw_button_down_left(screen, (550+250*(3/6), 600+100*(3/6))),
                            draw_functions.draw_button_down_left(screen, (550+250*(5/6), 600+100*(5/6)))]

    up_right_buttons = [draw_functions.draw_button_up_right(screen, (800+250*(1/6), 200+100*(1/6))),
                        draw_functions.draw_button_up_right(screen, (800+250*(3/6), 200+100*(3/6))),
                        draw_functions.draw_button_up_right(screen, (800+250*(5/6), 200+100*(5/6)))]

    up_left_buttons = [draw_functions.draw_button_up_left(screen, (550+250*(1/6), 300-100*(1/6))),
                        draw_functions.draw_button_up_left(screen, (550+250*(3/6), 300-100*(3/6))),
                        draw_functions.draw_button_up_left(screen, (550+250*(5/6), 300-100*(5/6)))]

    down_right_buttons = [draw_functions.draw_button_down_right(screen, (800+250*(1/6), 700-100*(1/6))),
                            draw_functions.draw_button_down_right(screen, (800+250*(3/6), 700-100*(3/6))),
                            draw_functions.draw_button_down_right(screen, (800+250*(5/6), 700-100*(5/6)))]

    buttons = left_buttons + right_buttons + down_left_buttons + down_right_buttons + up_left_buttons + up_right_buttons
            
    screen.blit(background_surface,(0, 0))
    screen.blit(menu,(0,0))
    screen.blit(menu,(1300,0))
    left_buttons[0]
    
    draw_functions.color_cube(screen, cube)
    draw_functions.draw_cube_edges(screen)


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