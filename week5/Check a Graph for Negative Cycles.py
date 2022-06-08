def convert_WeightedAdjacencyList(l):
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

def check_WhetherNodesAre_Connected(D):
    for key in D.keys():
        if D[key] == []:
            return False
    return True

def nth_iteration_of_BellmanFord(edges):
    WL = {}
    for i in range(size):
        WL[i] = []
    for (i,j,d) in edges:
        WL[i].append((j,d))
    return WL

def n_plus_one_iteration_of_BellmanFord(edges):
    WL = {}
    for i in range(size+1):
        WL[i] = []
    for (i,j,d) in edges:
        WL[i].append((j,d))
    return WL
    
def bellmanford(WList,s):
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
    Weighted_AList1 = nth_iteration_of_BellmanFord(edges)
    Dictionary_A = bellmanford(Weighted_AList1,0)
    
    Weighted_AList2 = n_plus_one_iteration_of_BellmanFord(edges)
    Dictionary_B = bellmanford(Weighted_AList2,0)
    
    Weighted_AList = nth_iteration_of_BellmanFord(edges)
    AList = convert_WeightedAdjacencyList(Weighted_AList)
    if not check_WhetherNodesAre_Connected(AList):
        return False
    else:
        for i in range(len(WL)):
            if Dictionary_A[i] != Dictionary_B[i]:
                return True
        return False
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))