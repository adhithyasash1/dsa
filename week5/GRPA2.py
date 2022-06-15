#1

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


#2

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