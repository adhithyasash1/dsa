'''
A queue is a data structure in which whatever comes first will go out first. It follows the FIFO
(First-In-First-Out) policy.

In Queue, the insertion is done from one end known as the rear end of the queue, 
whereas the deletion is done from another end known as the front end of the queue.

For a given class Queue, create two methods :

Enqueue(data): that accepts an integer data and inserts it into the queue in the last
position.

Dequeue(): if queue is empty, returns None . Otherwise, delete one element of the queue
from the first position and returns deleted element value.

Note - Use given linked list structure for implementation.

sample input :

[2,4,6,8,10] #elements for insert in queue
3 # remove 3 elements from queue

2 # first removed element from queue
4 # second removed element from queue
6 # third removed element from queue
8, 10 #remaining elements in queue
'''

class Node:
    def __init__(self, data):
        self.data = data # store data
        self.next = None #point to the next node

class Queue:
    def __init__(self):
        self.head = None # point to the first node of the list
        self.last = None # point to the last node of the list

    def Enqueue(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode

    def Dequeue(self):
        if(self.head != None):
            item = self.head.data
            if self.head == self.last:
                self.head=None
                self.last=None
            else:
                self.head = self.head.next
            return item

# Suffix
def traverse(self):
    temp = self.head
    if temp != None:
        while temp != None:
            if temp.next != None:
                print(temp.data, end=',')
            else:   
                print(temp.data)
            temp = temp.next
    else:
        print('None')

ins = eval(input())
delt=int(input())
A = Queue()
for i in ins:
    A.Enqueue(i)
for j in range(delt):
    print(A.Dequeue())
A.traverse()

'''
A doubly linked list is a linked data structure that consists of a set of sequentially linked records
called nodes.

Each node contains three fields: two link fields (references to the previous and to
the next node in the sequence of nodes) and one data field.

So, it can be traversed in both directions.

For the given class doubly_linked_list, create one methods:

insert_at_pos(data,pos): 
that accepts an integer data and inserts it into the list at given pos position where 1 < pos <= length(list)

Note- Use given linked list structure to implementation.

Example : 

[1,3,5,7,9] # Elements for insert in list one by one, start from 1
20 # data
2 # position

1,20,3,5,7,9 # Traversed list from head to last
9,7,5,3,20,1 # Traversed list from last to head
'''

class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains the reference of next node
        self.prev = None # Contains the reference of previous node

class doubly_linked_list:
    def __init__(self):
        self.head = None # Contains the reference of first node of the list
        self.last = None # Contains the reference of the last node of the list

    def insert_end(self,data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode

    def insert_at_pos(self,data,pos):
        newnode = Node(data)
        c = 1
        temp = self.head
        while c < pos-1:
            temp = temp.next
            c += 1
        temp1 = temp.next
        temp.next = newnode
        newnode.next = temp1
        newnode.prev = temp
        temp.next=newnode
        temp1.prev=newnode


def traverse(self):
    temp = self.head
    while temp != None:
        if temp.next != None:
            print(temp.data, end=',')
        else:
            print(temp.data)
        temp = temp.next

def traverse_rev(self):
    temp = self.last
    while temp != None:
        if temp.prev != None:
            print(temp.data, end=',')
        else:
            print(temp.data)
        temp = temp.prev

ins = eval(input())
data = int(input())
pos=int(input())
A = doubly_linked_list()
for i in ins:
    A.insert_end(i)
A.insert_at_pos(data,pos)
A.traverse()
A.traverse_rev()

'''
Implement a Stack using only two Queues. The implemented Stack should support all the
functions of a normal stack ( push , pop , top , and isempty ).

Create the following method for given class stack :

push(data) insert element data to the top of the stack.

pop() If stack is empty return message Stack is empty . Otherwise, remove the element
from the top of the stack and return it.

top() If stack is empty return message Stack is empty . Otherwise, return the element on
the top of the stack.

isempty() Returns True if the stack is empty, False otherwise.

Example :

[10,20,30,40,50] #push one by one
2 # pop 2 elemnts

50 #first popped element
40 #second popped element
30 #top element
False #isempty
'''

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, key):
        self.items.insert(0,key)
    
    def dequeue(self):
        return self.items.pop()

class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def isempty(self):
        return (self.size==0)

    def top(self):
        if (not self.isempty()):
            return self.q1.items[-1]
        else:
            return 'Stack is empty'
    
    def push(self,data):
        self.size += 1
        self.q2.enqueue(data)
        while (self.q1.items != []):
            self.q2.enqueue(self.q1.dequeue())
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
    
    def pop(self):
        if (not self.isempty()):
            self.size -= 1
            return self.q1.dequeue()
        else:
            return 'Stack is empty'

# Suffix
inp = eval(input())
dl = int(input())
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())

