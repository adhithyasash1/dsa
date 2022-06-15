'''
Shortest Path

The express train routes are provided in the adjacency list AList , here you have to find the route
from start to end with minimum number of possible. Write a function minimumhops(AList,
start, end) to return the cities to be visited starting from start to end . Return a list with only
start if the end is not reachable.

Example : 

    input :
        start = 8
        end = 7
        AList = {
                0: [8],
                8: [0, 9],
                1: [3, 5, 8],
                3: [1, 7, 2],
                5: [4],
                2: [8, 9],
                9: [1],
                7: [8],
                4: [2, 6],
                6: [9]
                }

    output :
        [8, 9, 1, 3, 7]
'''

def BFSListPathLevel(AList, v):
    level, parent = {}, {}
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = []
    
    level[v] = 0
    q.append(v)
    
    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if level[k] == -1:
                level[k] = level[j]+1
                parent[k] = j
                q.append(k)
    return level, parent

def minimumhops(AList, start, end):
    level, path = BFSListPathLevel(AList, start)
    shortestpath = []
    if level[end] != -1:
        shortestpath.append(end)
        while shortestpath[-1] != start:
            end = path[end]
            shortestpath.append(end)
    else:
        shortestpath.append(start)
    return shortestpath[::-1]

# Suffix
start = int(input())
end = int(input())
AList = eval(input())
shortestpath = minimumhops(AList, start, end)
print(shortestpath)

'''
Back and Forth

Write a function backandforth(AList, end1, end2) to return the maximum number of possible
route between node end1 and node end2 in the undirected graph without going through the
same node again with exception to end1 and end2 . The connectivity details between nodes are
provided by the adjacency list AList.

Example :

    input :
            AList = {
                0: [2, 3, 6],
                2: [0, 3, 4],
                3: [4, 2, 0, 1],
                6: [1, 5, 0],
                1: [3, 6, 5],
                4: [2, 3, 5],
                5: [1, 4, 6]
                }
            end1 = 0
            end2 = 1

    output :
        3
'''
def BFSListPath(AList, v, preventionList):
    visited, parent = {}, {}
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    q = []
    
    visited[v] = True
    q.append(v)
    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if not visited[k] and not k in preventionList:
                visited[k] = True
                parent[k] = j
                q.append(k)
    return visited, parent

def findpath(parent, start, end):
    L = []
    curr = parent[end]
    while curr != start:
        L.append(curr)
        curr = parent[curr]
    return L

def backandforth(AList, end1, end2):
    preventionList = []
    c = 0
    visited, parent = BFSListPath(AList, end1, preventionList)
    while visited[end2]:
        c += 1
        path = findpath(parent, end1, end2)
        preventionList.extend(path)
        visited, parent = BFSListPath(AList, end1, preventionList)
    return c

# Suffix
end1 = int(input())
end2 = int(input())
AList = {}
while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
            AList[u].append(v)

print(backandforth(AList, end1, end2))

'''
Cool Worker

A group of workers have to complete a list of tasks, those tasks have dependencies within the task
list. But the workers prefer some interesting task and hates to do some boring task. They always
do the most interesting one among the available tasks to be done.

Write a function coolWorkers(AList, preference) to return the order in which the tasks will be
done. AList is the adjacency list with the dependencies and preference is the tasks sorted in
preferred order, in which task in index 0 is the most preferred and index -1 (last element) be the
least preferred.

Example :

    input :
        AList = {0: [1, 2, 3],
                1: [7],
                2: [3, 5],
                3: [4, 1, 8],
                7: [],
                5: [6, 1],
                4: [5, 7],
                8: [5],
                6: [7]}
        preference = [1, 3, 2, 6, 8, 5, 4, 0, 7]

    output :
        [0, 2, 3, 8, 4, 5, 1, 6, 7]
'''

# Dictionary inversion for d which has list as values
def dInv(d):
    d_ = {}
    if not isinstance(list(d.values())[0], list):
        for k, v in d.items():
            if v not in d_:
                d_[v] = []
            d_[v].append(k)
        return d_
    
    if isinstance(list(d.values())[0], list):
        for k, v in d.items():
            for v_ in v:
                if v_ not in d_:
                    d_[v_] = []
                d_[v_].append(k)
        return d_

def coolWorkers(AList, preference):
    n = len(AList.keys())
    indegree = {}
    toposortlist = []
    
    IAList = dInv(AList)
    for i in AList.keys():
        if i not in IAList:
            IAList[i] = []
        indegree[i] = len(IAList[i])
    
    for i in range(n):
        availableTasks = [k for k in AList if indegree[k] == 0]
        t = [(preference.index(i), i) for i in availableTasks]
        t.sort()
        j = t[0][1]
        toposortlist.append(j)
        indegree[j] = indegree[j]-1
        for k in AList[j]:
            indegree[k] -= 1
    return toposortlist

# Suffix
AList = eval(input())
preference = eval(input())
print(coolWorkers(AList, preference))


'''
Complete the Python function findAllPaths to find all possible paths from the source vertex to
destination vertex in a directed graph.
Function findAllPaths(vertices, gList, source, destination) takes vertices as a list of vertices,
gList a dictionary that is an adjacency List representation of graph edges, source vertex,
destination vertex, and returns a list of all paths from source to destination . The return
value will be a List of Lists, where every path is a sequence of vertices as a List. Return an empty
list if no path exists from 'source' to 'destination'.

Example : 
    input : 
        vertices: [1, 2, 3, 4, 5, 6, 7, 8],
        gList: {1:[3,4], 2:[3], 3:[6], 4:[6,7], 5:[4,6], 6:[2], 7:[5]},
        source: 1
        destination: 2
    output : 
        [[1, 3, 6, 2], [1, 4, 6, 2], [1, 4, 7, 5, 6, 2]]
'''

# Helper functions
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

# Function
def findAllPaths(vertices, gList, source , destination):
    allPaths = []
    path = []
    visited = {v:False for v in vertices}
    findAllPathsRecursive(vertices, gList, source, destination, visited, path, allPaths)
    return allPaths

# Function that will be called recursively to find path from original source to destination, that passes through vertex 'src'.
# If a path is found add it o allPaths.
def findAllPathsRecursive(vertices, gList, src, dest, visited, path, allPaths):
    visited[src] = True
    path.append(src)
    if (src == dest):
        allPaths.append(path.copy())
    for e in gList[src]:
        if not visited[e]:
            findAllPathsRecursive(vertices, gList, e, dest, visited, path, allPaths)
    
    # If no path exist passing through this vertex remove it from path.
    # Mark it unvisited, this vertex could be part of some other path.
    path.pop()
    visited[src]=False

# Suffix 
#Vertices are expected to be labelled as single letter or single digit
#Sort and arrange the result for uniformity
def ArrangeResult(result):
    res = []
    for item in result:
        s = ""
        for i in item:
            s += str(i)
        res.append(s)
    res.sort()
    return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
    Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))