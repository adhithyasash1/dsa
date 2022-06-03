class Queue:
    def __init__(self):
        self.queue = []
        
    def addq(self,v):
        self.queue.append(v)
    
    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])
    
    def __str__(self):
        return(str(self.queue))
    
#BFS traversal thru an Adjacency Matrix

def BFS(AMat,v):
    #Accept arguments, adjacency matrix and vertex to begin with
    (rows,cols) = AMat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
        q = Queue()
    visited[v] = True
    q.addq(v)
    while(not q.isempty()):
        j = q.delq()
        for k in neighbours(AMat,j):
            if (not visited[k]):
                visited[k] = True
                q.addq(k)
    return(visited)
    
#BFS traversal thru an Adjecency List

def BFSList(AList,v):
    #Accept arguments, adjacency list and a vertex to begin with
    visited = {}
    for i in AList.keys():
        visited[i] = False
    q = Queue()
    visited[v] = True
    q.addq(v)
    while(not q.isempty()):
        j = q.delq()
        for k in AList[j]:
            if (not visited[k]):
                visited[k] = True
                q.addq(k)
    return(visited)

#BFS records distance

def BFSListPathLevel(AList,v):
    (level,parent) = ({},{})
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = Queue()
    level[v] = 0
    q.addq(v)
    while(not q.isempty()):
        j = q.delq()
        for k in AList[j]:
            if (level[k] == -1):
                level[k] = level[j]+1
                parent[k] = j
                q.addq(k)
    return(level,parent)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    