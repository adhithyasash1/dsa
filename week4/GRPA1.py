'''
Consider a social network of friends/relatives, most of whom are closely connected. Visualize this
as a graph where each vertex denotes a person, and if two people know each other there is an
edge between the vertices denoting them. If persons x and y know each other directly, then
there is an edge connecting x and y and level of connectivity between them is 1. If person x is
a friend of person y and person y is friend of person z, but x is not a friend of z, 

then the level of connectivity between x and z is 2, and so on. The connectivity between people is always
two way, i.e. if x directly knows y, then y also knows x directly.

Complete the Python function findconnectionLevel (n, Gmat, Px, Py) that takes 4
arguments, number of persons In (n persons numbered from 0 to (n-1), Gmat an adjacency
matrix representation of n persons and their connections(if Gmat [x] [y] = 1, then person x
and y are directly connected), two persons Px and Py both numbers, and returns the minimum
level of connectivity between Px and Py . Return 0 if Px and py are not connected through
anybody in the group.

# For example, for the graph below representing 7 persons from 0 to 6 and their connectivity.

'''

def adjM_to_adjL(Amat):
    Alist = { }
    for i in range(len(Amat)):
        Alist[i] = [ ]
        for j in range(len(Amat)):
            if Amat[i][j]:
                Alist[i].append(j)
    return Alist

class Queue:
    def __init__(self):
        self.queue = [ ]
        
    def addq(self, v):
        self.queue.append(v)
        
    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def isempty(self):
        return (self.queue == [])
        
    def __str__(self):
        return str(self.queue)

def BFSListPathLevel(AList, Px):
    level, parent = { }, { }
    for i in AList.keys():
        level[i] = 0
        parent[i] = -1
        
    q = Queue()
    level[Px] = 0
    q.addq(Px)
    
    while not q.isempty():
        j = q.delq()
        for k in AList[j]:
            if level[k] == 0:
                level[k] = level[j] + 1
                parent[k] = j
                q.addq(k)
    return level
    
def findConnectionLevel(n, Amat, Px, Py):
    AList = adjM_to_adjL(Amat)
    levels = BFSListPathLevel(AList, Px)
    return levels[Py]
                 


# test inputs:

A = [[0,1,1,0,0,0,0],
     [1,0,1,1,1,1,0],
     [1,1,0,1,1,1,0],
     [0,1,1,0,1,0,0],
     [0,1,1,1,0,1,0],
     [0,1,1,0,1,0,1],
     [0,0,0,0,0,1,0]]    
    
B = [[0, 1, 1, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 1, 0],
     [1, 1, 0, 1, 1, 1, 0],
     [0, 1, 1, 0, 1, 0, 0],
     [0, 1, 1, 1, 0, 1, 0],
     [0, 1, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]


# Solution 2 
    
#Initializing the Graph Class
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
        
    #Function to implement BFS Traversal for SSSP
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

g = Graph(Adj)
print(g.bfs(0, 6))
'''

'''
def neighbours(Amat,v):
    (rows,cols) = (len(Amat),len(Amat[0]))
    nbrs = []
    for i in range(cols):
        if Amat[i][v] == 1:
            nbrs.append(i)
    return nbrs
    
def findConnectionLevel(v,Amat, X, Y):
    level = {}
    (rows,cols) = (len(Amat),len(Amat[0]))
    for i in range(rows):
        level[i] = -1
    q = []
    q.append(X)
    level[X] = 0
    
    while q != []:
        j = q.pop()
        for k in neighbours(Amat,j):
            
            if k == Y:
                level[k] = level[j]+1
                break
            
            if level[k] == -1:
                level[k] = level[j]+1
                q.append(k)
            
    
    if level[Y] >= 0:
        return level[Y]
    else:
        return 0

# Solution 3

# Helper function
from collections import deque
class myQueue:
  def __init__(self):
    self.Q = deque()
  
  def deQueue(self):
    return self.Q.popleft()

  def enQueue(self, x):
    return self.Q.append(x)

  def isEmpty(self):
    return False if self.Q else True

def findConnectionLevel(n, Gmat, Px, Py):
  q = myQueue() 
  visited = [False for i in range(n)]
  q.enQueue(Px)
  q.enQueue(-1) #using -1 in queue to distinguish between levels in BFS.
  visited[Px]=True
  level=1;

  while not q.isEmpty():
    v = q.deQueue()
    if (v == -1):
      level+=1
      if (not q.isEmpty()):
        q.enQueue(-1)
      continue
    for i in range(n):
      if(i==Py and Gmat[v][i] == 1):
        return level
      if(Gmat[v][i] and (not visited[i])):
        q.enQueue(i)
        visited[i]=True
  return 0

vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))

