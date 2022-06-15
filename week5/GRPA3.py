def fun(l):
    WL = {}
    for i in range(size):
        WL[i] = []
    for (i,j,d) in edges:
        WL[i].append((j,d))
        
    D = { }
    for key in WL.keys():
        D[key] = [ ]
    for key, values in WL.items():
        for i in range(len(WL[key])):
            D[key].append(values[i][0])
    return D

def check(D):
    for key in D.keys():
        if D[key] == []:
            return False
    return True

def BA(edges):
    WL = {}
    for i in range(size):
        WL[i] = []
    for (i,j,d) in edges:
        WL[i].append((j,d))
    return WL

def BB(edges):
    WL = {}
    for i in range(size+1):
        WL[i] = []
    for (i,j,d) in edges:
        WL[i].append((j,d))
    return WL
    
def bellmanfordlist(WList,s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
        
    distance[s] = 0
    
    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v] = min(distance[v], distance[u] + d)
    return(distance)

def IsNegativeWeightCyclePresent(WL):
    WL1 = BA(edges)
    DA = bellmanfordlist(WL1,0)
    
    WL2 = BB(edges)
    DB = bellmanfordlist(WL2,0)
    
    Weighted_AList = BA(edges)
    AList = fun(Weighted_AList)
    if not check(AList):
        return False
    else:
        for i in range(len(WL)):
            if DA[i] != DB[i]:
                return True
        return False