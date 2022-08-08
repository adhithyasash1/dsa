Write a class named Student with the following specification:

Attributes

(1) name: string, denotes the name of the student
(2) marks: int, denotes the marks obtained by the student in some exam

Methods

self is the first argument of all methods. We will only mention the additional arguments, if any.

(1) __init__: constructor with two arguments — name and marks; assign these two values to the corresponding attributes within the constructor
(2) print_info: prints the name and the marks of the student separated by a colon.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_info(self):
        print(f'{self.name}:{self.marks}')























