import math

"""Dimentions"""
a=250
b=100

def randomassformula(angle):
    """Deprecated"""
    return angle

def calculate_elipse_cords(angle):
    """Deprecated"""
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
    return [x,y]
    

def transpose_matrix(matrix : list):
    """Transposes matrix. Returns the transposed matrix"""
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

def flip_horizontal_matrix(matrix:list):
    """Flip matrix horizontally. Returns flipped matrix"""
    flipped_matrix = [row[::-1] for row in matrix]
    return flipped_matrix

def flip_vertical_matrix(matrix:list):
    """Flips matrix vertically. Returns flipped matrix"""
    flipped_matrix = matrix[::-1]
    return flipped_matrix

def face_rotate_counterclockwise(side:list):
    """Rotates face of the cube clockwise"""
    flipped_side = flip_horizontal_matrix(side)
    rotated_side = transpose_matrix(flipped_side)
    return rotated_side

def face_rotate_clockwise(side:list):
    """Rotates face of the cube counterclockwise"""
    flipped_side = flip_vertical_matrix(side)
    rotated_side = transpose_matrix(flipped_side)
    return rotated_side

def rotate_side_clockwise(side1, side2, side3, side4):
    """Rotates the outside sets of small face of a side clockwise""" 
    return side4, side1, side2, side3

def rotate_side_counterclockwise(side1, side2, side3, side4):
    """Rotates the outside sets of small face of a side counterclockwise""" 
    return side2, side3, side4, side1

def print_matrix(matrix:list):
    """Prints matrix as table""" 
    for row in matrix:
        print(row)

def calculate_x_ellipse(a: int, b:int, angle:float)->float:
     """Deprecated"""
     return (a*b)/math.sqrt(b*b+a*a*(math.tan(angle%360)**2))

def calculate_y_ellipse(a: int, b:int, angle:float)->float:
     """Deprecated"""
     return b*math.sqrt(1-(calculate_x_ellipse(a,b,angle)**2)/(a**2))

def get_color(letter):
     """Returns RBG code for each color of the cube faces"""
     match letter:
          case 'W': return (240, 240, 240)
          case 'R': return (230, 0, 0)
          case 'Y': return (230, 235, 0)
          case 'G': return (0, 128, 0)
          case 'B': return (0, 0, 204)
          case 'O': return (255, 115, 0)
         

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

