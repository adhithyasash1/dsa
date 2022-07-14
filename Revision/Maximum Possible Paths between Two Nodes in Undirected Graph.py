'''
Write a function backandforth(AList, end1, end2) to return the maximum number of possible
route between node end1 and node end2 in the undirected graph without going through the
same node again with exception to end1 and end2 . The connectivity details between nodes are
provided by the adjacency list AList .
'''

# Prefix

def BFSListPath(AList, v, preventionList=[]):
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

# Solution

def findpath(parent, start, end):
	L = []
	curr = parent[end]
	while curr != start:
		L.append(curr)
		curr = parent[curr]
	return L

def backandforth(AList, start, end):
	preventionList = []
	visited, parent = BFSListPath(AList, start, preventionList)
	c = 0
	while visited[end]:
		c += 1
		path = findpath(parent, start, end)
		preventionList.extend(path)
		visited, parent = BFSListPath(AList, start, preventionList)
	return c

# Suffix

start = int(input())
end = int(input())
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

print(backandforth(AList, start, end))


'''
Input
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

Output
	3
	Explanation
		The possible paths are [0, 3, 1], [1, 6, 0] and [0, 2, 4, 5, 1]. Hence the answer is 3.
'''


















