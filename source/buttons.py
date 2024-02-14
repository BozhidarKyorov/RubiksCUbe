import pygame
import draw_functions
from helpers import a, b
import math

left_buttons = [[pygame.Rect((550 - 40, 350 - 20), (20, 40)), draw_functions.draw_button_left, (550, 350)],
                    [pygame.Rect((550 - 40, 450 - 20), (20, 40)), draw_functions.draw_button_left, (550, 450)],
                    [pygame.Rect((550 - 40, 550 - 20), (20, 40)), draw_functions.draw_button_left, (550, 550)]]

right_buttons = [[pygame.Rect((1050 + 20, 350 - 20), (20, 40)), draw_functions.draw_button_right, (1050, 350)],
                    [pygame.Rect((1050 + 20, 450 - 20), (20, 40)), draw_functions.draw_button_right, (1050, 450)],
                    [pygame.Rect((1050 + 20, 550 - 20), (20, 40)), draw_functions.draw_button_right, (1050, 550)]]

up_left_buttons = [[pygame.Rect((550 + a*(1/6) - (20*a + 20*b)/(math.sqrt(a*a + b/b)), 300 - b*(1/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                    draw_functions.draw_button_up_left, (550 + a*(1/6), 300 - b*(1/6))],
                    [pygame.Rect((550 + a*(3/6) - (20*a + 20*b)/(math.sqrt(a*a + b/b)), 300 - b*(3/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                    draw_functions.draw_button_up_left, (550 + a*(3/6), 300 - b*(3/6))],
                    [pygame.Rect((550 + a*(5/6) - (20*a + 20*b)/(math.sqrt(a*a + b/b)), 300 - b*(5/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                    draw_functions.draw_button_up_left, (550 + a*(5/6), 300 - b*(5/6))]]

down_left_buttons = [[pygame.Rect((550 + a*(1/6) - (20*b + 20*a)/(math.sqrt(a*a + b/b)), 600 + b*(1/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)), 
                        draw_functions.draw_button_down_left, (550 + a*(1/6), 600 + b*(1/6))],
                        [pygame.Rect((550 + a*(3/6) - (20*b + 20*a)/(math.sqrt(a*a + b/b)), 600 + b*(3/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_left, (550 + a*(3/6), 600 + b*(3/6))],
                        [pygame.Rect((550 + a*(5/6) - (20*b + 20*a)/(math.sqrt(a*a + b/b)), 600 + b*(5/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_left, (550 + a*(5/6), 600 + b*(5/6))]]

up_right_buttons = [[pygame.Rect((800 + a*(1/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 200 + b*(1/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_up_right, (800 + a*(1/6), 200 + b*(1/6))],
                    [pygame.Rect((800 + a*(3/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 200 + b*(3/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_up_right, (800 + a*(3/6), 200 + b*(3/6))],
                    [pygame.Rect((800 + a*(5/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 200 + b*(5/6) - (40*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_up_right, (800 + a*(5/6), 200 + b*(5/6))]]

down_right_buttons = [[pygame.Rect((800 + a*(1/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 700 - b*(1/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_right, (800 + a*(1/6), 700 - b*(1/6))],
                        [pygame.Rect((800 + a*(3/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 700 - b*(3/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_right, (800 + a*(3/6), 700 - b*(3/6))],
                        [pygame.Rect((800 + a*(5/6) - (20*a - 20*b)/(math.sqrt(a*a + b/b)), 700 - b*(5/6) - (20*b - 20*a)/(math.sqrt(a*a + b/b))), (40, 30)),
                        draw_functions.draw_button_down_right, (800 + a*(5/6), 700 - b*(5/6))]]

buttons = left_buttons + right_buttons + up_left_buttons + down_left_buttons + up_right_buttons + down_right_buttons

print(buttons)
def draw_buttons(screen):
    for button in buttons:
        button[1](screen, button[2])