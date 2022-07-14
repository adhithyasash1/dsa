'''
Matrix Multiplication

a) Matrix multiplication is associative 
b) Bracketing does not change answer but can affect the complexity 
c) Find an optimal order to compute the product 

Complexity : O(n^3)
'''


# Implementation 1

def MM(dim):
    n = dim.shape[0]
    C = np.zeros((n,n))
    for i in range(n):
        C[i,i] = 0
    for diff in range(1,n):
        for i in range(0,n-diff):
            j = i + diff
            C[i,j] = C[i,i] + C[i+1,j] + dim[i][0] * dim[i+1][0] * dim[j][1]
            print(C)
            for k in range(i+1, j+1):
                C[i,j] = min(C[i,j],C[i,k-1] + C[k,j] + dim[i][0] * dim[k][0] * dim[j][1])
            print(C)
    return(C[0,n-1])

import numpy as np
a = np.array([[2,3],[3,4],[4,5]])
print(MM(a))

# Implementation 2

def MM(dim):
    n = len(dim)
    C = []
    for i in range(n):
        L = []
        L=[0]*n
        C.append(L.copy())        
    for diff in range(1,n):
        for i in range(0,n-diff):
            j = i + diff
            KL = []
            for k in range(i, j):
                KL.append(C[i][k] + C[k+1][j] + dim[i][0] * dim[k][1] * dim[j][1])
            C[i][j] = min(KL)
    return(C[0][n-1])

a = [[4,10],[10,3],[3,12],[12,20],[20,7]]
print(MM(a))



