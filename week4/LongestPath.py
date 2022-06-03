'''
calculating longest path to reach vertex i is 
being done thru the dictionary longest_path
in which the keys are vertices and values are the
longest path to reach them

while doing topological sort, we keep track of indegree
and longest path, and finally while returning the topological
list, we instead return longest_path

longest path is the minimum time taken to complete all
tasks including their dependencies

longest path = diameter of a graph

in DAGS it is easy to calculate longest path, but in
general graphs it becomes a hard problem to solve
'''

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


def longestpath(AList):
	indegree, longest_path = { }, { }

	for u in AList.keys():
		indegree[u], longest_path[u] = 0, 0

	for u in AList.keys():
		for v in AList[u]:
			indegree[v] += 1

	zerodegreeq = Queue()
	for u in AList.keys():
		if indegree[u] == 0:
			zerodegreeq.addq(u)

	while not zerodegreeq.isempty():
		j = zerodegreeq.delq()
		indegree[j] -= 1
		for k in AList[j]:
			indegree[k] -= 1
			longest_path[k] = max(longest_path[k], (longest_path[j] + 1))
			if indegree[k] == 0:
				zerodegreeq.addq(k)

	return longest_path


