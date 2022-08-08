We are going to model points in 2D space as objects of a class named Point. Mathematical details that are relevant to solve this problem are given below:
(1) Distance of a point P(x, y)P(x,y) from the origin is \sqrt{x^2 + y^2} 
x 
2
 +y 
2
 
​
 .
(2) Slope of the line joining the origin and PP is \cfrac{y}{x} 
x
y
​
 , for x \neq 0x

=0.

Define a class named Point that has the following specification:

Attributes

(1) x: int, x-coordinate of the point in 2D space.
(2) y: int, y-coordinate of the point in 2D space.

Methods

self is the first argument of all methods. We will only mention the additional arguments, if any.

(1) __init__: constructor with two arguments — x and y; assign these two values to the corresponding attributes within the constructor
(2) distance: return the distance of the point from the origin as a float value
(3) is_origin: return True if the point coincides with the origin, and False otherwise
(4) on_xaxis: return True if the point is on the x-axis, and False otherwise
(5) on_yaxis: return True if the point is on the y-axis and False otherwise
(6) quadrant: return the quadrant that this point belongs to; assume that this method will only be called if the point is not on either of the axes; possible return values are ['first', 'second', 'third', 'fourth'].
(7) slope: return the slope of the line joining the origin and this point as a float value; assume that this method will only be called if the point is not on the y-axis




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def is_origin(self):
        return self.x == 0 and self.y == 0

    def on_xaxis(self):
        return self.y == 0

    def on_yaxis(self):
        return self.x == 0

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 'first'
        if self.x < 0 and self.y > 0:
            return 'second'
        if self.x < 0 and self.y < 0:
            return 'third'
        if self.x > 0 and self.y < 0:
            return 'fourth'

    def slope(self):
        return self.y / self.x