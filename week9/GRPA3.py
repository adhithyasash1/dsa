'''
Longest Decreasing Sequence (LDS) is in which the values gets strictly decreasing over the sequence. 

For example :
	in [5, 4, 7, 1], 

		[5, 4, 1] is a longest decreasing sequence

Write a function LDS(L) to return a list of longest decreasing sequence. If more than one LDS is present in the list L then return any one of LDS. 
'''

# Solution 1

def LDS(L):
    n = len(L)
    
    # LDS with respect to the index
    LDSCount = [1]*n 

    # Previous value with respect to the index
    prev = [None]*n 
    
    for i in range(n):
        preMax = L[0]
        for j in range(i):
            if L[j] > L[i] and LDSCount[j] > preMax:
                preMax, prev[i] = LDSCount[j], j
        LDSCount[i] = 1 + preMax # Updating LDSCount
    
    # Count of LDS
    mx = max(LDSCount)
    
    # Index of LDS
    mxi = LDSCount.index(mx) 
    
    # Backtracking to get the sequence
    seq = []
    while mxi != None:
        seq.append(L[mxi])
        mxi = prev[mxi]
    return seq[::-1]


 # Solution 2

 def LDS(L):
    if not L:
        return
    
    LDS = [[] for _ in range(len(L))]
    
    LDS[0].append(L[0])
    for i in range(1, len(L)):
        for j in range(i):
            if L[j] > L[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j].copy()
        LDS[i].append(L[i])
    
    j = 0
    for i in range(len(L)):
        if len(LDS[j]) < len(LDS[i]):
            j = i

    return LDS[j]


'''
Input
	47 20 46 96 44 58 29 12 2 86
Output
	True 6

Input
	6 33 4 97 33 100 10 53 39 53 56 96 2 57 9 96 36 100 98 72
Output
	True 4
'''