'''
An Internet service provider company wants to lay fiber lines to connect in cities labeled 0 to n-1. 

Write a function FiberLink(distance_map) that accepts a weighted adjacenty list
distance_map in the following format:-

distance_map = {

                source_index : [(destination_index, distance (km)) ,
                (destination_index, distance) , . .],
                A W

                source_index : [(destination_index, distance),
                (destination_index, distance) , . .]
                
                }

The function returns the minimum length of fiber required to connect all in cities.

Input
    7
    [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
Output
    182
'''

def adjL(dedges):
    edges = dedges + [(j,i,w) for (i,j,w) in dedges]
    print(edges)
    size = 7
    WL = {}
    for i in range(size):
        WL[i] = []
    for (i,j,d) in edges:
        WL[i].append((j,d))
    return (WL)

def primlist(WList):
    infinity = 1 + max([d for u in WList.keys()
                        for (v,d) in WList[u]])
    
    (visited,distance,TreeEdges) = ({},{},[])
    
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)

    visited[0] = True
    
    for (v,d) in WList[0]:
        distance[v] = d
   
    for i in WList.keys():
        (mindist,nextv) = (infinity,None)
        for u in WList.keys():
            for (v,d) in WList[u]:
                if visited[u] and (not visited[v]) and d < mindist:
                    (mindist,nextv,nexte) = (d,v,(u,v))
        
        if nextv is None:
            break
        
        visited[nextv] = True
        
        TreeEdges.append(nexte)        
        
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],d)
    
    return(TreeEdges)

def FiberLink(distance_map):
    ans = primlist(distance_map)
    s = 0
    A = ans
    B = edges
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i][0] == B[j][0] and A[i][1] == B[j][1]:
                s += B[j][2]
            elif A[i][0] == B[j][1] and A[i][1] == B[j][0]:
                s += B[j][2]
    return s


size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))


# Solution 2

def kruskal(WList):
    (edges,component,TE)=([],{},[])
    for u in WList.keys():
        edges.extend([(d,u,v) for (v,d) in WList[u]])
        component[u] = u
    edges.sort()
    for (d,u,v) in edges:
        if component[u] != component[v]:
            TE.append((u,v))
            c = component[u]
        for w in WList.keys():
            if component[w] == c:
                component[w] = component[v]
    return(TE)

def FiberLink(distance_map):
    R = kruskal(distance_map)
    S = 0
    for e in R:
        for ed in distance_map[e[0]]:
            if ed[0]==e[1]:
                S += ed[1]
    return S

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))
