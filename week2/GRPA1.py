def combinationSort(L):
    L1 = [ ]
    for i in L:
        L1.append((i[0], i[1:]))
    L2 = sorted(L1, key = lambda x: x[0])
    L1= [ ]
    L1 = [i[0] + i[1] for i in L2]
    L3 = sorted(L1, key = lambda x: int(x[1:]), reverse = True)
    L4 = sorted(L3, key = lambda x: x[0])
    return L1, L4