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

    def insert_at_pos(self,pos,data):
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
        
    def delete_at_pos(self,pos):
        c = 1
        temp = self.head
        while c < pos - 1:
            c += 1
            temp = temp.next
        
        arb = temp
        temp1 = temp.next.next
        temp.next = temp1
        temp1.prev = arb

    def delete_and_insert(self,pos,data):
        newnode = Node(data)
        c = 1
        temp = self.head
        while c < pos - 1:
            c += 1
            temp = temp.next
        
        arb = temp
        temp1 = temp.next.next
        temp.next = newnode
        newnode.next = temp1
        newnode.prev = arb

    def traverse(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.data, end=' ')
            else:
                print(temp.data)
            temp = temp.next
    
    def traverse_rev(self):
        temp = self.last
        while temp != None:
            if temp.prev != None:
                print(temp.data, end=' ')
            else:
                print(temp.data)
            temp = temp.prev

ins = [0,1,2,3,4,5,6,7,8,9]
A = doubly_linked_list()
for i in ins:
    A.insert_end(i)
A.traverse()
A.insert_at_pos(7,10)
A.traverse()
A.delete_and_insert(7,11)
A.traverse()
A.delete_at_pos(7)
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

class create_stack:
  def __init__(self):
    self.stack = []
  def push(self,d):
    self.stack += [d]
  def pop(self):
    t = self.stack[-1]
    self.stack = self.stack[:-1]
    return t

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

'''
Quadratic probing is an open addressing scheme in computer programming for resolving hash
collisions in hash tables. Quadratic probing operates by taking the original hash index and adding
successive values of an arbitrary quadratic polynomial until an open or empty slot is found.
An example of a sequence using quadratic probing is:
h, h + 1, h + 4, h+ 9.. .h+ i2

Quadratic function
Let h(k) = k mod m be a hash function that maps an element k to an integer in [0, m-1], where
m is the size of the table. Let the ?" probe position for a value k be given by the function
h(k, i) = (h(k) + cli + czi") mod m
where cl and c2 are positive integers. The value of i = 0, 1, . . ., m - 1. So we start from
i = 0, and increase this until we get one free slot in hash table.

For a given class Hashing, create two methods:
. store_data(data): That accepts a positive integer data and generate an index value (0 to m-
1) using given quadratic function and stores data in hashtable list on corresponding index
generated by quadratic function. hashtable can contain only m data items. So, if all are
already filled, then print Hash table is full.
. display_hashtable(): That returns hashtable.

Input
    1 #cl
    1 #c2
    11 #m
    [22, 44, 35, 54, 36,27] # data for store one by one, start from 22
'''

class Hashing:
  def __init__(self,c1,c2,m):
    self.hashtable = []
    for i in range(m):
        self.hashtable.append(None)     
    self.c1 = c1
    self.c2 = c2
    self.m = m
  def hashfunction(self, data):
        i = 0
        key = (((data) % self.m + self.c1 * i + self.c2 * (i**2) ) % self.m)
        while self.hashtable[key] != None and i < self.m:
            key = (((data) % self.m + self.c1 * i + self.c2 * (i**2) ) % self.m)
            i += 1
        return key
  
  
  def store_data(self, data):
        if self.hashtable.count(None) != 0:
            key = self.hashfunction(data)
            self.hashtable[key] = data
        else:
            print('Hash table is full')

  def display_hashtable(self):
        return self.hashtable

c1 = int(input())
c2 = int(input())
m = int(input())
data=eval(input())
A = Hashing(c1,c2,m)
for i in data:
    A.store_data(i)
print(A.display_hashtable())
