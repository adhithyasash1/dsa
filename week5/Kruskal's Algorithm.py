
def kruskal(WList):
    # keep track of edges in our tree [TE]
    # keep track of edges in order to process
    # keep track of components of the graph
    (edges,component,TE) = ([],{},[])
    # (d, u, v) = weight, vertex 'u' to vertex 'v'
    # sort the edges according to weight
    # process the adjacency list
    # for every edge v-d in the adjacency list of vertex 'u' 
    for u in WList.keys():
        # weight as first component to sort easily
        edges.extend([(d,u,v) for (v,d) in WList[u]])
        component[u] = u
    edges.sort()
    # while processing the list, we keep track of the components, each vertex belong to
    # when we merge two components, we keep the name of one component
    for (d,u,v) in edges:
        if component[u] != component[v]:
            TE.append((u,v))
            c = component[u]
            for w in WList.keys():
                if component[w] == c:
                    component[w] = component[v]
    return(TE)

# sorting is O(mlogm) complexity
# outer loop runs for 'm' times
# inner loop runs for (n-1) times
# total time complexity is O(n^2)
# to improve this algorithm, 
# later we will learn how to use union-find operation 
# to reduce the complexity to O(mlogm) from O(n^2)
# kruskal's algorithm gives the same answer as prim, if the graph has unique set of edges
# if edge weights repeat, then this is no longer true


















