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
# Print number of connected components for undirected graph. This method will not work for directed graphs.

def findComponents_undirectedGraph(vertices, edges):
    # Create a adjacency list for graph.
    GList = {}
    for i in vertices:
        GList[i]=[]
    for (i,j) in edges:
        GList[i].append(j)
        GList[j].append(i)
    # Mark every vertex not visited.
    visited = {v:False for v in vertices}
    q = myQueue()
    componentsCount = 0
    # 1. Select some vertex v
    # 2. Start traversing the graph from v, till all vertices are visited in this component. Increment component count.
    # 3. Search for any unvisited vertex v, go to step 2
    for v in vertices:
        if not visited[v]:
            q.enQueue(v)
            while not q.isEmpty():
                v = q.deQueue()
                if not visited[v]:
                    for i in GList[v]:
                        if(not visited[i]):
                            q.enQueue(i)
                    visited[v]=True
            componentsCount += 1
    return componentsCount


'''suffix

v = [item for item in input().split(" ")]
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
s = input().split(" ")
e.append((s[0], s[1]))
print(findComponents_undirectedGraph(v, e))

'''