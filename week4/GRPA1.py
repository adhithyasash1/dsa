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

'''
another way: 
    
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
    
'''












