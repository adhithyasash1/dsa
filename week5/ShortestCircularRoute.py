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