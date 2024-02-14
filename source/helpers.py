import math

a=250
b=100

def transpose_matrix(matrix : list):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

def flip_horizontal_matrix(matrix:list):
    flipped_matrix = [row[::-1] for row in matrix]
    return flipped_matrix

def flip_vertical_matrix(matrix:list):
    flipped_matrix = matrix[::-1]
    return flipped_matrix

def face_rotate_counterclockwise(side:list):
    flipped_side = flip_horizontal_matrix(side)
    rotated_side = transpose_matrix(flipped_side)
    return rotated_side

def face_rotate_clockwise(side:list):
    # Rotate matrix counterclockwise by flipping vertically and then transposing
    flipped_side = flip_vertical_matrix(side)
    rotated_side = transpose_matrix(flipped_side)
    return rotated_side

def rotate_side_clockwise(side1, side2, side3, side4):
        return side4, side1, side2, side3

def rotate_side_counterclockwise(side1, side2, side3, side4):
        return side2, side3, side4, side1

def print_matrix(matrix:list):
    for row in matrix:
        print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def calculate_x_ellipse(a: int, b:int, angle:float)->float:
     return (a*b)/math.sqrt(b*b+a*a*(math.tan(angle%360)**2))

def calculate_y_ellipse(a: int, b:int, angle:float)->float:
     return b*math.sqrt(1-(calculate_x_ellipse(a,b,angle)**2)/(a**2))

def get_color(letter):
     match letter:
          case 'W': return (240, 240, 240)
          case 'R': return (230, 0, 0)
          case 'Y': return (230, 235, 0)
          case 'G': return (0, 128, 0)
          case 'B': return (0, 0, 204)
          case 'O': return (255, 115, 0)

