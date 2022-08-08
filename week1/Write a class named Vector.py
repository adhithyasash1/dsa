Write a class named Vector that has the following specification:

Attributes

(1) x: int, first coordinate of the vector
(2) y: int, second coordinate of the vector

Methods

(1) __init__: constructor with two arguments — x and y; assign these two values to the attributes within the constructor
(2) print_info: print a string that represents the coordinates of the current vector in the following form: (x,y); there should be no spaces anywhere in the string; you have to print and not return the string in this case
(3) scale: accept an integer s as argument and scale the current vector by ss units
(4) reflect_about_X: reflect the current vector about the X-axis
(5) reflect_about_Y: reflect the current vector about the Y-axis
(6) add: accept another Vector as argument, and return the sum of the current vector (self) and this argument; you must return an object of type Vector




class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect_about_X(self):
        self.y *= -1

    def reflect_about_Y(self):
        self.x *= -1

    def scale(self, s):
        self.x, self.y = s * self.x, s * self.y

    def add(self, V):
        v = Vector(0, 0)
        v.x = self.x + V.x
        v.y = self.y + V.y
        return v

    def print_info(self):
        return f'({self.x},{self.y})'


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def print(self):
        print(f'({self.x},{self.y})')
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def scale(self, s):
        self.x, self.y = self.x * s, self.y * s
    def rotate_xaxis(self):
        self.y = -self.y
    def rotate_yaxis(self):
        self.x = -self.x
    def add(self, P):
        result = Vector(0, 0)
        result.x, result.y = self.x + P.x, self.y + P.y
        return result


    def dist(P1, P2):
        return ((P1.x - P2.x) ** 2 + (P1.y - P2.y) ** 2) ** 0.5

    def side_lengths(triangle):
        la = dist(triangle[0], triangle[1])
        lb = dist(triangle[1], triangle[2])
        lc = dist(triangle[2], triangle[0])
        return la, lb, lc