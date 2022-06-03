''' DFS thru Adjacency Matrix not declaring Global Variables '''

def DFSInit(AMat):
    # Initialization
    (rows,cols) = AMat.shape
    (visited,parent) = ({},{})
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return(visited,parent)

def DFS(AMat,visited,parent,v):
    visited[v] = True
    for k in neighbours(AMat,v):
        if (not visited[k]):
            parent[k] = v
            (visited,parent) = DFS(AMat,visited,parent,k)
    return(visited,parent)

''' DFS thru Adjacency Matrix declaring Global Variables '''

(visited,parent) = ({},{})

def DFSInitGlobal(AMat):
    # Initialization
    (rows,cols) = AMat.shape
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return

def DFSGlobal(AMat,v):
    visited[v] = True
    for k in neighbours(AMat,v):
        if (not visited[k]):
            parent[k] = v
            DFSGlobal(AMat,k)
    return

''' DFS thru Adjacency List not declaring Global Variables '''

def DFSInitList(AList):
    # Initialization
    (visited,parent) = ({},{})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return(visited,parent)

def DFSList(AList,visited,parent,v):
    visited[v] = True
    for k in AList[v]:
        if (not visited[k]):
            parent[k] = v
            (visited,parent) = DFSList(AList,visited,parent,k)
    return(visited,parent)

''' DFS thru Adjacency List  declaring Global Variables '''

(visited,parent) = ({},{})

def DFSInitListGlobal(AList):
    # Initialization
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return

def DFSListGlobal(AList,v):
    visited[v] = True
    for k in AList[v]:
        if (not visited[k]):
            parent[k] = v
            DFSListGlobal(AList,k)
    return









