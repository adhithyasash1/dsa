# Longest Common Sub Word (LCW) 
# Given two strings, find the (length  of the) longest common sub word 
# Complexity : O(mn)

def LCW(s1,s2):
    import numpy as np
    (m,n) = (len(s1),len(s2))
    lcw = np.zeros((m+1,n+1))
    maxw = 0
    for c in range(n-1,-1,-1):
        for r in range(m-1,-1,-1):
            if s1[r] == s2[c]:
                lcw[r,c] = 1 + lcw[r+1,c+1]
            else:
                lcw[r,c] = 0
            if lcw[r,c] > maxw:
                maxw = lcw[r,c]                
    return maxw

s1 = 'bisect'
s2 = 'secret'
print(LCW(s1,s2))


