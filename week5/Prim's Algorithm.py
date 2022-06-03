# keep track of the tree that we've built, shortest distance of every vertex,
# distance[v] = distance form every vertex to TV, smallest edge connecting vertex 'v' to the tree   
# order of time complexity : O(n^3)

def primlist(WList):
    # define a large value for variable infinity
    infinity = 1 + max([d for u in WList.keys()
                        for (v,d) in WList[u]])
    (visited,distance,TreeEdges) = ({},{},[])
    for v in WList.keys():
        # initially every vertex is unvisited and infinitely far away from each other
        (visited[v],distance[v]) = (False,infinity)
    # start building MCST from vertex '0' , set it to True
    visited[0] = True
    # for every vertex in the adjacency list of vertex '0'
    # set the distance to that vertex to be the distance of that edge 
    for (v,d) in WList[0]:
        distance[v] = d
    # initialization is over, have set up a tree with source vertex '0'
    # set the distance of all its neighbours and created a tree 

    # calculating minimum distance for loop
    for i in WList.keys():
        (mindist,nextv) = (infinity,None)
        for u in WList.keys():
            for (v,d) in WList[u]:
                # go thru all vertices and its neighbours, check if it is visited
                # if it is visited, then check if its distance is smaller than the current minimum distance
                if visited[u] and (not visited[v]) and d < mindist:
                    (mindist,nextv,nexte) = (d,v,(u,v))
        if nextv is None:
            # case in which if the graph is broken, we exit the loop
            break
        # after we have identified this minimum vertex 'nextv', we set visited to True
        visited[nextv] = True
        # append the newly discovered minimum edge to the result
        TreeEdges.append(nexte)
        # for every neighbour of vertext 'nextv', we repeat the same process of updation
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],d)
    return(TreeEdges)


# Improved Implementation
# instead of keeping track of tree edges with a list, 
# we can keep of track of the neighbours 
# from the neighbours, we can identify the MCST
# improved time complexity of order O(n^2) for Adjacency List
# very very similar to Dijkstra's Algorithm
# Greedy Strategy 

def primlist2(WList):
    infinity = 1 + max([d for u in WList.keys()
                        for (v,d) in WList[u]])
    # instead of tree edges list, we maintain a neighbours dictionary
    (visited,distance,nbr) = ({},{},{})
    # initialization part, where we initialize all the vertices neighbours to be (-1)
    for v in WList.keys():
        (visited[v],distance[v],nbr[v]) = (False,infinity,-1)
    visited[0] = True
    for (v,d) in WList[0]:
        # for every neighbour of the vertex from where we start the algorithm
        # we set its distance from vertex '0' to be d
        # we set its neighbour to be 0 in the neighbour's dictionary (where we came from)
        (distance[v],nbr[v]) = (d,0)
    #initialization part is over, we have created a level 1 MCST from source vertex

    # similar to dijkstra, we repeat this process for all vertices, do the updation if possible 
    for i in range(1,len(WList.keys())):
        # find the minimum distance 
        nextd = min([distance[v] for v in WList.keys()
                     if not visited[v]])
        # find the minimum edge to be added, which connects vertex 'v' and vertext 'nextv'
        nextvlist = [v for v in WList.keys()
                     if (not visited[v]) and
                     distance[v] == nextd]
        # in case the graph is broken
        if nextvlist == []:
            break
        # we do not need to know, how it was connected because it was already connected by its neighbour
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v,d) in WList[nextv]:
            if not visited[v]:
                (distance[v],nbr[v]) = (min(distance[v],d),nextv)
    return(nbr)



