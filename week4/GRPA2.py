'''
tanks = [1, 2, 3, 4, 5, 6, 7]
pipes =[(1, 3),(2, 3),(3, 6),(4, 6),(4, 7),(6, 2),(7, 5),(5, 1),(5, 6)]

tanks = [1, 2, 3, 4]
pipes = [(1, 2), (2, 3), (2, 4)]
'''

def A_List(pipes):
    D = { }
    for i in pipes:
        if i[0] not in D.keys():
            D[i[0]] = [i[1]]
        else:
            D[i[0]].append(i[1])
    return D 

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
        if k in visited.keys():
            if (not visited[k]):
                parent[k] = v
                (visited,parent) = DFSList(AList,visited,parent,k)                
    return(visited,parent)

def check(x):
    flag = 0
    for key, values in x.items():
        if x[key] == True:
            pass
        elif x[key] == False:
            flag = 1
    if flag == 1:
        return False
    else:
        return True

def findMasterTank(tanks, pipes):
    AList = A_List(pipes)
    tankS = [int(i) for i in tanks]
    for i in tankS:
        visited, parent = DFSInitList(AList)
        visited, parent = (DFSList(AList,visited,parent,i))
        if check(visited):
            return i
    return 0



'''
def DFSInitGlobal(Alist):
    visited = {}
    for i in Alist.keys():
        visited[i] = False
    return visited

def DFSGlobal(Alist,visited,v):
    visited[v] = True
    for k in Alist[v]:
        if not visited[k]:
            DFSGlobal(Alist,visited,k)
    return visited
      
      
def findMasterTank(v, e):
    n = len(v)
    Alist = {}
    for i in range(int(v[0]),int(v[-1])+1):
        Alist[i] = []
    for (i,j) in e:
        Alist[int(i)].append(int(j))
    DFSInitGlobal(Alist)
    for i in Alist.keys():
        visited = DFSGlobal(Alist,DFSInitGlobal(Alist),i)
        Flag = True
        for k in visited.keys():
            if visited[k] != True:
                Flag = False
                break
        if Flag:
            return i
    return 0
'''
        
        
        
    
    
































