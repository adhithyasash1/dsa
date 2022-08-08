class Student:
    count = 0
    #this variable is not owned by the objects
    #hence there wont be any duplicate values of count
    #only one value of count owned by all objects
    #whenever we declare variables here
    #it is owned by the class
    def __init__(self, roll_no, name, total):
        #init is the contructor of the class
        #whenever we declare any variable 
        #inside init it is owned by the object
        #each object has its own value of these variables
        self.roll_no = roll_no
        self.name = name
        self.total = total
    
        
    def display(self):
        #every time any function from the class is executed
        #python knows which object initiated that execution
        
        #self is a container which holds the current object
        
        #we have to use self as the first parameter
        #in every function inside a class
        
        print(self.roll_no, self.name, self.total)
        
    def result(self):
        if self.total > 120:
            print('pass')
        else:
            print('fail')
        
s0 = Student(0, 'sashi', 100)
#after executing this code^ python executed def __init__ 

#initialize parameters against 
#some variables which are available in the class
#then we use constructor with parameters
s0.display()

s1 = Student(1, 'adhithya', 150)
#whenever we create an object 
#it has a copy of its own variable
#present inside the class (inside def __init__)
#we can perform all functions 
#present inside the class on that object

s1.display()
#s1.display makes self as s1 and displays the values of s1

s0.result()
s1.result()

Student.count += 1
Student.count += 1
print(Student.count)

#all functions defined inside a class are called methods.

















