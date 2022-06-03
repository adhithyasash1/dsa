'''Component Connectivity can be checked thru both BFS and DFS traversals,
in here we are using BFS traversal to perform component connectivity'''

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

def Component(AList):
	component = { }
	for i in AList.keys():
		component[i] = -1

	comp_id, seen = 0, 0

	while seen <= max(AList.keys()):
		start_vertex = min([i for i in AList.keys() if component[i] == -1])
		visited = BFS(AList, start_vertex)
		for i in visited.keys():
			if visited[i]:
				seen += 1
				component[i] = comp_id
		comp_id += 1
	return component	
