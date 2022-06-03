'''Complexity = O(n^2) for Adjacency Matrix'''

def toposort(AMat):
    rows, cols = AMat.shape
    # empty dictionary to keep track of indegrees
    # empty list to save the order of topologically sorted vertices
    indegree = { }
    toposortlist = [ ]
    
    # first thing to do is compute the indegrees from Adjacency Matrix
    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r, c] == 1:
                indegree[c] += 1            
    
    
    for i in range(rows):
    # i repeat this process for all n vertices in my row
        
        # find all vertices with indegree zero
        # and choose the minimum (you can choose any one of them)
        # in this case to make explanation easy
        # i choose minimum out of all vertices with indegree 0
        j = min([k for k in range(cols) if indegree[k] == 0])
        
        # i append the vertex j to my topologically sorted list
        toposortlist.append(j)
        indegree[j] -= 1
        
        # for every outgoing edge/vertex from j
        # for every k in the column
        # if i have an edge going from j to k
        # i decrease the indegree of k by 1
        for k in range(cols):
            if AMat[j, k] == 1:
                indegree[k] = indegree[k] - 1
    
    return toposortlist


'''Complexity = O(n + m) for Adjacency List'''

def toposortlist(AList):
    # keep an empty dictionary for indegree 
    # and a list for topologically sorted vertices
    indegree, toposortlist = { }, [ ]

    # first i set indegree of all keys in AList to be 0
    # in Alist, keys being my set of vertices and values being the edges 
    for u in AList.keys():
        indegree[u] = 0

    # for every vertex in AList
    # i look at outgoing edges and update their vertex indegrees by 1
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] += 1
    
    # keep track of vertices which has to be enumerated
    # vertices with indegrees zero
    # put them in a queue and enumerate one by one

    # we got thru all vertices in indegree dictionary
    # add a vertex to the queue if its indegree is zero 
    zerodegreeq = Queue()
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)

    # while this queue is not empty :
        # we delete the first element in the queue and enumerate it
        # then update the degrees of outgoing vertices (reduce it by 1)
        # while reducing by 1,
        # if you find any vertex becoming a vertex with indegree 0
        # put the vertex in the queue for enumeration
    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j] -= 1
        for k in AList[j]:
            indegree[k] -= 1
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    
    return toposortlist

