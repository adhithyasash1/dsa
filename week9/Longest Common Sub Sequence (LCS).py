# Longest Common Sub Sequence (LCS)
# Subsequence – can drop some  letters in between 
# Complexity : O(mn)

def LCS(s1,s2):
    import numpy as np
    (m,n) = (len(s1),len(s2))
    lcs = np.zeros((m+1,n+1))
    for c in range(n-1,-1,-1):
        for r in range(m-1,-1,-1):
            if s1[r] == s2[c]:
                lcs[r,c] = 1 + lcs[r+1,c+1]
            else:
                lcs[r,c] = max(lcs[r+1,c], lcs[r,c+1])                
    return lcs[0,0]

s1 = 'secret'
s2 = 'bisect'
print(LCS(s1,s2))