"""Main module with screen functions and needed parameters"""

import pygame
import draw_functions
import cube
import buttons

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
TOGGLE_TUTORIAL = False

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
                pygame.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main()
                if tutorial_button.collidepoint(event.pos):
                    global TOGGLE_TUTORIAL
                    TOGGLE_TUTORIAL = True
                    main()
                if close_button.collidepoint(event.pos):
                    pygame.quit()
                    pygame.exit()

        pygame.display.update()
        clock.tick(60)

def main():
    """Main screen event loop"""
    shuffled = False
    turns = 0    
    global TOGGLE_TUTORIAL
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background_surface, (0, 0))

        left_menu_buttons = left_menu()
        right_menu()

        draw_functions.color_cube(screen, cube)
        draw_functions.draw_cube_edges(screen)

        buttons.draw_buttons(screen)

        if TOGGLE_TUTORIAL:
            show_tutorial()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.exit()

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
                    TOGGLE_TUTORIAL = not TOGGLE_TUTORIAL
                if left_menu_buttons[2].collidepoint(event.pos):
                    cube.shuffle()
                    shuffled = True
                if left_menu_buttons[3].collidepoint(event.pos):
                    pygame.quit()
                    pygame.exit()

        if cube.is_solved() and shuffled:
            victory_screen()
            shuffled = False
            turns = 0

        for button in buttons.rotate_side_buttons + buttons.rotate_cube_buttons:
            if button[0].collidepoint(mouse_pos):
                button[1](screen, button[2], 'white')

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
                pygame.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_menu_buttons[3].collidepoint(event.pos):
                    pygame.quit()
                    pygame.exit()

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
