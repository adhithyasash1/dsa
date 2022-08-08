class Question:
    def __init__(self, statement, marks):
        self.statement = statement
        self.marks = marks
    
    def print_question(self):
        print(self.statement)
    
    def update_marks(self, marks):
        self.marks = marks


Question is a class that is defined in the prefix code. Define a class named NAT that is a sub-class of Question with the following specification:

Attributes

Only those attributes that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.

answer: int, numerical answer for this question
Methods

Only those methods that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.

(1) __init__: Accept the arguments statement, marks and answer. Call the constructor of the base class with the first two arguments, and assign answer to the corresponding attribute of the derived class.
(2) update_answer: Accept an argument named answer and update the corresponding attribute of the class with this new answer.



class NAT(Question):
    def __init__(self, statement, marks, answer):
        super().__init__(statement, marks)
        self.answer = answer

    def update_answer(self, answer):
        self.answer = answer



Question is a class that is defined in the prefix code. Define a class named MCQ that is a sub-class of Question with the following specification:

Attributes

Only those attributes that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.

(1) ops: list of strings; list of options and will always have four elements
(2) c_ops: list of strings, list of correct options, it will be a subset of ['a', 'b', 'c', 'd'].

Methods

Only those methods that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.

(1) __init__: Accept the arguments statement, marks and ops and c_ops. Call the constructor of the base class with the first two arguments, assign ops and c_ops to the corresponding attributes of the derived class.
(2) print_question: Since this method is already present in the base class, override it in the following way: print the statement of the question on the first line, followed by the four options on separate lines.


class MCQ(Question):
    def __init__(self, statement, marks, ops, c_ops):
        super().__init__(statement, marks)
        self.ops = ops      # list of all options
        self.c_ops = c_ops  # list of correct options

    def print_question(self):
        super().print_question()
        for i in range(4):
            print(self.ops[i])