'''
Write a Function min_cost_walk(WList, S, D, V) that accepts a weighted adjacenty list WList for
a undirected and connected graph. The function returns the minimum cost and walk route in the
format (minimum_cost, [walk_route]) from node S to node D, via node V (S -> V -> D),
where the cost of a walk is the sum of weights of edges encountered on the route.

Note:- Node can be repeat in path.

Input
    7
    [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
    0
    4
    3    
Output
    (110, [0, 1, 3, 4])
'''

# Solution 1

def path(prev, s, t):
    p = []
    dest = s
    while dest != t:
        p += [dest]
        dest = min([j for i,j in prev.items() if i == dest])
    return p

def min_cost_walk(WList, s, e, t):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()
                           for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)
    
    distance[t] = 0
    prev = {}
    
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys()
                        if not visited[v]])
        nextvlist = [v for v in WList.keys()
                        if (not visited[v]) and
                            distance[v] == nextd]

        if visited[s] and visited[e]:
            break

        nextv = min(nextvlist)
        visited[nextv] = True       
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],distance[nextv]+d)
                if distance[v] == distance [nextv] + d:
                    prev[v] = nextv
    #dest = s
    #while dest != t:
     #   p += [dest]
     #   dest = min([j for i,j in prev.items() if i == dest])
    return(distance[s] + distance [e], path(prev, s, t) +[t]+ path(prev,e,t)[::-1])


#Solution 2

def bellmanford(WList,s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    distance = {}
    prev = {}
    for v in WList.keys():
        distance[v] = infinity
        prev[v] = None
    distance[s] = 0
    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                if distance[v] > distance[u] + d:
                    distance[v] = distance[u] + d
                    prev[v] = u
    return (distance,prev)
def min_cost_walk(route_map,source,destination,via):
    distance1,path1 = bellmanford(route_map, source)
    distance2,path2 = bellmanford(route_map, via)
    tot_dist = distance1[via]+distance2[destination]
    Route_S_D = []
    # shortest route for source to via
    if distance2[destination] != 0:
        dest = destination
        while dest != via:
            Route_S_D = [dest] + Route_S_D
            for k,l in path2.items():
                if dest == k:
                    dest = l
                    break
        Route_S_D = Route_S_D
    # shortest route for via to destination
    if distance1[via] != 0:
        dest = via
        while dest != source:
            Route_S_D = [dest] + Route_S_D
            for i,j in path1.items():
                if dest == i:
                    dest = j
                    break
        Route_S_D = [dest] + Route_S_D

    return (tot_dist,Route_S_D)

# Solution 3

def dijkstra(WList,s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()for (v,d) in WList[u]])
    (visited,distance,prev) = ({},{},{})
    for v in WList.keys():
        (visited[v],distance[v],prev[v]) = (False,infinity,None)       
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
                if distance[v] > distance[nextv]+d:
                    distance[v] = distance[nextv]+d
                    prev[v] = nextv    
    return(distance,prev)


def min_cost_walk(WList,S, D, V):
    distance1,path1 = dijkstra(WList, S)
    distance2,path2 = dijkstra(WList, V)
    tot_dist = distance1[V] + distance2[D]
    Route_S_V = []
    Route_V_D = []
    # shortest route for S to V
    if distance1[V] != 0:
        dest = V
        while dest != S:
            Route_S_V = [dest] + Route_S_V
            for i,j in path1.items():
                if dest == i:
                    dest = j
                    break
        Route_S_V = [dest] + Route_S_V
    # shortest route for V to D
    if distance2[D] != 0:
        dest = D
        while dest != V:
            Route_V_D = [dest] + Route_V_D
            for i,j in path2.items():
                if dest == i:
                    dest = j
                    break
        Route_V_D = [dest] + Route_V_D
    Route_S_D = Route_S_V[:-1]+ Route_V_D
    return (tot_dist,Route_S_D)

size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))
