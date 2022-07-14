'''
Quick select and Fast select

1) Find the  smallest value in a sequence of length k   

2) Sort in descending order and look at position k - O(nlogn)

3) For any fixed k, find maximum for k times – O(kn)

4) k = n/2, (median) – O(n^2)

5) Median of medians – O(n)

6) Selection becomes O(n) in Fast select algorithm 

7) Quicksort becomes O(nlogn) using MoM

'''

def quickselect(L,l,r,k): # k-th smallest in L[l:r]
  if (k < 1) or (k > r-l):
    return(None)

  (pivot,lower,upper) = (L[l],l+1,l+1)
  for i in range(l+1,r):
    if L[i] > pivot:  # Extend upper segment
      upper = upper + 1
    else: # Exchange L[i] with start of upper segment
      (L[i], L[lower]) = (L[lower], L[i])
      (lower,upper) = (lower+1,upper+1)
  (L[l],L[lower-1]) = (L[lower-1],L[l]) # Move pivot
  lower = lower - 1

  # Recursive calls
  lowerlen = lower - l
  if k <= lowerlen:
    return(quickselect(L,l,lower,k))
  elif k == (lowerlen + 1):
    return(L[lower])
  else:
    return(quickselect(L,lower+1,r,k-(lowerlen+1)))
    
print(quickselect([5,3,7,2,1],0,5,2))

'''
Median of Medians(MoM)

1) Divide L into blocks of 5 

2) Find the median of each block (brute force) 

3) Let M be the list of block medians 

4) Recursively apply the process to M 

5) We can visualize the blocks as follows

6) Each block of 5 is arranged in ascending order, top to bottom 

7) Block medians are the middle row

8) The median of block medians lies between 3len(L)/10 and 7len(L)/10

'''

def MoM(L): # Median of medians
  if len(L) <= 5:
    L.sort()
    return(L[len(L)//2])
  # Construct list of block medians
  M = []
  for i in range(0,len(L),5):
    X = L[i:i+5]
    X.sort()
    M.append(X[len(X)//2])
  return(MoM(M))
print(MoM([4,3,5,6,2,1,8,9,7,10,13,15,18,17,11]))

'''
Fast Select 

'''

def MoM(L): # Median of medians
  if len(L) <= 5:
    L.sort()
    return(L[len(L)//2])
  # Construct list of block medians
  M = []
  for i in range(0,len(L),5):
    X = L[i:i+5]
    X.sort()
    M.append(X[len(X)//2])
  return(MoM(M))



def fastselect(L,l,r,k): # k-th smallest in L[l:r]
  if (k < 1) or (k > r-l):
    return(None)

  # Find MoM pivot and move to L[l]
  pivot = MoM(L[l:r])
  pivotpos = min([i for i in range(l,r) if L[i] == pivot])
  (L[l],L[pivotpos]) = (L[pivotpos],L[l])

  (pivot,lower,upper) = (L[l],l+1,l+1)
  for i in range(l+1,r):
    if L[i] > pivot:  # Extend upper segment
      upper = upper + 1
    else: # Exchange L[i] with start of upper segment
      (L[i], L[lower]) = (L[lower], L[i])
      (lower,upper) = (lower+1,upper+1)
  (L[l],L[lower-1]) = (L[lower-1],L[l]) # Move pivot
  lower = lower - 1
  
  # Recursive calls
  lowerlen = lower - l
  if k <= lowerlen:
    return(fastselect(L,l,lower,k))
  elif k == (lowerlen + 1):
    return(L[lower])
  else:
    return(fastselect(L,lower+1,r,k-(lowerlen+1)))

print(fastselect([4,3,5,6,2,1,8,9,7,10,13,15,18,17,11],0,15,4))


