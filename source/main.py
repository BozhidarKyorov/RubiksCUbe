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
button_font = pygame.font.SysFont('Helvetica', 35)

background_surface = pygame.transform.scale(pygame.image.load('images/background.jpg'), screen.get_size())
cube_image = pygame.transform.smoothscale(pygame.image.load('images/cube.png'), (600, 600))
logo_image = pygame.transform.smoothscale(pygame.image.load('images/logo.png'), (500, 191))
button_image = pygame.transform.smoothscale(pygame.image.load('images/button.png'), (300, 100))
menu_image = pygame.transform.scale(pygame.image.load('images/background2.png'), screen.get_size())
menu_surface = pygame.Surface((350, 900))
menu_surface.blit(menu_image, (0,0))


cube = cube.Cube()




def starting_screen():
    while True:
        screen.blit(background_surface,(0, 0))
        screen.blit(cube_image, (150, 150))
        screen.blit(logo_image, (900, 100))

        screen.blit(button_image, (1000, 350))
        screen.blit(button_image, (1000, 500))
        screen.blit(button_image, (1000, 650))

        screen.blit(button_font.render('Start', 1, 'black'), (1110, 375))
        screen.blit(button_font.render('Tutorial', 1, 'black'), (1095, 525))
        screen.blit(button_font.render('Close', 1, 'black'), (1110, 675))

        start_button = pygame.Rect(1015, 362, 271, 71)
        tutorial_button = pygame.Rect(1015, 512, 271, 71)
        close_button = pygame.Rect(1015, 662, 271, 71)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main()
                if tutorial_button.collidepoint(event.pos):
                    show_tutorial()
                if close_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()  


        pygame.display.update()
        clock.tick(60)

def main():
    while True:
        screen.blit(background_surface, (0, 0))
        
        left_menu_buttons = left_menu()
        right_menu()
        #screen.blit(menu_surface, (1250, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:   
                for button in buttons.rotate_side_buttons + buttons.rotate_cube_buttons:
                    if button[0].collidepoint(event.pos):
                        button[3](cube)
                
                                      
                if left_menu_buttons[0].collidepoint(event.pos):
                    starting_screen()
                if left_menu_buttons[1].collidepoint(event.pos):
                    show_tutorial()
                if left_menu_buttons[2].collidepoint(event.pos):
                    cube.shuffle()
                if left_menu_buttons[3].collidepoint(event.pos):
                    pygame.quit()
                    exit()

        

        draw_functions.color_cube(screen, cube)
        draw_functions.draw_cube_edges(screen)

        buttons.draw_buttons(screen)


        for button in buttons.rotate_side_buttons + buttons.rotate_cube_buttons:
            if button[0].collidepoint(MOUSE_POS):
                button[1](screen, button[2], 'white')


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

def left_menu():
    screen.blit(menu_surface, (0, 0))

    screen.blit(pygame.transform.smoothscale(button_image, (250, 100)), (40, 200))
    screen.blit(pygame.transform.smoothscale(button_image, (250, 100)), (40, 350))
    screen.blit(pygame.transform.smoothscale(button_image, (250, 100)), (40, 500))
    screen.blit(pygame.transform.smoothscale(button_image, (250, 100)), (40, 650))

    screen.blit(button_font.render('Back', 1, 'black'), (128, 225))
    screen.blit(button_font.render('Tutorial', 1, 'black'), (112, 375))
    screen.blit(button_font.render('Shuffle', 1, 'black'), (114, 525))
    screen.blit(button_font.render('Close', 1, 'black'), (122, 675))

    back_button = pygame.Rect((50, 210), (230, 75))
    tutorial_button = pygame.Rect((50, 360), (230, 75))
    shuffle_button = pygame.Rect((50, 510), (230, 75))
    close_button = pygame.Rect((50, 660), (230, 75))
    
    return [back_button, tutorial_button, shuffle_button, close_button]

def right_menu():
    screen.blit(menu_surface, (1250, 0))
    

    


    
def show_tutorial():
    pygame.quit()
    exit()


main()