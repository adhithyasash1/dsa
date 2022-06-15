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