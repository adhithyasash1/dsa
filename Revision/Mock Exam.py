'''
Write a function backandforth(AList, end1, end2) to return the maximum number of possible
route between node end1 and node end2 in the undirected graph without going through the
same node again with exception to end1 and end2 . The connectivity details between nodes are
provided by the adjacency list AList.

Sample Input

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

Sample Output
	3
	The possible paths are [0, 3, 1], [1, 6, 0] and [0, 2, 4, 5, 1]. Hence the answer is 3.

'''

# Prefix (visible)
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

# suffix (invisible)
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
Write a function MaxValueSelection(items, C) that accepts a dictionary items where each key
of the dictionary represents the item name and the corresponding value is a tuple (number of
units, value of all units) and function accept one more variable C which represents the
maximum capacity of units you can select from all items to get maximum value.

Sample Input
	{1:(10,60),2:(20,100),3:(30,120)}
	50

Sample Output
	240
'''

def maxValueSelection(items, c):
	total_value = 0
	for i in sorted(items, key=lambda x:items[x][1]/items[x][0], reverse=True):
		if items[i][0] <= c:
			total_value += items[i][1]
			c -= items[i][0]
		else:
			total_value += items[i][1]/items[i][0] * c
			c = 0
	return total_value


'''
Swapping Min-max
You are given two lists a and b of n positive integers each. You can apply the following swap
operation to them any number of times:
Select an index and swap with (i.e. becomes and vice versa).

Write a function minmax(a,b) which takes two lists and of size n as inputs and returns an
integer, which is the minimum possible value of max(a1,a2,...,an)*max(b1,b2,...,bn)
you can get after applying the swap operation any number of times (possibly zero).

Sample Input
	[1,2,6,5,1,2]
	[3,4,3,2,2,5]

Sample Output
	18
'''

def minmax(a,b):
	for i in range(len(a)):
		if a[i]<b[i]:
			(a[i],b[i]) = (b[i],a[i])
	return(max(a)*max(b))

'''
Shortest Circular Route
A traveler made a travel plan which starts from city S . Due to time limitations, he decided to
choose the shortest circular route that returns to the starting city S without using any road twice
in the route. The route need not visit all cities.

Write a Function shortestCircularRoute(WList, S) that accepts a weighted adjacency list WList
for the connected two-way road network of n cities, labeled 0 to n-1 and another parameter S
which represents the start city. The function returns the total distance of the shortest circular
route from city S .

Note: You are guaranteed that there is always at least one circular route.

Hint: Observe that a circular route from S consists of a road from S to a neighbour U followed by
a path back from U to S that does not use the road (U, S).

Format of WList: 
	 {
	source_index : [(destination_index,distance),
	(destination_index,distance),..],
	..
	..
	source_index : [(destination_index,distance),
	(destination_index,distance),..]
	}

Sample Input
	6 #n- number of nodes(cities) labeled 0 to 5
	[(2,0,11),(5,0,12),(5,3,52),(5,1,17),(4,1,14),(3,4,13),(2,3,10)] # edges
	(roads between city with distance)
	0 #S source index (start city)

Sample Output
	77 #total distance of Shortest circular route 0 - 2 - 3 - 4 - 1 - 5 - 0
'''

import copy
def dijkstra(WList,s):
	infinity = 1 + len(WList.keys())*max([d for u in WList.keys()for (v,d) in WList[u]])
	(visited,distance) = ({},{})
	for v in WList.keys():
		(visited[v],distance[v]) = (False,infinity)
	distance[s] = 0
	for u in WList.keys():
		nextd = min([distance[v] for v in WList.keys() if not visited[v]])
		nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
		if nextvlist == []:
			break
		nextv = min(nextvlist)
		visited[nextv] = True
		for (v,d) in WList[nextv]:
			if not visited[v]:
				if distance[v] > distance[nextv] + d:
					distance[v] = distance[nextv] + d
	return(distance)

def shortestCircularRoute(WList,s):
	pathweight=[]
	adj = []
	for node in WList[s]:
		adj.append(node)
	for each_adj in adj:
		wl = copy.deepcopy(WList)
		wl[s].remove(each_adj)
		wl[each_adj[0]].remove((s,each_adj[1]))
		d = dijkstra(wl,each_adj[0])
		pathweight.append(each_adj[1]+ d[s])
	return(min(pathweight))

