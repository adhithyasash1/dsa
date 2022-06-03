def bellmanford(WMat,s):
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat)*rows + 1
    distance = { }
    for v in range(rows):
        distance[v] = infinity
    distance[s] = 0
    for i in range(rows):
        # we do this process of running for loops for u, v: 'n' times
        # hence the outer for loop 'i' runs for a range of total number of rows 
        for u in range(rows):
            for v in range(cols):
                if WMat[u, v, 0] == 1:
                    # for vertices u, v: if u-v is an edge
                    distance[v] = min(distance[v], distance[u]
                                      +WMat[u, v, 1])
                    # we update the distance of v to be the minimum of 
                    # (existing distance) or 
                    # (distance of the starting point of the edge and the weight of the edge.)  
    return(distance)


# the order of complexity reduces to order(m)
# m = no. of edges for a given vertex via adjacency list (dictionary data structure)
# overal complexity is order(mn) since we run this order(m)- 'n' times

def bellmanfordlist(WList,s):
    infinity = 1 + len(WList.keys())*
                    max([d for u in WList.keys()
                         for (v,d) in WList[u]])
    distance = { }
    for v in WList.keys():
        distance[v] = infinity
    distance[s] = 0
    for i in WList.keys():
        for u in WList.keys():
            # since we aren't going to look for any other vertices which does not have an edge
            # adjacency list only gives us vertices which has a direct edge
            for (v,d) in WList[u]:
                distance[v] = min(distance[v],distance[u] + d)
    return(distance)
    





