# Edit distance
# Minimum number of editing operations needed to transform one document to the other
# Complexity : O(mn)

def ED(u,v):
    import numpy as np
    (m,n) = (len(u),len(v))
    ed = np.zeros((m+1,n+1))
    for i in range(m-1,-1,-1):
        ed[i,n] = m-i
    for j in range(n-1,-1,-1):
        ed[m,j] = n-j
    for j in range(n-1,-1,-1):
        for i in range(m-1,-1,-1):
            if u[i] == v[j]:
                ed[i,j] = ed[i+1,j+1]
            else:
                ed[i,j] = 1 + min(ed[i+1,j+1], ed[i,j+1], ed[i+1,j])
    return(ed[0,0])

print(ED('bisect','secret'))

