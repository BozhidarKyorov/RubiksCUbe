##deprecated
from draw_functions import *
import pygame
from helpers import calculate_elipse_cords, randomassformula

"""
def test_screen():
    angle = 0 
    rotating = False
    
    while True:
        if(angle >= 90):
            rotating = False
            angle = 0

        screen.blit(background_surface, (0, 0))
        screen.blit(button_font.render('TEST', 1, 'black'), (800, 100))
        
        left_menu()
        right_menu()

        test_button = pygame.draw.rect(screen, 'grey', pygame.Rect(400, 300, 100, 50))

        if rotating:
                rotate_functions.rf_rotate_side_up_clockwise(cube, screen, angle)
        else:
            draw_functions.color_cube(screen, cube)
            draw_functions.draw_cube_edges(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if test_button.collidepoint(event.pos):
                    rotating = True
                    angle = 0


        

        #draw_functions.color_cube(screen, cube)
        #draw_functions.draw_cube_edges(screen)

        

        #if angle == 90:
        #    angle += 10
        #else:
        #   angle += (1 - math.log(abs(90-angle)/90, 1.5))/2
        angle += 1
        #print(angle)
        #print(randomassformula(angle))


        #draw_functions.draw_up(screen)
        #draw_functions.draw_left(screen)
        #draw_functions.draw_right(screen)
        #draw_functions.draw_ver(screen)
        #pygame.draw.ellipse(screen, 'white', (550,200,500,200), 3)

        
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
        
        pygame.display.update()
        clock.tick(60)

"""
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
    pygame.draw.line(screen, 'red', (550, 300),                         (550 + a/3, 300 - b/3),         3)

def up_hor_2(screen):
    pygame.draw.line(screen, 'red', (550 + a/3, 300 - b/3),         (550 + a*(2/3), 300 - b*(2/3)), 3)

def up_hor_3(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300 - b*(2/3)), (800, 200),                         3)

def up_hor_4(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 300 + b*(1/3)), (550 + a*(2/3), 300),             3)

def up_hor_5(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300),             (800, 300 - b*(1/3)),             3)

def up_hor_6(screen):
    pygame.draw.line(screen, 'red', (800, 300 - b*(1/3)),             (800+a*(1/3), 300 - b*(2/3)),   3)

def up_hor_7(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300 + b*(2/3)), (800, 300 + b*(1/3)),             3)

def up_hor_8(screen):
    pygame.draw.line(screen, 'red', (800, 300 + b*(1/3)),             (800 + a*(1/3), 300),             3)

def up_hor_9(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 300),             (800 + a*(2/3), 300 - b*(1/3)), 3)

def up_hor_10(screen):
    pygame.draw.line(screen, 'red', (800, 400),                         (800 + a*(1/3), 400 - b*(1/3)), 3)

def up_hor_11(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 400 - b*(1/3)), (800 + a*(2/3), 400 - b*(2/3)), 3)

def up_hor_12(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 400 - b*(2/3)), (1050, 300),                        3)

def up_ver_1(screen):
    pygame.draw.line(screen, 'red', (550, 300), (550 + a/3, 300 + b/3), 3)

def up_ver_2(screen):
    pygame.draw.line(screen, 'red', (550 + a/3, 300 + b/3), (550 + a*(2/3), 300 + b*(2/3)),3)

def up_ver_3(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300 + b*(2/3)), (800, 400), 3)

def up_ver_4(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 300 - b*(1/3)), (550 + a*(2/3), 300), 3)

def up_ver_5(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300), (800, 300 + b*(1/3)),3)

def up_ver_6(screen):
    pygame.draw.line(screen, 'red', (800, 300 + b*(1/3)), (800+a*(1/3), 300 + b*(2/3)), 3)

def up_ver_7(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300 - b*(2/3)), (800, 300 - b*(1/3)), 3)

def up_ver_8(screen):
    pygame.draw.line(screen, 'red', (800, 300 - b*(1/3)), (800 + a*(1/3), 300), 3)

def up_ver_9(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 300), (800 + a*(2/3), 300 + b*(1/3)), 3)

def up_ver_10(screen):
    pygame.draw.line(screen, 'red', (800, 200), (800 + a*(1/3), 200 + b*(1/3)), 3)

def up_ver_11(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 200 + b*(1/3)), (800 + a*(2/3), 200 + b*(2/3)), 3)

def up_ver_12(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 200 + b*(2/3)), (1050, 300), 3)

#############################################################################################  
    
def left_hor_1(screen):
    pygame.draw.line(screen, 'red', (550, 400),                         (550 + a/3, 400 + b/3),         3)

def left_hor_2(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 400 + b*(1/3)), (550 + a*(2/3), 400 + b*(2/3)), 3)

def left_hor_3(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 400 + b*(2/3)), (800, 500),                         3)

def left_hor_4(screen):
    pygame.draw.line(screen, 'red', (550, 500),                         (550 + a*(1/3), 500 + b*(1/3)), 3)

def left_hor_5(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 500 + b*(1/3)), (550 + a*(2/3), 500 + b*(2/3)), 3)

def left_hor_6(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 500 + b*(2/3)),             (800, 600),             3)

def left_hor_7(screen):
    pygame.draw.line(screen, 'red', (550, 600),                         (550 + a*(1/3), 600 + b*(1/3)), 3)

def left_hor_8(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 600 + b*(1/3)), (550 + a*(2/3), 600 + b*(2/3)), 3)

def left_hor_9(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 600 + b*(2/3)), (800, 700),                         3)
###########################################################################################
def right_hor_1(screen):
    pygame.draw.line(screen, 'red', (800, 500),                         (800 + a/3, 500 - b/3),         3)

def right_hor_2(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 500 - b*(1/3)), (800 + a*(2/3), 500 - b*(2/3)), 3)

def right_hor_3(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 500 - b*(2/3)), (1050, 400),                        3)

def right_hor_4(screen):
    pygame.draw.line(screen, 'red', (800, 600),                         (800 + a*(1/3), 600 - b*(1/3)), 3)

def right_hor_5(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 600 - b*(1/3)), (800 + a*(2/3), 600 - b*(2/3)), 3)

def right_hor_6(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 600 - b*(2/3)), (1050, 500),                        3)

def right_hor_7(screen):
    pygame.draw.line(screen, 'red', (800, 700),                         (800 + a*(1/3), 700 - b*(1/3)), 3)

def right_hor_8(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 700 - b*(1/3)), (800 + a*(2/3), 700 - b*(2/3)), 3)

def right_hor_9(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 700 - b*(2/3)), (1050, 600),                        3)
########################################################################################################
def ver_1(screen):
    pygame.draw.line(screen, 'red', (550, 300), (550, 400), 3)

def ver_2(screen):
    pygame.draw.line(screen, 'red', (550, 400), (550, 500), 3)

def ver_3(screen):
    pygame.draw.line(screen, 'red', (550, 500), (550, 600), 3)

def ver_4(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 300 + b*(1/3)), (550 + a*(1/3), 400 + b*(1/3)), 3)

def ver_5(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 400 + b*(1/3)), (550 + a*(1/3), 500 + b*(1/3)), 3)

def ver_6(screen):
    pygame.draw.line(screen, 'red', (550 + a*(1/3), 500 + b*(1/3)), (550 + a*(1/3), 600 + b*(1/3)), 3)

def ver_7(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 300 + b*(2/3)), (550 + a*(2/3), 400 + b*(2/3)), 3)

def ver_8(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 400 + b*(2/3)), (550 + a*(2/3), 500 + b*(2/3)), 3)

def ver_9(screen):
    pygame.draw.line(screen, 'red', (550 + a*(2/3), 500 + b*(2/3)), (550 + a*(2/3), 600 + b*(2/3)), 3)

def ver_10(screen):
    pygame.draw.line(screen, 'red', (800, 400), (800, 500), 3)

def ver_11(screen):
    pygame.draw.line(screen, 'red', (800, 500), (800, 600), 3)

def ver_12(screen):
    pygame.draw.line(screen, 'red', (800, 600), (800, 700), 3)

def ver_13(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 400 - b*(1/3)), (800 + a*(1/3), 500 - b*(1/3)), 3)

def ver_14(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 500 - b*(1/3)), (800 + a*(1/3), 600 - b*(1/3)), 3)

def ver_15(screen):
    pygame.draw.line(screen, 'red', (800 + a*(1/3), 600 - b*(1/3)), (800 + a*(1/3), 700 - b*(1/3)), 3)

def ver_16(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 400 - b*(2/3)), (800 + a*(2/3), 500 - b*(2/3)), 3)

def ver_17(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 500 - b*(2/3)), (800 + a*(2/3), 600 - b*(2/3)), 3)

def ver_18(screen):
    pygame.draw.line(screen, 'red', (800 + a*(2/3), 600 - b*(2/3)), (800 + a*(2/3), 700 - b*(2/3)), 3)

def ver_19(screen):
    pygame.draw.line(screen, 'red', (1050, 300), (1050, 400), 3)

def ver_20(screen):
    pygame.draw.line(screen, 'red', (1050, 400), (1050, 500), 3)

def ver_21(screen):
    pygame.draw.line(screen, 'red', (1050, 500), (1050, 600), 3)



def rf_rotate_side_up_clockwise(cube, screen, angle):
    draw_left(screen)
    draw_right(screen)
    ver_2(screen)
    ver_3(screen)
    ver_5(screen)
    ver_6(screen)
    ver_8(screen)
    ver_9(screen)
    ver_11(screen)
    ver_12(screen)
    ver_14(screen)
    ver_15(screen)
    ver_17(screen)
    ver_18(screen)
    ver_20(screen)
    ver_21(screen)



    cords_top1 = [x + y for x, y in zip(calculate_elipse_cords(randomassformula(angle)/180 * math.pi), [800, 300])]
    cords_top2 = [x + y for x, y in zip(calculate_elipse_cords((randomassformula(angle + 90)/180) * math.pi), [800, 300])]
    cords_top3 = [x + y for x, y in zip(calculate_elipse_cords((randomassformula(angle + 180)/180) * math.pi), [800, 300])]
    cords_top4 = [x + y for x, y in zip(calculate_elipse_cords((randomassformula(angle + 270)/180) * math.pi), [800, 300])]
    pygame.draw.line(screen, 'red', (cords_top1[0], cords_top1[1]), (cords_top2[0], cords_top2[1]), 3)
    pygame.draw.line(screen, 'red', (cords_top2[0], cords_top2[1]), (cords_top3[0], cords_top3[1]), 3)
    pygame.draw.line(screen, 'red', (cords_top3[0], cords_top3[1]), (cords_top4[0], cords_top4[1]), 3)
    pygame.draw.line(screen, 'red', (cords_top4[0], cords_top4[1]), (cords_top1[0], cords_top1[1]), 3)

    pygame.draw.line(screen, 'red', (cords_top2[0] + (cords_top1[0] - cords_top2[0])*(1/3), cords_top2[1] + (cords_top1[1] - cords_top2[1])*(1/3)), 
                                    (cords_top3[0] - (cords_top3[0] - cords_top4[0])*(1/3), cords_top3[1] - (cords_top3[1] - cords_top4[1])*(1/3)), 3)
    pygame.draw.line(screen, 'red', (cords_top2[0] + (cords_top1[0] - cords_top2[0])*(2/3), cords_top2[1] + (cords_top1[1] - cords_top2[1])*(2/3)), 
                                    (cords_top3[0] - (cords_top3[0] - cords_top4[0])*(2/3), cords_top3[1] - (cords_top3[1] - cords_top4[1])*(2/3)), 3)
    
    pygame.draw.line(screen, 'red', (cords_top4[0] + (cords_top1[0] - cords_top4[0])*(1/3), cords_top4[1] + (cords_top1[1] - cords_top4[1])*(1/3)), 
                                    (cords_top3[0] - (cords_top3[0] - cords_top2[0])*(1/3), cords_top3[1] - (cords_top3[1] - cords_top2[1])*(1/3)), 3)
    pygame.draw.line(screen, 'red', (cords_top4[0] + (cords_top1[0] - cords_top4[0])*(2/3), cords_top4[1] + (cords_top1[1] - cords_top4[1])*(2/3)), 
                                    (cords_top3[0] - (cords_top3[0] - cords_top2[0])*(2/3), cords_top3[1] - (cords_top3[1] - cords_top2[1])*(2/3)), 3)

    pygame.display.update()






def rf_rotate_side_up_counterclockwise(cube, screen):
    draw_left(screen)
    draw_right(screen)
    ver_2(screen)
    ver_3(screen)
    ver_5(screen)
    ver_6(screen)
    ver_8(screen)
    ver_9(screen)
    ver_11(screen)
    ver_12(screen)
    ver_14(screen)
    ver_15(screen)
    ver_17(screen)
    ver_18(screen)
    ver_20(screen)
    ver_21(screen)

def rf_rotate_side_middle_clockwise(cube, screen):
    draw_up(screen)
    draw_left(screen)
    draw_right(screen)
    ver_1(screen)
    ver_3(screen)
    ver_4(screen)
    ver_6(screen)
    ver_7(screen)
    ver_9(screen)
    ver_10(screen)
    ver_12(screen)
    ver_13(screen)
    ver_15(screen)
    ver_16(screen)
    ver_18(screen)
    ver_19(screen)
    ver_21(screen)

def rf_rotate_side_middle_counterclockwise(cube, screen):
    draw_up(screen)
    draw_left(screen)
    draw_right(screen)
    ver_1(screen)
    ver_3(screen)
    ver_4(screen)
    ver_6(screen)
    ver_7(screen)
    ver_9(screen)
    ver_10(screen)
    ver_12(screen)
    ver_13(screen)
    ver_15(screen)
    ver_16(screen)
    ver_18(screen)
    ver_19(screen)
    ver_21(screen)

def rf_rotate_side_down_clockwise(cube, screen):
    draw_up(screen)
    
    left_hor_1(screen)
    left_hor_2(screen)
    left_hor_3(screen)
    left_hor_4(screen)
    left_hor_5(screen)
    left_hor_6(screen)

    right_hor_1(screen)
    right_hor_2(screen)
    right_hor_3(screen)
    right_hor_4(screen)
    right_hor_5(screen)
    right_hor_6(screen)

    ver_1(screen)
    ver_2(screen)
    ver_4(screen)
    ver_5(screen)
    ver_7(screen)
    ver_8(screen)
    ver_10(screen)
    ver_11(screen)
    ver_13(screen)
    ver_14(screen)
    ver_16(screen)
    ver_17(screen)
    ver_19(screen)
    ver_20(screen)

def rf_rotate_side_down_counterclockwise(cube, screen):
    draw_up(screen)
    
    left_hor_1(screen)
    left_hor_2(screen)
    left_hor_3(screen)
    left_hor_4(screen)
    left_hor_5(screen)
    left_hor_6(screen)

    right_hor_1(screen)
    right_hor_2(screen)
    right_hor_3(screen)
    right_hor_4(screen)
    right_hor_5(screen)
    right_hor_6(screen)

    ver_1(screen)
    ver_2(screen)
    ver_4(screen)
    ver_5(screen)
    ver_7(screen)
    ver_8(screen)
    ver_10(screen)
    ver_11(screen)
    ver_13(screen)
    ver_14(screen)
    ver_16(screen)
    ver_17(screen)
    ver_19(screen)
    ver_20(screen)


def rf_rotate_side_left_clockwise(cube, screen):
    up_hor_2(screen)
    up_hor_3(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_8(screen)
    up_hor_9(screen)
    up_hor_11(screen)
    up_hor_12(screen)

    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_9(screen)
    up_ver_10(screen)
    up_ver_11(screen)
    up_ver_12(screen)

    right_hor_2(screen)
    right_hor_3(screen)
    right_hor_5(screen)
    right_hor_6(screen)
    right_hor_8(screen)
    right_hor_9(screen)

    ver_13(screen)
    ver_14(screen)
    ver_15(screen)
    ver_16(screen)
    ver_17(screen)
    ver_18(screen)
    ver_19(screen)
    ver_20(screen)
    ver_21(screen)
   
def rf_rotate_side_middle_right_clockwise(cube, screen):
    up_hor_1(screen)
    up_hor_3(screen)
    up_hor_4(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_9(screen)
    up_hor_10(screen)
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

    draw_ver(screen)
    draw_left(screen)

    right_hor_1(screen)
    right_hor_3(screen)
    right_hor_4(screen)
    right_hor_6(screen)
    right_hor_7(screen)
    right_hor_9(screen)

def rf_rotate_side_back_right_clockwise(cube, screen):
    up_hor_1(screen)
    up_hor_2(screen)
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_10(screen)
    up_hor_11(screen)

    up_ver_1(screen)
    up_ver_2(screen)
    up_ver_3(screen)
    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_9(screen)

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

    draw_left(screen)

    right_hor_1(screen)
    right_hor_2(screen)
    right_hor_4(screen)
    right_hor_5(screen)
    right_hor_7(screen)
    right_hor_8(screen)

def rf_rotate_side_left_counterclockwise(cube, screen):
    up_hor_2(screen)
    up_hor_3(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_8(screen)
    up_hor_9(screen)
    up_hor_11(screen)
    up_hor_12(screen)

    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_9(screen)
    up_ver_10(screen)
    up_ver_11(screen)
    up_ver_12(screen)

    right_hor_2(screen)
    right_hor_3(screen)
    right_hor_5(screen)
    right_hor_6(screen)
    right_hor_8(screen)
    right_hor_9(screen)

    ver_13(screen)
    ver_14(screen)
    ver_15(screen)
    ver_16(screen)
    ver_17(screen)
    ver_18(screen)
    ver_19(screen)
    ver_20(screen)
    ver_21(screen)
   
def rf_rotate_side_middle_right_counterclockwise(cube, screen):
    up_hor_1(screen)
    up_hor_3(screen)
    up_hor_4(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_9(screen)
    up_hor_10(screen)
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

    draw_ver(screen)
    draw_left(screen)

    right_hor_1(screen)
    right_hor_3(screen)
    right_hor_4(screen)
    right_hor_6(screen)
    right_hor_7(screen)
    right_hor_9(screen)

def rf_rotate_side_back_right_counterclockwise(cube, screen):
    up_hor_1(screen)
    up_hor_2(screen)
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_10(screen)
    up_hor_11(screen)

    up_ver_1(screen)
    up_ver_2(screen)
    up_ver_3(screen)
    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_9(screen)

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

    draw_left(screen)

    right_hor_1(screen)
    right_hor_2(screen)
    right_hor_4(screen)
    right_hor_5(screen)
    right_hor_7(screen)
    right_hor_8(screen)


def rf_rotate_side_right_clockwise(cube, screen):
    up_hor_1(screen)
    up_hor_2(screen)
    up_hor_3(screen)
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_9(screen)

    up_ver_1(screen)
    up_ver_2(screen)
    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_10(screen)
    up_ver_11(screen)

    ver_1(screen)
    ver_2(screen)
    ver_3(screen)
    ver_4(screen)
    ver_5(screen)
    ver_6(screen)
    ver_7(screen)
    ver_8(screen)
    ver_9(screen)

    left_hor_1(screen)
    left_hor_2(screen)
    left_hor_4(screen)
    left_hor_5(screen)
    left_hor_7(screen)
    left_hor_8(screen)

def rf_rotate_side_middle_left_clockwise(cube, screen):
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
    up_ver_3(screen)
    up_ver_4(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_9(screen)
    up_ver_10(screen)
    up_ver_12(screen)

    draw_ver(screen)
    draw_right(screen)

    left_hor_1(screen)
    left_hor_3(screen)
    left_hor_4(screen)
    left_hor_6(screen)
    left_hor_7(screen)
    left_hor_9(screen)

def rf_rotate_side_back_left_clockwise(cube, screen):
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_9(screen)
    up_hor_10(screen)
    up_hor_11(screen)
    up_hor_12(screen)

    up_ver_2(screen)
    up_ver_3(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_8(screen)
    up_ver_9(screen)
    up_ver_11(screen)
    up_ver_12(screen)

    left_hor_2(screen)
    left_hor_3(screen)
    left_hor_5(screen)
    left_hor_6(screen)
    left_hor_8(screen)
    left_hor_9(screen)

    draw_right(screen)

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

def rf_rotate_side_right_counterclockwise(cube, screen):
    up_hor_1(screen)
    up_hor_2(screen)
    up_hor_3(screen)
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_9(screen)

    up_ver_1(screen)
    up_ver_2(screen)
    up_ver_4(screen)
    up_ver_5(screen)
    up_ver_7(screen)
    up_ver_8(screen)
    up_ver_10(screen)
    up_ver_11(screen)

    ver_1(screen)
    ver_2(screen)
    ver_3(screen)
    ver_4(screen)
    ver_5(screen)
    ver_6(screen)
    ver_7(screen)
    ver_8(screen)
    ver_9(screen)

    left_hor_1(screen)
    left_hor_2(screen)
    left_hor_4(screen)
    left_hor_5(screen)
    left_hor_7(screen)
    left_hor_8(screen)

def rf_rotate_side_middle_left_counterclockwise(cube, screen):
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
    up_ver_3(screen)
    up_ver_4(screen)
    up_ver_6(screen)
    up_ver_7(screen)
    up_ver_9(screen)
    up_ver_10(screen)
    up_ver_12(screen)

    draw_ver(screen)
    draw_right(screen)

    left_hor_1(screen)
    left_hor_3(screen)
    left_hor_4(screen)
    left_hor_6(screen)
    left_hor_7(screen)
    left_hor_9(screen)

def rf_rotate_side_back_left_counterclockwise(cube, screen):
    up_hor_4(screen)
    up_hor_5(screen)
    up_hor_6(screen)
    up_hor_7(screen)
    up_hor_8(screen)
    up_hor_9(screen)
    up_hor_10(screen)
    up_hor_11(screen)
    up_hor_12(screen)

    up_ver_2(screen)
    up_ver_3(screen)
    up_ver_5(screen)
    up_ver_6(screen)
    up_ver_8(screen)
    up_ver_9(screen)
    up_ver_11(screen)
    up_ver_12(screen)

    left_hor_2(screen)
    left_hor_3(screen)
    left_hor_5(screen)
    left_hor_6(screen)
    left_hor_8(screen)
    left_hor_9(screen)

    draw_right(screen)

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










