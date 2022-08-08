class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name, self.age)
        
'''
we do not need to repeat codes, as a programming lesson, 
its always best practice to not repeat any code statements 
as much as possible

in this case, both classes (Employee and Student) 
share same variables (name and age) 
hence, we can try to write a single parent class which
gives them the same name and age

consider Employee and Student as siblings and write a parent 
class for both, and put these common attributes in that
parent class

uncommon attributes will stay in their particular class, only the
common attributes among classes will be shared amongst them in
parent class

hence, we create a class called Person which has name and age
'''        
        
#class Student inherits properties of its parent class Person
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        #takes the initialization from parent class
        self.marks = marks
        
    def display(self):
        super().display()
        #displays parent class def display() initially
        print(self.marks)
        
#class Employee inherits properties of its parent class Person    
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        #takes the initialization from parent class
        self.salary = salary
        
    def display(self):
        #instead of mentioning super class inheritance
        #we can do method over-ride
        #this overrides the method specified in parent class
        #with its own required spin-off
        print(self.name, self.age, self.salary)
    
'''
now that we have created a parent class Person, we have to 
somehow mention the fact that, class Employee and class Student
are children of this parent class Person 

for that we will mention within parenthesis of class Employee and 
class Student, (Person)
'''

s = Student('Rida', 20, 250)
s.display()

e = Student('Harsh', 30, 50000)
e.display()

'''
this method is called Inheritance, function super(), 
tells the class to initiate the corresponding function in
parent class and the execute the current behavior

the class inherits the properties of its parent, implementing
a child class for this class, the child inherits properties 
from both parent and grandparent and likewise
'''

'''
this whole process of using Inheritance, Method Overriding
to create small chunks of code is called Modularization 

if security is needed we can add two underscores before 
any variable in super class, so that it is held private

ex: self.__age
    self.__name 
    
will not enable inheritance on these variables by its children
(class Student, class Employee) on its parent (class Person)

hence we can selectively share information thru inheritance
'''

'''
Types of Inheritance:
    
a) one parent one child

b) one parent many child 
    
c) many parent many child
    
d) parent - child - grandchild
    
e) combination of all classes hybrid (no particular order)
    
'''





    
    



















