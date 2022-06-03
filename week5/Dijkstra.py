'''Implementation of Dijkstra using a 
Weighted Adjacency Matrix
 starting at vertex 's'

 Complexity = O(n^2)
'''

def dijkstra(WMat,s):
    (rows,cols,x) = WMat.shape
    # (i,j,0) means there is no edge from i to j
    # (i,j,1) means tehre is an edge from i to j
    infinity = np.max(WMat)*rows+1
    # setting some large value for infinity unachievable by the graph
    (visited,distance) = ({},{})
    # initialize two empty dictionaries, visited and distance
    for v in range(rows):
        (visited[v],distance[v]) = (False,infinity)
    # set all vertices in visited to false
    # set all vertices distance to infinity
    distance[s] = 0
    # initialize the distance of the source vertex to 0

    # find minimum distance that is present
    # explore that vertex
    # find which are all the vertices that are not visited and have that minimum distance
    for u in range(rows):
        nextd = min([distance[v] for v in range(rows)
                     if not visited[v]])
        nextvlist = [v for v in range(rows)
                     if (not visited[v]) and
                     distance[v] == nextd]

    # there can be vertices which are not visited forever
    # boundary condition
    if nextvlist == []:
        break

    # choose any one of the vertices with minimum distance
    nextv = min(nextvlist)
    visited[nextv] = True

    # look at all its outgoing edges and update their distance
    # update the distance to be the current vertex or distance it took to reach that vertex + current distance
    for v in range(cols):
        if WMat[nextv,v,0] == 1 and (not visited[v]):
            distance[v] = min(distance[v],distance[nextv]
                              +WMat[nextv,v,1])
    return(distance)


'''Implementation of Dijkstra using a 
Weighted Adjacency List
 starting at vertex 's'

 Complexity = O(n^2)
'''

def dijkstralist(WList,s):

    # set infinity to be some large value
    infinity = 1 + len(WList.keys()) * 
                max([d for u in WList.keys() 
                     for (v,d) in WList[u]])
    # initialize the dictionaries
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)

    # mark distance to reach source vertex as 0
    distance[s] = 0

    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys()
                     if not visited[v]])
        nextvlist = [v for v in WList.keys()
                     if (not visited[v]) and
                     distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],distance[nextv]+d)
    return(distance)



def dijkstra(WMat, s):
    rows, cols, x = WMat.shape
    infinity = np.max(WMat) * rows + 1
    visited, distance, parent = {}, {}, {}
    for v in range(rows):
        visited[v], distance[v], parent[v] = False, infinity, None

    distance[s] = 0

    for u in range(rows):
        nextd = min([distance[v] for v in range(rows) if not visited[v]])
        nextvlist = [v for v in range(rows) if (not visited[v]) and distance[v] == nextd]

        if nextvlist == [ ]:
            break

        nextv = min(nextvlist)
        visited[nextv] = True
        for v in range(cols):
            if WMat[nextv, v][0] == 1 and (not visited[v]):
                if distance[nextv] + WMat[nextv, v][1] < distance[v]:
                    parent[v] = nextv
                    distance[v] = distance[nextv] + WMat[nextv, v][1]

    return distance, parent













