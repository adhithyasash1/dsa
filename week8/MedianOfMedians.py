def MoM(L): # Median of medians
  if len(L) <= 7:
    L.sort()
    return(L[len(L)//2])
  # Construct list of block medians
  M = []
  for i in range(0,len(L),7):
    X = L[i:i+7]
    X.sort()
    M.append(X[len(X)//2])
  return(MoM(M))

def MoM7pos(L):
    x = MoM(L)
    return(sorted(L).index(x))
    
    