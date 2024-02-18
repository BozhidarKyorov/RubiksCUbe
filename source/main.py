import pygame
import draw_functions
import cube
import buttons
from helpers import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Rubik's Cube")
clock = pygame.time.Clock()

button_font = pygame.font.SysFont('Helvetica', 35)
tutorial_font = pygame.font.SysFont('Helvetica', 25)

background_surface = pygame.transform.smoothscale(pygame.image.load('images/background.jpg'), screen.get_size())
cube_image = pygame.transform.smoothscale(pygame.image.load('images/cube.png'), (600, 600))
logo_image = pygame.transform.smoothscale(pygame.image.load('images/logo.png'), (500, 191))
button_image = pygame.transform.smoothscale(pygame.image.load('images/button.png'), (300, 100))
menu_image = pygame.transform.scale(pygame.image.load('images/background2.png'), screen.get_size())
menu_surface = pygame.Surface((350, 900))
menu_surface.blit(menu_image, (0,0))
text_bubble = pygame.transform.smoothscale(pygame.image.load('images/text_bubble.png'), (230, 65))


cube = cube.Cube()

shuffled = False
turns = 0
toggle_tutorial = False
angle = 0
rotating = False




def starting_screen():
    """Starting screen event loop"""
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
                    global toggle_tutorial
                    toggle_tutorial = True
                    main()
                if close_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()  

        pygame.display.update()
        clock.tick(60)

def main():
    """Main screen event loop"""
    global shuffled, turns, toggle_tutorial
    while True:
        screen.blit(background_surface, (0, 0))
        
        left_menu_buttons = left_menu()
        right_menu()

        draw_functions.color_cube(screen, cube)
        draw_functions.draw_cube_edges(screen)

        buttons.draw_buttons(screen)

        if toggle_tutorial:
            show_tutorial()


        MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:   
                for button in buttons.rotate_side_buttons + buttons.rotate_cube_buttons:
                    if button[0].collidepoint(event.pos):
                        if pygame.mouse.get_pressed()[0]:
                            button[3](cube)
                            turns += 1
                            if turns >= 10:
                                shuffled = True
                        elif pygame.mouse.get_pressed()[2]:
                            button[3](cube)
                            button[3](cube)
                            button[3](cube)
                            turns += 1
                            if turns >= 10:
                                shuffled = True

                
                                      
                if left_menu_buttons[0].collidepoint(event.pos):
                    starting_screen()
                if left_menu_buttons[1].collidepoint(event.pos):
                    toggle_tutorial = not toggle_tutorial
                if left_menu_buttons[2].collidepoint(event.pos):
                    cube.shuffle()
                    shuffled = True
                if left_menu_buttons[3].collidepoint(event.pos):
                    pygame.quit()
                    exit()

        if cube.is_solved() and shuffled:
            victory_screen()
            shuffled = False
            turns = 0




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
    """Draws the left menu on the main screen and returns the rectangle of each button on it"""
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
    """Draws the right menu on the main screen and returns the rectangle of each button on it"""
    screen.blit(menu_surface, (1250, 0))
    
def victory_screen():
    """Victory screen"""
    while True:
        screen.blit(background_surface,(0, 0))
        left_menu_buttons = left_menu()
        right_menu()
        screen.blit(button_font.render('Back', 1, 'grey'), (128, 225))
        screen.blit(button_font.render('Tutorial', 1, 'grey'), (112, 375))
        screen.blit(button_font.render('Shuffle', 1, 'grey'), (114, 525))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if left_menu_buttons[3].collidepoint(event.pos):
                    pygame.quit()
                    exit()
                
       
        screen.blit(button_font.render('Vicotry', 1, 'black'), (800, 375))

        pygame.display.update()
        clock.tick(60)
    
    
def show_tutorial():
    """Shows tutorial """
    screen.blit(text_bubble, (1172, 435))
    screen.blit(tutorial_font.render('Rotates cube', 1, 'black'), (1232, 452))

    screen.blit(pygame.transform.flip(text_bubble, 0, 1), (1027, 190))
    screen.blit(tutorial_font.render('Rotates side', 1, 'black'), (1087, 207))

    screen.blit(pygame.transform.flip(text_bubble, 0, 1), (280, 180))
    screen.blit(tutorial_font.render('Back to start', 1, 'black'), (340, 195))

    screen.blit(pygame.transform.flip(text_bubble, 0, 1), (280, 330))
    screen.blit(tutorial_font.render('Show tutorial', 1, 'black'), (340, 345))

    screen.blit(text_bubble, (280, 540))
    screen.blit(tutorial_font.render('Shuffle cube', 1, 'black'), (340, 555))

    screen.blit(text_bubble, (280, 690))
    screen.blit(tutorial_font.render('Closes game', 1, 'black'), (340, 705))






starting_screen()