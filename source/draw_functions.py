import cube
import pygame
import math
from helpers import get_color

def color_polygon(screen, color, corners, thickness=0):
        pygame.draw.polygon(screen, color, corners, thickness)

def color_left_side(screen, cube: cube.Cube, rows, cols):
    for i in rows:
        for j in cols:
            color_polygon(screen, get_color(cube.left[i][j]),
                         ((550 + 250*(j/3), 300 + 100*i + 100*((j)/3)),
                          (550 + 250*(j/3), 300 + 100*(i+1) + 100*((j)/3)),
                          (550 + 250*((j+1)/3), 300 + 100*(i+1) + 100*((j+1)/3)),
                          (550 + 250*((j+1)/3), 300 + 100*i + 100*((j+1)/3))))
            
def color_right_side(screen, cube: cube.Cube, rows, cols):
    for i in rows:
        for j in cols:
            color_polygon(screen, get_color(cube.right[i][j]),
                         ((800 + 250*(j/3), 400 + 100*i - 100*((j)/3)),
                          (800 + 250*(j/3), 400 + 100*(i+1) - 100*((j)/3)),
                          (800 + 250*((j+1)/3), 400 + 100*(i+1) - 100*((j+1)/3)),
                          (800 + 250*((j+1)/3), 400 + 100*i - 100*((j+1)/3))))

def color_up_side(screen, cube: cube.Cube, rows, cols):
    for i in rows:
        for j in cols:
            color_polygon(screen, get_color(cube.up[i][j]),
                         ((550 + 250*((i+j)/3), 300 - 100*((-i+j)/3)),
                          (550 + 250*((i+j+1)/3), 300 - 100*((-i+j)/3) + 100*(1/3)),
                          (550 + 250*((i+j+2)/3), 300 - 100*((-i+j)/3)),
                          (550 + 250*((i+j+1)/3), 300 - 100*((-i+j)/3) - 100*(1/3))))

def color_cube(screen, cube):
    color_left_side(screen,cube,[0,1,2], [0,1,2])
    color_right_side(screen,cube,[0,1,2], [0,1,2])
    color_up_side(screen,cube,[0,1,2], [0,1,2])

def draw_button_left(screen, cords):
    color_polygon(screen, 'grey', 
                  ((cords[0] - 40, cords[1]),
                   (cords[0] - 20, cords[1] + 20),
                   (cords[0] - 20, cords[1] - 20)))
    
    color_polygon(screen, 'black', 
                  ((cords[0] - 40, cords[1]),
                   (cords[0] - 20, cords[1] + 20),
                   (cords[0] - 20, cords[1] - 20)), 2)
    
def draw_button_right(screen, cords):
    color_polygon(screen, 'grey', 
                  ((cords[0] + 40, cords[1]),
                   (cords[0] + 20, cords[1] + 20),
                   (cords[0] + 20, cords[1] - 20)))
    
    color_polygon(screen, 'black', 
                  ((cords[0] + 40, cords[1]),
                   (cords[0] + 20, cords[1] + 20),
                   (cords[0] + 20, cords[1] - 20)), 2)

def draw_button_down_left(screen, cords):
    a = 250
    b = 100
    color_polygon(screen, 'grey', 
                  ((cords[0] - (40*b)/(math.sqrt(a*a+b/b)), cords[1] + (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(b-a))/(math.sqrt(a*a+b/b)), cords[1] + (20*(a+b))/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] - (20*(b-a))/(math.sqrt(a*a+b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] - (40*b)/(math.sqrt(a*a+b/b)), cords[1] + (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(b-a))/(math.sqrt(a*a+b/b)), cords[1] + (20*(a+b))/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] - (20*(b-a))/(math.sqrt(a*a+b/b)))), 2)

def draw_button_up_right(screen, cords):
    a = 250
    b = 100
    color_polygon(screen, 'grey', 
                  ((cords[0] + (40*b)/(math.sqrt(a*a+b/b)), cords[1] - (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(b-a))/(math.sqrt(a*a+b/b)), cords[1] - (20*(a+b))/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] + (20*(b-a))/(math.sqrt(a*a+b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] + (40*b)/(math.sqrt(a*a+b/b)), cords[1] - (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(b-a))/(math.sqrt(a*a+b/b)), cords[1] - (20*(a+b))/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] + (20*(b-a))/(math.sqrt(a*a+b/b)))), 2)

def draw_button_up_left(screen, cords):
    a = 250
    b = 100
    color_polygon(screen, 'grey', 
                  ((cords[0] - (40*b)/(math.sqrt(a*a+b/b)), cords[1] - (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] + (20*(b-a))/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(a-b))/(math.sqrt(a*a+b/b)), cords[1] - (20*(a+b))/(math.sqrt(a*a+b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] - (40*b)/(math.sqrt(a*a+b/b)), cords[1] - (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] + (20*(b-a))/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(a-b))/(math.sqrt(a*a+b/b)), cords[1] - (20*(a+b))/(math.sqrt(a*a+b/b)))), 2)

def draw_button_down_right(screen, cords):
    a = 250
    b = 100
    color_polygon(screen, 'grey', 
                  ((cords[0] + (40*b)/(math.sqrt(a*a+b/b)), cords[1] + (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] - (20*(b-a))/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(a-b))/(math.sqrt(a*a+b/b)), cords[1] + (20*(a+b))/(math.sqrt(a*a+b/b)))))
    color_polygon(screen, 'black', 
                  ((cords[0] + (40*b)/(math.sqrt(a*a+b/b)), cords[1] + (40*a)/(math.sqrt(a*a+b/b))),
                   (cords[0] + (20*(a+b))/(math.sqrt(a*a+b/b)), cords[1] - (20*(b-a))/(math.sqrt(a*a+b/b))),
                   (cords[0] - (20*(a-b))/(math.sqrt(a*a+b/b)), cords[1] + (20*(a+b))/(math.sqrt(a*a+b/b)))), 2)

def draw_cube_edges(screen):
    pygame.draw.line(screen, 'black', (800, 700), (550, 600), 3)
    pygame.draw.line(screen, 'black', (800, 700), (1050, 600), 3)

    pygame.draw.line(screen, 'black', (800, 700), (800, 400), 3)
    pygame.draw.line(screen, 'black', (1050, 600), (1050, 300), 3)
    pygame.draw.line(screen, 'black', (550, 600), (550, 300), 3)

    pygame.draw.line(screen, 'black', (800, 400), (550, 300), 3)
    pygame.draw.line(screen, 'black', (800, 400), (1050, 300), 3)

    pygame.draw.line(screen, 'black', (800, 200), (550, 300), 3)
    pygame.draw.line(screen, 'black', (800, 200), (1050, 300), 3)

    pygame.draw.line(screen, 'black', (550 + (1/3)*250, 600 + (1/3)*100), (550 + (1/3)*250, 300 + (1/3)*100), 3)
    pygame.draw.line(screen, 'black', (550 + (2/3)*250, 600 + (2/3)*100), (550 + (2/3)*250, 300 + (2/3)*100), 3)

    pygame.draw.line(screen, 'black', (800 + (2/3)*250, 600 + (1/3)*100), (800 + (2/3)*250, 300 + (1/3)*100), 3)
    pygame.draw.line(screen, 'black', (800 + (1/3)*250, 600 + (2/3)*100), (800 + (1/3)*250, 300 + (2/3)*100), 3)

    pygame.draw.line(screen, 'black', (800 + (2/3)*250, 600 + (1/3)*100), (800 + (2/3)*250, 300 + (1/3)*100), 3)
    pygame.draw.line(screen, 'black', (800 + (1/3)*250, 600 + (2/3)*100), (800 + (1/3)*250, 300 + (2/3)*100), 3)

    pygame.draw.line(screen, 'black', (800, 600), (550, 500), 3)
    pygame.draw.line(screen, 'black', (800, 500), (550, 400), 3)

    pygame.draw.line(screen, 'black', (800, 600), (1050, 500), 3)
    pygame.draw.line(screen, 'black', (800, 500), (1050, 400), 3)

    #######
    pygame.draw.line(screen, 'black', (800 + (1/3)*250, 200 + (1/3)*100), (550 + (1/3)*250, 300 + (1/3)*100), 3)
    pygame.draw.line(screen, 'black', (800 + (2/3)*250, 200 + (2/3)*100), (550 + (2/3)*250, 300 + (2/3)*100), 3)

    pygame.draw.line(screen, 'black', (550 + (2/3)*250, 200 + (1/3)*100), (800 + (2/3)*250, 300 + (1/3)*100), 3)
    pygame.draw.line(screen, 'black', (550 + (1/3)*250, 200 + (2/3)*100), (800 + (1/3)*250, 300 + (2/3)*100), 3)




def draw_up(screen):
    up_hor_1(screen)
    up_hor_2(screen)
    up_hor_3(screen)
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_9(screen)
    up_hor_10(screen)
    up_hor_11(screen)
    up_hor_12(screen)
    up_ver_1(screen)
    up_ver_2(screen)
    up_ver_3(screen)
    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_9(screen)
    up_ver_10(screen)
    up_ver_11(screen)
    up_ver_12(screen)

def draw_left(screen):
    left_hor_1(screen)
    left_hor_2(screen)
    left_hor_3(screen)
    left_hor_4(screen)
    left_hor_5(screen)
    left_hor_6(screen)
    left_hor_7(screen)
    left_hor_8(screen)
    left_hor_9(screen)

def draw_right(screen):
    right_hor_1(screen)
    right_hor_2(screen)
    right_hor_3(screen)
    right_hor_4(screen)
    right_hor_5(screen)
    right_hor_6(screen)
    right_hor_7(screen)
    right_hor_8(screen)
    right_hor_9(screen)

def draw_ver(screen):
    ver_1(screen)
    ver_2(screen)
    ver_3(screen)
    ver_4(screen)
    ver_5(screen)
    ver_6(screen)
    ver_7(screen)
    ver_8(screen)
    ver_9(screen)
    ver_10(screen)
    ver_11(screen)
    ver_12(screen)
    ver_13(screen)
    ver_14(screen)
    ver_15(screen)
    ver_16(screen)
    ver_17(screen)
    ver_18(screen)
    ver_19(screen)
    ver_20(screen)
    ver_21(screen)

def up_hor_1(screen):
    pygame.draw.line(screen, 'red', (550, 300),                         (550 + 250/3, 300 - 100/3),         3)

def up_hor_2(screen):
    pygame.draw.line(screen, 'red', (550 + 250/3, 300 - 100/3),         (550 + 250*(2/3), 300 - 100*(2/3)), 3)

def up_hor_3(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300 - 100*(2/3)), (800, 200),                         3)

def up_hor_4(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 300 + 100*(1/3)), (550 + 250*(2/3), 300),             3)

def up_hor_5(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300),             (800, 300 - 100*(1/3)),             3)

def up_hor_6(screen):
    pygame.draw.line(screen, 'red', (800, 300 - 100*(1/3)),             (800+250*(1/3), 300 - 100*(2/3)),   3)

def up_hor_7(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300 + 100*(2/3)), (800, 300 + 100*(1/3)),             3)

def up_hor_8(screen):
    pygame.draw.line(screen, 'red', (800, 300 + 100*(1/3)),             (800 + 250*(1/3), 300),             3)

def up_hor_9(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 300),             (800 + 250*(2/3), 300 - 100*(1/3)), 3)

def up_hor_10(screen):
    pygame.draw.line(screen, 'red', (800, 400),                         (800 + 250*(1/3), 400 - 100*(1/3)), 3)

def up_hor_11(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 400 - 100*(1/3)), (800 + 250*(2/3), 400 - 100*(2/3)), 3)

def up_hor_12(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 400 - 100*(2/3)), (1050, 300),                        3)

def up_ver_1(screen):
    pygame.draw.line(screen, 'red', (550, 300), (550 + 250/3, 300 + 100/3), 3)

def up_ver_2(screen):
    pygame.draw.line(screen, 'red', (550 + 250/3, 300 + 100/3), (550 + 250*(2/3), 300 + 100*(2/3)),3)

def up_ver_3(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300 + 100*(2/3)), (800, 400), 3)

def up_ver_4(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 300 - 100*(1/3)), (550 + 250*(2/3), 300), 3)

def up_ver_5(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300), (800, 300 + 100*(1/3)),3)

def up_ver_6(screen):
    pygame.draw.line(screen, 'red', (800, 300 + 100*(1/3)), (800+250*(1/3), 300 + 100*(2/3)), 3)

def up_ver_7(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300 - 100*(2/3)), (800, 300 - 100*(1/3)), 3)

def up_ver_8(screen):
    pygame.draw.line(screen, 'red', (800, 300 - 100*(1/3)), (800 + 250*(1/3), 300), 3)

def up_ver_9(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 300), (800 + 250*(2/3), 300 + 100*(1/3)), 3)

def up_ver_10(screen):
    pygame.draw.line(screen, 'red', (800, 200), (800 + 250*(1/3), 200 + 100*(1/3)), 3)

def up_ver_11(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 200 + 100*(1/3)), (800 + 250*(2/3), 200 + 100*(2/3)), 3)

def up_ver_12(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 200 + 100*(2/3)), (1050, 300), 3)

#############################################################################################  
    
def left_hor_1(screen):
    pygame.draw.line(screen, 'red', (550, 400),                         (550 + 250/3, 400 + 100/3),         3)

def left_hor_2(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 400 + 100*(1/3)), (550 + 250*(2/3), 400 + 100*(2/3)), 3)

def left_hor_3(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 400 + 100*(2/3)), (800, 500),                         3)

def left_hor_4(screen):
    pygame.draw.line(screen, 'red', (550, 500),                         (550 + 250*(1/3), 500 + 100*(1/3)), 3)

def left_hor_5(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 500 + 100*(1/3)), (550 + 250*(2/3), 500 + 100*(2/3)), 3)

def left_hor_6(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 500 + 100*(2/3)),             (800, 600),             3)

def left_hor_7(screen):
    pygame.draw.line(screen, 'red', (550, 600),                         (550 + 250*(1/3), 600 + 100*(1/3)), 3)

def left_hor_8(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 600 + 100*(1/3)), (550 + 250*(2/3), 600 + 100*(2/3)), 3)

def left_hor_9(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 600 + 100*(2/3)), (800, 700),                         3)
###########################################################################################
def right_hor_1(screen):
    pygame.draw.line(screen, 'red', (800, 500),                         (800 + 250/3, 500 - 100/3),         3)

def right_hor_2(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 500 - 100*(1/3)), (800 + 250*(2/3), 500 - 100*(2/3)), 3)

def right_hor_3(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 500 - 100*(2/3)), (1050, 400),                        3)

def right_hor_4(screen):
    pygame.draw.line(screen, 'red', (800, 600),                         (800 + 250*(1/3), 600 - 100*(1/3)), 3)

def right_hor_5(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 600 - 100*(1/3)), (800 + 250*(2/3), 600 - 100*(2/3)), 3)

def right_hor_6(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 600 - 100*(2/3)), (1050, 500),                        3)

def right_hor_7(screen):
    pygame.draw.line(screen, 'red', (800, 700),                         (800 + 250*(1/3), 700 - 100*(1/3)), 3)

def right_hor_8(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 700 - 100*(1/3)), (800 + 250*(2/3), 700 - 100*(2/3)), 3)

def right_hor_9(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 700 - 100*(2/3)), (1050, 600),                        3)
########################################################################################################
def ver_1(screen):
    pygame.draw.line(screen, 'red', (550, 300), (550, 400), 3)

def ver_2(screen):
    pygame.draw.line(screen, 'red', (550, 400), (550, 500), 3)

def ver_3(screen):
    pygame.draw.line(screen, 'red', (550, 500), (550, 600), 3)

def ver_4(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 300 + 100*(1/3)), (550 + 250*(1/3), 400 + 100*(1/3)), 3)

def ver_5(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 400 + 100*(1/3)), (550 + 250*(1/3), 500 + 100*(1/3)), 3)

def ver_6(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(1/3), 500 + 100*(1/3)), (550 + 250*(1/3), 600 + 100*(1/3)), 3)

def ver_7(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 300 + 100*(2/3)), (550 + 250*(2/3), 400 + 100*(2/3)), 3)

def ver_8(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 400 + 100*(2/3)), (550 + 250*(2/3), 500 + 100*(2/3)), 3)

def ver_9(screen):
    pygame.draw.line(screen, 'red', (550 + 250*(2/3), 500 + 100*(2/3)), (550 + 250*(2/3), 600 + 100*(2/3)), 3)

def ver_10(screen):
    pygame.draw.line(screen, 'red', (800, 400), (800, 500), 3)

def ver_11(screen):
    pygame.draw.line(screen, 'red', (800, 500), (800, 600), 3)

def ver_12(screen):
    pygame.draw.line(screen, 'red', (800, 600), (800, 700), 3)

def ver_13(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 400 - 100*(1/3)), (800 + 250*(1/3), 500 - 100*(1/3)), 3)

def ver_14(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 500 - 100*(1/3)), (800 + 250*(1/3), 600 - 100*(1/3)), 3)

def ver_15(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(1/3), 600 - 100*(1/3)), (800 + 250*(1/3), 700 - 100*(1/3)), 3)

def ver_16(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 400 - 100*(2/3)), (800 + 250*(2/3), 500 - 100*(2/3)), 3)

def ver_17(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 500 - 100*(2/3)), (800 + 250*(2/3), 600 - 100*(2/3)), 3)

def ver_18(screen):
    pygame.draw.line(screen, 'red', (800 + 250*(2/3), 600 - 100*(2/3)), (800 + 250*(2/3), 700 - 100*(2/3)), 3)

def ver_19(screen):
    pygame.draw.line(screen, 'red', (1050, 300), (1050, 400), 3)

def ver_20(screen):
    pygame.draw.line(screen, 'red', (1050, 400), (1050, 500), 3)

def ver_21(screen):
    pygame.draw.line(screen, 'red', (1050, 500), (1050, 600), 3)
