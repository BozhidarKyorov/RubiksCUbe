import cube
import pygame
import math
from helpers import get_color, a, b

def color_polygon(screen, color, corners, thickness=0):
        """
        Draws a polygon by given screen, set of corners and color. 
        Default thickness = 0 otherwise draws the outline of a polygon
        """
        pygame.draw.polygon(screen, color, corners, thickness)

def color_left_side(screen, cube: cube.Cube, rows, cols):
    """Draws the left face of the cube with no edges, coloring them with the information in cube"""
    for i in rows:
        for j in cols:
            color_polygon(screen, get_color(cube.left[i][j]),
                         ((550 + a*(j/3), 300 + b*i + b*((j)/3)),
                          (550 + a*(j/3), 300 + b*(i+1) + b*((j)/3)),
                          (550 + a*((j+1)/3), 300 + b*(i+1) + b*((j+1)/3)),
                          (550 + a*((j+1)/3), 300 + b*i + b*((j+1)/3))))
            
def color_right_side(screen, cube: cube.Cube, rows, cols):
    """Draws the right face of the cube with no edges, coloring them with the information in cube"""
    for i in rows:
        for j in cols:
            color_polygon(screen, get_color(cube.right[i][j]),
                         ((800 + a*(j/3), 400 + b*i - b*((j)/3)),
                          (800 + a*(j/3), 400 + b*(i+1) - b*((j)/3)),
                          (800 + a*((j+1)/3), 400 + b*(i+1) - b*((j+1)/3)),
                          (800 + a*((j+1)/3), 400 + b*i - b*((j+1)/3))))

def color_up_side(screen, cube: cube.Cube, rows, cols):
    """Draws the up face of the cube with no edges, coloring them with the information in cube"""
    for i in rows:
        for j in cols:
            color_polygon(screen, get_color(cube.up[i][j]),
                         ((550 + a*((i+j)/3), 300 - b*((-i+j)/3)),
                          (550 + a*((i+j+1)/3), 300 - b*((-i+j)/3) + b*(1/3)),
                          (550 + a*((i+j+2)/3), 300 - b*((-i+j)/3)),
                          (550 + a*((i+j+1)/3), 300 - b*((-i+j)/3) - b*(1/3))))

def color_cube(screen, cube):
    """Draws the the cube with no edges, coloring it with the information in cube"""
    color_left_side(screen,cube,[0,1,2], [0,1,2])
    color_right_side(screen,cube,[0,1,2], [0,1,2])
    color_up_side(screen,cube,[0,1,2], [0,1,2])


def draw_rotate_button_left(screen, cords, color = 'grey'):
    """Draws left-oriented triangle for cube rotaion button with outline"""
    color_polygon(screen, color,
                  ((cords[0] - 120, cords[1]), 
                   (cords[0] - 100, cords[1] - 40), 
                   (cords[0] - 100, cords[1] + 40)))
    
    color_polygon(screen, 'black',
                  ((cords[0] - 120, cords[1]), 
                   (cords[0] - 100, cords[1] - 40), 
                   (cords[0] - 100, cords[1] + 40)), 2)

def draw_rotate_button_right(screen, cords, color = 'grey'):
    """Draws right-oriented triangle for cube rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] + 120, cords[1]),
                   (cords[0] + 100, cords[1] + 40),
                   (cords[0] + 100, cords[1] - 40)))
    
    color_polygon(screen, 'black', 
                  ((cords[0] + 120, cords[1]),
                   (cords[0] + 100, cords[1] + 40),
                   (cords[0] + 100, cords[1] - 40)), 2)

def draw_rotate_button_down_left(screen, cords, color = 'grey'):
    """Draws down-left oriented triangle for cube rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] - (120*b)/(math.sqrt(a*a + b/b)), cords[1] + (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (100*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (100*a + 40*b)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (120*b + 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (120*b + 40*a)/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] - (120*b)/(math.sqrt(a*a + b/b)), cords[1] + (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (100*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (100*a + 40*b)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (120*b + 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (120*b + 40*a)/(math.sqrt(a*a + b/b)))), 2)

def draw_rotate_button_up_right(screen, cords, color = 'grey'):
    """Draws up-right oriented triangle for cube rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] + (120*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (120*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] - (100*a + 40*b)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (100*a - 40*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*b + 40*a)/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] + (120*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (120*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] - (100*a + 40*b)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (100*a - 40*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*b + 40*a)/(math.sqrt(a*a + b/b)))), 2)

def draw_rotate_button_up_left(screen, cords, color = 'grey'):
    """Draws up-left oriented triangle for cube rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] - (120*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (100*a - 40*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*b + 40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (120*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] - (100*a + 40*b)/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] - (120*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (100*a - 40*b)/(math.sqrt(a*a + b/b)), cords[1] - (120*b + 40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (120*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] - (100*a + 40*b)/(math.sqrt(a*a + b/b)))), 2)

def draw_rotate_button_down_right(screen, cords, color = 'grey'):
    """Draws down-right oriented triangle for cube rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] + (120*b)/(math.sqrt(a*a + b/b)), cords[1] + (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (100*b + 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (120*b + 40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (120*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (100*a + 40*b)/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] + (120*b)/(math.sqrt(a*a + b/b)), cords[1] + (120*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (100*b + 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (120*b + 40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (120*b - 40*a)/(math.sqrt(a*a + b/b)), cords[1] + (100*a + 40*b)/(math.sqrt(a*a + b/b)))), 2)


def draw_button_left(screen, cords, color = 'grey'):
    """Draws left oriented small triangle for side rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] - 40, cords[1]),
                   (cords[0] - 20, cords[1] + 20),
                   (cords[0] - 20, cords[1] - 20)))
    
    color_polygon(screen, 'black', 
                  ((cords[0] - 40, cords[1]),
                   (cords[0] - 20, cords[1] + 20),
                   (cords[0] - 20, cords[1] - 20)), 2)
    
def draw_button_right(screen, cords, color = 'grey'):
    """Draws right oriented small triangle for side rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] + 40, cords[1]),
                   (cords[0] + 20, cords[1] + 20),
                   (cords[0] + 20, cords[1] - 20)))
    
    color_polygon(screen, 'black', 
                  ((cords[0] + 40, cords[1]),
                   (cords[0] + 20, cords[1] + 20),
                   (cords[0] + 20, cords[1] - 20)), 2)

def draw_button_down_left(screen, cords, color = 'grey'):
    """Draws down-left oriented small triangle for side rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] - (40*b)/(math.sqrt(a*a + b/b)), cords[1] + (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(b - a))/(math.sqrt(a*a + b/b)), cords[1] + (20*(a + b))/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] - (20*(b - a))/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] - (40*b)/(math.sqrt(a*a + b/b)), cords[1] + (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(b - a))/(math.sqrt(a*a + b/b)), cords[1] + (20*(a + b))/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] - (20*(b - a))/(math.sqrt(a*a + b/b)))), 2)

def draw_button_up_right(screen, cords, color = 'grey'):
    """Draws up-right oriented small triangle for side rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] + (40*b)/(math.sqrt(a*a + b/b)), cords[1] - (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(b - a))/(math.sqrt(a*a + b/b)), cords[1] - (20*(a + b))/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] + (20*(b - a))/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] + (40*b)/(math.sqrt(a*a + b/b)), cords[1] - (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(b - a))/(math.sqrt(a*a + b/b)), cords[1] - (20*(a + b))/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] + (20*(b - a))/(math.sqrt(a*a + b/b)))), 2)

def draw_button_up_left(screen, cords, color = 'grey'):
    """Draws up-left oriented small triangle for side rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] - (40*b)/(math.sqrt(a*a + b/b)), cords[1] - (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] + (20*(b - a))/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(a - b))/(math.sqrt(a*a + b/b)), cords[1] - (20*(a + b))/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] - (40*b)/(math.sqrt(a*a + b/b)), cords[1] - (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] + (20*(b - a))/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(a - b))/(math.sqrt(a*a + b/b)), cords[1] - (20*(a + b))/(math.sqrt(a*a + b/b)))), 2)

def draw_button_down_right(screen, cords, color = 'grey'):
    """Draws down-right oriented small triangle for side rotaion button with outline"""
    color_polygon(screen, color, 
                  ((cords[0] + (40*b)/(math.sqrt(a*a + b/b)), cords[1] + (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] - (20*(b - a))/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(a - b))/(math.sqrt(a*a + b/b)), cords[1] + (20*(a + b))/(math.sqrt(a*a + b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] + (40*b)/(math.sqrt(a*a + b/b)), cords[1] + (40*a)/(math.sqrt(a*a + b/b))),
                   (cords[0] + (20*(a + b))/(math.sqrt(a*a + b/b)), cords[1] - (20*(b - a))/(math.sqrt(a*a + b/b))),
                   (cords[0] - (20*(a - b))/(math.sqrt(a*a + b/b)), cords[1] + (20*(a + b))/(math.sqrt(a*a + b/b)))), 2)

def draw_cube_edges(screen):
    """Draws the cube edges"""
    pygame.draw.line(screen, 'black', (800, 700), (550, 600), 3)
    pygame.draw.line(screen, 'black', (800, 700), (1050, 600), 3)

    pygame.draw.line(screen, 'black', (800, 700), (800, 400), 3)
    pygame.draw.line(screen, 'black', (1050, 600), (1050, 300), 3)
    pygame.draw.line(screen, 'black', (550, 600), (550, 300), 3)

    pygame.draw.line(screen, 'black', (800, 400), (550, 300), 3)
    pygame.draw.line(screen, 'black', (800, 400), (1050, 300), 3)

    pygame.draw.line(screen, 'black', (800, 200), (550, 300), 3)
    pygame.draw.line(screen, 'black', (800, 200), (1050, 300), 3)

    pygame.draw.line(screen, 'black', (550 + (1/3)*a, 600 + (1/3)*b), (550 + (1/3)*a, 300 + (1/3)*b), 3)
    pygame.draw.line(screen, 'black', (550 + (2/3)*a, 600 + (2/3)*b), (550 + (2/3)*a, 300 + (2/3)*b), 3)

    pygame.draw.line(screen, 'black', (800 + (2/3)*a, 600 + (1/3)*b), (800 + (2/3)*a, 300 + (1/3)*b), 3)
    pygame.draw.line(screen, 'black', (800 + (1/3)*a, 600 + (2/3)*b), (800 + (1/3)*a, 300 + (2/3)*b), 3)

    pygame.draw.line(screen, 'black', (800 + (2/3)*a, 600 + (1/3)*b), (800 + (2/3)*a, 300 + (1/3)*b), 3)
    pygame.draw.line(screen, 'black', (800 + (1/3)*a, 600 + (2/3)*b), (800 + (1/3)*a, 300 + (2/3)*b), 3)

    pygame.draw.line(screen, 'black', (800, 600), (550, 500), 3)
    pygame.draw.line(screen, 'black', (800, 500), (550, 400), 3)

    pygame.draw.line(screen, 'black', (800, 600), (1050, 500), 3)
    pygame.draw.line(screen, 'black', (800, 500), (1050, 400), 3)

    #######
    pygame.draw.line(screen, 'black', (800 + (1/3)*a, 200 + (1/3)*b), (550 + (1/3)*a, 300 + (1/3)*b), 3)
    pygame.draw.line(screen, 'black', (800 + (2/3)*a, 200 + (2/3)*b), (550 + (2/3)*a, 300 + (2/3)*b), 3)

    pygame.draw.line(screen, 'black', (550 + (2/3)*a, 200 + (1/3)*b), (800 + (2/3)*a, 300 + (1/3)*b), 3)
    pygame.draw.line(screen, 'black', (550 + (1/3)*a, 200 + (2/3)*b), (800 + (1/3)*a, 300 + (2/3)*b), 3)




