import pygame
import draw_functions
from helpers import a, b
import math
from cube import Cube

left_buttons = [[pygame.Rect((550 - 40, 350 - 20), (20, 40)), draw_functions.draw_button_left, (550, 350), Cube.rotate_side_up_clockwise],
                    [pygame.Rect((550 - 40, 450 - 20), (20, 40)), draw_functions.draw_button_left, (550, 450), Cube.rotate_side_middle_clockwise],
                    [pygame.Rect((550 - 40, 550 - 20), (20, 40)), draw_functions.draw_button_left, (550, 550), Cube.rotate_side_down_clockwise]]

right_buttons = [[pygame.Rect((1050 + 20, 350 - 20), (20, 40)), draw_functions.draw_button_right, (1050, 350), Cube.rotate_side_up_counterclockwise],
                    [pygame.Rect((1050 + 20, 450 - 20), (20, 40)), draw_functions.draw_button_right, (1050, 450), Cube.rotate_side_middle_counterclockwise],
                    [pygame.Rect((1050 + 20, 550 - 20), (20, 40)), draw_functions.draw_button_right, (1050, 550), Cube.rotate_side_down_counterclockwise]]

up_left_buttons = [[pygame.Rect((550 + a*(1/6) - (20*a + 20*b)/(math.sqrt(a*a + b/b)), 300 - b*(1/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                    draw_functions.draw_button_up_left, (550 + a*(1/6), 300 - b*(1/6)), Cube.rotate_side_left_counterclockwise],
                    [pygame.Rect((550 + a*(3/6) - (20*a + 20*b)/(math.sqrt(a*a + b/b)), 300 - b*(3/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                    draw_functions.draw_button_up_left, (550 + a*(3/6), 300 - b*(3/6)), Cube.rotate_side_middle_right_counterclockwise],
                    [pygame.Rect((550 + a*(5/6) - (20*a + 20*b)/(math.sqrt(a*a + b/b)), 300 - b*(5/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                    draw_functions.draw_button_up_left, (550 + a*(5/6), 300 - b*(5/6)), Cube.rotate_side_back_right_counterclockwise]]

down_left_buttons = [[pygame.Rect((550 + a*(1/6) - (20*b + 20*a)/(math.sqrt(a*a + b/b)), 600 + b*(1/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)), 
                        draw_functions.draw_button_down_left, (550 + a*(1/6), 600 + b*(1/6)), Cube.rotate_side_back_left_counterclockwise],
                        [pygame.Rect((550 + a*(3/6) - (20*b + 20*a)/(math.sqrt(a*a + b/b)), 600 + b*(3/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_left, (550 + a*(3/6), 600 + b*(3/6)), Cube.rotate_side_middle_left_counterclockwise],
                        [pygame.Rect((550 + a*(5/6) - (20*b + 20*a)/(math.sqrt(a*a + b/b)), 600 + b*(5/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_left, (550 + a*(5/6), 600 + b*(5/6)), Cube.rotate_side_right_counterclockwise]]

up_right_buttons = [[pygame.Rect((800 + a*(1/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 200 + b*(1/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_up_right, (800 + a*(1/6), 200 + b*(1/6)), Cube.rotate_side_back_left_clockwise],
                    [pygame.Rect((800 + a*(3/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 200 + b*(3/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_up_right, (800 + a*(3/6), 200 + b*(3/6)), Cube.rotate_side_middle_left_clockwise],
                    [pygame.Rect((800 + a*(5/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 200 + b*(5/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_up_right, (800 + a*(5/6), 200 + b*(5/6)), Cube.rotate_side_right_clockwise]]

down_right_buttons = [[pygame.Rect((800 + a*(1/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 700 - b*(1/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_right, (800 + a*(1/6), 700 - b*(1/6)), Cube.rotate_side_left_clockwise],
                        [pygame.Rect((800 + a*(3/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 700 - b*(3/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_right, (800 + a*(3/6), 700 - b*(3/6)), Cube.rotate_side_middle_right_clockwise],
                        [pygame.Rect((800 + a*(5/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 700 - b*(5/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_right, (800 + a*(5/6), 700 - b*(5/6)), Cube.rotate_side_back_right_clockwise]]

rotate_side_buttons = left_buttons + right_buttons + up_left_buttons + down_left_buttons + up_right_buttons + down_right_buttons

def draw_buttons(screen):
    for button in rotate_side_buttons:
        button[1](screen, button[2])

    for button in rotate_cube_buttons:
        button[1](screen, button[2])

rotate_cube_buttons = [[pygame.Rect((550 - 120, 450 - 40), (20, 80)), 
                        draw_functions.draw_rotate_button_left, (550, 450), Cube.rotate_cube_right_to_left],
                       [pygame.Rect((1050 + 100, 450 - 40), (20, 80)), 
                        draw_functions.draw_rotate_button_right, (1050, 450), Cube.rotate_cube_left_to_right],
                       [pygame.Rect((550 + a*(1/2) - (120*b + 40*a)/(math.sqrt(a*a + b/b)), 600 + b*(1/2) + (120*b + 40*a)/(math.sqrt(a*a + b/b))), (88, 35)), 
                        draw_functions.draw_rotate_button_down_left, (550 + a*(1/2), 600 + b*(1/2)), Cube.rotate_cube_up_to_left],
                       [pygame.Rect((800 + a*(1/2) - (120*b - 40*a)/(math.sqrt(a*a + b/b)), 700 - b*(1/2) + (120*b + 40*a)/(math.sqrt(a*a + b/b))), (88, 35)), 
                        draw_functions.draw_rotate_button_down_right, (800 + a*(1/2), 700 - b*(1/2)), Cube.rotate_cube_up_to_right],
                       [pygame.Rect((550 + a*(1/2) - (100*a - 40*b)/(math.sqrt(a*a + b/b)), 300 - b*(1/2) - (120*a)/(math.sqrt(a*a + b/b))), (88, 35)), 
                        draw_functions.draw_rotate_button_up_left, (550 + a*(1/2), 300 - b*(1/2)), Cube.rotate_cube_right_to_up],
                       [pygame.Rect((800 + a*(1/2) - (120*b - 40*a)/(math.sqrt(a*a + b/b)), 200 + b*(1/2) - (120*a)/(math.sqrt(a*a + b/b))), (88, 35)), 
                        draw_functions.draw_rotate_button_up_right, (800 + a*(1/2), 200 + b*(1/2)), Cube.rotate_cube_left_to_up]]
