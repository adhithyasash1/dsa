class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
           raise TimerError("Timer is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
           raise TimerError("Timer has not been run yet. Use .start()")
        return(self_elapsed_time)

    def __str__(self):
        """print() prints elapsed time"""
        return(str(self._elapsed_time))
    
# ANALYSIS OF SEARCH ALGORITHMS
    
def naive_search(v, l):
    for i in l:
        if i == v:
            return True
    return False

def binary_search(v, l):
    if l == [ ]:
        return False
    
    m = len(l) // 2
    
    if v == l[m]:
        return True
    if v < l[m]:
        return binary_search(v, l[:m])
    if v > l[m]:
        return binary_search(v, l[m+1:])
    
l = list(range(0, 100000, 2))
t = Timer()
t.start()
for i in range(3001, 13000, 2):
    v = naive_search(i, l)
t.stop()
print()
print('Naive Search -', t)

t.start()
for i in range(3001, 13000, 2):
    v = binary_search(i, l)
t.stop()
print()
print('Binary Search -', t)

# ANALYSIS OF SELECTION SORT

def SelectionSort(L):
   n = len(L)
   if n < 1:
      return(L)
   for i in range(n):
      # Assume L[:i] is sorted
      mpos = i  
      # mpos is position of minimum in L[i:]
      for j in range(i + 1, n):
        if L[j] < L[mpos]:
           mpos = j
      # L[mpos] is the smallest value in L[i:]
      L[i], L[mpos] = L[mpos], L[i]
      # Now L[:i+1] is sorted
   return(L)

import random
random.seed(2021)
inputlists = {}
inputlists["random"] = [ random.randrange(100000) for i in range(5000) ] 
inputlists["ascending"] = [ i for i in range(5000) ]
inputlists["descending"] = [ i for i in range (4999, -1, -1) ]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    SelectionSort(tmplist)
    t.stop()
    print()
    print(k, t)
    
# ANALYSIS OF INSERTION SORT

def InsertionSort(L):
   n = len(L)
   if n < 1:
      return(L)
   for i in range(n):
      # Assume L[:i] is sorted
      # Move L[i] to correct position in L[:i]
      j = i
      while(j > 0 and L[j] < L[j-1]):
          L[j], L[j-1] = L[j-1], L[j]
          j = j-1
      # Now L[:i+1] is sorted
   return L

import random
random.seed(2021)
inputlists = {}
inputlists["random"] = [ random.randrange(100000) for i in range(5000) ]
inputlists["ascending"] = [ i for i in range(5000) ]
inputlists["descending"] = [ i for i in range (4999, -1, -1) ]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    InsertionSort(tmplist)
    t.stop()
    print()
    print(k, t)
    
# Merge Sort

def merge(A,B):
  (m,n) = (len(A),len(B))
  (C,i,j,k) = ([],0,0,0)
  while k < m+n:
    if i == m:
      C.extend(B[j:])
      k = k + (n-j)
    elif j == n:
      C.extend(A[i:])
      k = k + (n-i)
    elif A[i] < B[j]:
      C.append(A[i])
      (i,k) = (i+1,k+1)
    else:
      C.append(B[j])
      (j,k) = (j+1,k+1)
  return(C)

def mergesort(A):
  n = len(A)

  if n <= 1:
     return(A)
  
  L = mergesort(A[:n//2])
  R = mergesort(A[n//2:])

  B = merge(L,R)

  return(B)

# mergesort([i for i in range(0,1000,2)]+[j for j in range (1,1000,2)])
import random
random.seed(2021)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(1000000)]
inputlists["descending"] = [i for i in range (999999,-1,-1)]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    mergesort(tmplist)
    t.stop()
    print()
    print(k,t)


    
    
    
    
    
    
    
    
    
    
    
    
    