"""Module for cube class"""

from random import randint
import helpers


class Cube:
    """Cube class"""
    def __init__(self):
        """Initialize the cube with default colors for each face"""
        self.up = [['W' for _ in range(0, 3)] for _ in range(0, 3)]
        self.left = [['R' for _ in range(0, 3)] for _ in range(0, 3)]
        self.right = [['B' for _ in range(0, 3)] for _ in range(0, 3)]
        self.down = [['Y' for _ in range(0, 3)] for _ in range(0, 3)]
        self.back_left = [['G' for _ in range(0, 3)] for _ in range(0, 3)]
        self.back_right = [['O' for _ in range(0, 3)] for _ in range(0, 3)]

    def print_cube(self):
        """Prints the current state of the cube"""
        for i in range(0, 3):
            if i < 1:
                for j in range(0, 3):
                    print("      " + str(' '.join(self.back_left[j])))
            elif i < 2:
                for j in range(0, 3):
                    print(' '.join(self.left[j]) + " " + ' '.join(self.up[j]) + " " +
                          ' '.join(self.back_right[j]) + " " + ' '.join(self.down[j]))
            else:
                for j in range(0, 3):
                    print("      " + ' '.join(self.right[j]))

    def rotate_cube_left_to_up(self):
        """"Rotates the cube so the left face faces up"""
        self.up, self.back_right, self.down, self.left = self.left, self.up, self.back_right, self.down
        self.up = helpers.face_rotate_clockwise(self.up)
        self.back_right = helpers.face_rotate_clockwise(self.back_right)
        self.right = helpers.face_rotate_clockwise(self.right)
        self.back_left = helpers.face_rotate_counterclockwise(self.back_left)
        self.left = helpers.face_rotate_counterclockwise(self.left)
        self.down = helpers.face_rotate_counterclockwise(self.down)

    def rotate_cube_right_to_up(self):
        """Rotates the cube so the right face faces up"""
        self.up, self.back_left, self.down, self.right = self.right, self.up, self.back_left, self.down
        self.back_right = helpers.face_rotate_clockwise(self.back_right)
        self.right = helpers.face_rotate_clockwise(helpers.face_rotate_clockwise(self.right))
        self.back_left = helpers.face_rotate_counterclockwise(helpers.face_rotate_counterclockwise(self.back_left))
        self.left = helpers.face_rotate_counterclockwise(self.left)

    def rotate_cube_up_to_left(self):
        """Rotates the cube so the up face faces left"""
        self.rotate_cube_left_to_up()
        self.rotate_cube_left_to_up()
        self.rotate_cube_left_to_up()

    def rotate_cube_up_to_right(self):
        """Rotates the cube so the up face faces right"""
        self.rotate_cube_right_to_up()
        self.rotate_cube_right_to_up()
        self.rotate_cube_right_to_up()

    def rotate_cube_left_to_right(self):
        """Rotates the cube so the left face faces right"""
        self.up = helpers.face_rotate_counterclockwise(self.up)
        self.down = helpers.face_rotate_counterclockwise(self.down)
        self.left, self.right, self.back_right, self.back_left = self.back_left, self.left, self.right, self.back_right

    def rotate_cube_right_to_left(self):
        """Rotates the cube so the right face faces left"""
        self.up = helpers.face_rotate_clockwise(self.up)
        self.down = helpers.face_rotate_clockwise(self.down)
        self.left, self.right, self.back_right, self.back_left = self.right, self.back_right, self.back_left, self.left

    def is_solved(self):
        """Check if the cube is solved"""
        for face in [self.up, self.left, self.right, self.down, self.back_left, self.back_right]:
            color = face[0][0]
            for row in face:
                for sticker in row:
                    if sticker != color:
                        return False
        return True

    # Rotate sides horizontaly
    def rotate_side_up_clockwise(self):
        """Rotates the up facing side clockwise"""
        self.right[0], self.left[0], self.back_left[0], self.back_right[0] = helpers.rotate_side_clockwise(
            self.right[0], self.left[0], self.back_left[0], self.back_right[0])
        self.up = helpers.face_rotate_clockwise(self.up)

    def rotate_side_up_counterclockwise(self):
        """Rotates the up facing side counterclockwise"""
        self.rotate_side_up_clockwise()
        self.rotate_side_up_clockwise()
        self.rotate_side_up_clockwise()

    def rotate_side_middle_clockwise(self):
        """Rotates the middle side parallel to the up face clockwise"""
        self.right[1], self.left[1], self.back_left[1], self.back_right[1] = helpers.rotate_side_clockwise(
            self.right[1], self.left[1], self.back_left[1], self.back_right[1])

    def rotate_side_middle_counterclockwise(self):
        """Rotates the middle side parallel to the up face counterclockwise"""
        self.right[1], self.left[1], self.back_left[1], self.back_right[1] = helpers.rotate_side_counterclockwise(
            self.right[1], self.left[1], self.back_left[1], self.back_right[1])

    def rotate_side_down_counterclockwise(self):
        """Rotates the down facing side clockwise"""
        self.right[2], self.left[2], self.back_left[2], self.back_right[2] = helpers.rotate_side_counterclockwise(
            self.right[2], self.left[2], self.back_left[2], self.back_right[2])
        self.down = helpers.face_rotate_clockwise(self.down)

    def rotate_side_down_clockwise(self):
        """Rotates the down facing side counterclockwise"""
        self.rotate_side_down_counterclockwise()
        self.rotate_side_down_counterclockwise()
        self.rotate_side_down_counterclockwise()

    # Rotate sides perpendicular ot the left plane

    def rotate_side_left_clockwise(self):
        """Rotates the left facing side clockwise"""
        self.left = helpers.face_rotate_clockwise(self.left)
        self.up[0][0], self.right[0][0], self.down[2][2], self.back_left[2][2] = helpers.rotate_side_clockwise(
            self.up[0][0], self.right[0][0], self.down[2][2], self.back_left[2][2])
        self.up[1][0], self.right[1][0], self.down[1][2], self.back_left[1][2] = helpers.rotate_side_clockwise(
            self.up[1][0], self.right[1][0], self.down[1][2], self.back_left[1][2])
        self.up[2][0], self.right[2][0], self.down[0][2], self.back_left[0][2] = helpers.rotate_side_clockwise(
            self.up[2][0], self.right[2][0], self.down[0][2], self.back_left[0][2])

    def rotate_side_left_counterclockwise(self):
        """Rotates the left facing side counterclockwise"""
        self.rotate_side_left_clockwise()
        self.rotate_side_left_clockwise()
        self.rotate_side_left_clockwise()

    def rotate_side_middle_right_clockwise(self):
        """Rotates the middle side parallel to the left face clockwise"""
        self.up[0][1], self.right[0][1], self.down[2][1], self.back_left[2][1] = helpers.rotate_side_clockwise(
            self.up[0][1], self.right[0][1], self.down[2][1], self.back_left[2][1])
        self.up[1][1], self.right[1][1], self.down[1][1], self.back_left[1][1] = helpers.rotate_side_clockwise(
            self.up[1][1], self.right[1][1], self.down[1][1], self.back_left[1][1])
        self.up[2][1], self.right[2][1], self.down[0][1], self.back_left[0][1] = helpers.rotate_side_clockwise(
            self.up[2][1], self.right[2][1], self.down[0][1], self.back_left[0][1])

    def rotate_side_middle_right_counterclockwise(self):
        """Rotates the middle side parallel to the left face counterclockwise"""
        self.rotate_side_middle_right_clockwise()
        self.rotate_side_middle_right_clockwise()
        self.rotate_side_middle_right_clockwise()

    def rotate_side_back_right_clockwise(self):
        """Rotates the back right facing side clockwise"""
        self.back_right = helpers.face_rotate_counterclockwise(self.back_right)
        self.up[0][2], self.right[0][2], self.down[2][0], self.back_left[2][0] = helpers.rotate_side_clockwise(
            self.up[0][2], self.right[0][2], self.down[2][0], self.back_left[2][0])
        self.up[1][2], self.right[1][2], self.down[1][0], self.back_left[1][0] = helpers.rotate_side_clockwise(
            self.up[1][2], self.right[1][2], self.down[1][0], self.back_left[1][0])
        self.up[2][2], self.right[2][2], self.down[0][0], self.back_left[0][0] = helpers.rotate_side_clockwise(
            self.up[2][2], self.right[2][2], self.down[0][0], self.back_left[0][0])

    def rotate_side_back_right_counterclockwise(self):
        """Rotates theback right facing side counterclockwise"""
        self.rotate_side_back_right_clockwise()
        self.rotate_side_back_right_clockwise()
        self.rotate_side_back_right_clockwise()

    # Rotate sides perpendicular ot the right plane

    def rotate_side_right_clockwise(self):
        """Rotates the right facing side clockwise"""
        self.right = helpers.face_rotate_clockwise(self.right)
        self.up[2][0], self.back_right[0][0], self.down[2][0], self.left[2][2] = helpers.rotate_side_clockwise(
            self.up[2][0], self.back_right[0][0], self.down[2][0], self.left[2][2])
        self.up[2][1], self.back_right[1][0], self.down[2][1], self.left[1][2] = helpers.rotate_side_clockwise(
            self.up[2][1], self.back_right[1][0], self.down[2][1], self.left[1][2])
        self.up[2][2], self.back_right[2][0], self.down[2][2], self.left[0][2] = helpers.rotate_side_clockwise(
            self.up[2][2], self.back_right[2][0], self.down[2][2], self.left[0][2])

    def rotate_side_right_counterclockwise(self):
        """Rotates the right facing side counterclockwise"""
        self.rotate_side_right_clockwise()
        self.rotate_side_right_clockwise()
        self.rotate_side_right_clockwise()

    def rotate_side_middle_left_clockwise(self):
        """Rotates the middle side parallel to the right face clockwise"""
        self.up[1][0], self.back_right[0][1], self.down[1][0], self.left[2][1] = helpers.rotate_side_clockwise(
            self.up[1][0], self.back_right[0][1], self.down[1][0], self.left[2][1])
        self.up[1][1], self.back_right[1][1], self.down[1][1], self.left[1][1] = helpers.rotate_side_clockwise(
            self.up[1][1], self.back_right[1][1], self.down[1][1], self.left[1][1])
        self.up[1][2], self.back_right[2][1], self.down[1][2], self.left[0][1] = helpers.rotate_side_clockwise(
            self.up[1][2], self.back_right[2][1], self.down[1][2], self.left[0][1])

    def rotate_side_middle_left_counterclockwise(self):
        """Rotates the middle side parallel to the right face counterclockwise"""
        self.rotate_side_middle_left_clockwise()
        self.rotate_side_middle_left_clockwise()
        self.rotate_side_middle_left_clockwise()

    def rotate_side_back_left_clockwise(self):
        """Rotates the back left facing side clockwise"""
        self.back_left = helpers.face_rotate_counterclockwise(self.back_left)
        self.up[0][0], self.back_right[0][2], self.down[0][0], self.left[2][0] = helpers.rotate_side_clockwise(
            self.up[0][0], self.back_right[0][2], self.down[0][0], self.left[2][0])
        self.up[0][1], self.back_right[1][2], self.down[0][1], self.left[1][0] = helpers.rotate_side_clockwise(
            self.up[0][1], self.back_right[1][2], self.down[0][1], self.left[1][0])
        self.up[0][2], self.back_right[2][2], self.down[0][2], self.left[0][0] = helpers.rotate_side_clockwise(
            self.up[0][2], self.back_right[2][2], self.down[0][2], self.left[0][0])

    def rotate_side_back_left_counterclockwise(self):
        """Rotates the back left facing side counterclockwise"""
        self.rotate_side_back_left_clockwise()
        self.rotate_side_back_left_clockwise()
        self.rotate_side_back_left_clockwise()

    def shuffle(self):
        """Shuffles the cube, 20 turns by choosing side at random"""
        for _ in range(0,20):
            match (randint(1,18)):
                case 1: self.rotate_side_up_counterclockwise()
                case 2: self.rotate_side_up_clockwise()
                case 3: self.rotate_side_middle_counterclockwise()
                case 4: self.rotate_side_middle_clockwise()
                case 5: self.rotate_side_down_counterclockwise()
                case 6: self.rotate_side_down_clockwise()
                case 7: self.rotate_side_left_counterclockwise()
                case 8: self.rotate_side_left_clockwise()
                case 9: self.rotate_side_middle_right_counterclockwise()
                case 10: self.rotate_side_middle_right_clockwise()
                case 11: self.rotate_side_back_right_counterclockwise()
                case 12: self.rotate_side_back_right_clockwise()
                case 13: self.rotate_side_right_counterclockwise()
                case 14: self.rotate_side_right_clockwise()
                case 15: self.rotate_side_middle_left_counterclockwise()
                case 16: self.rotate_side_middle_left_clockwise()
                case 17: self.rotate_side_back_left_counterclockwise()
                case 18: self.rotate_side_back_left_clockwise()
                case _: self.rotate_cube_left_to_right()

