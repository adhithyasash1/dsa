import sys
sys.setrecursionlimit(2**31-1)

def selection_sort(L):
    # if the length if zero , we don't need to do anything, just return the list
    n = len(L)
    if n < 1:
        return L
    #else, we scan the list and look for the minimum
    for i in range(n):
        # Assume L[:i] is sorted
        mpos = i
        # mpos = position of minimmu element in L[i:] 
        for j in range(i+1, n):
            if L[j] < L[mpos]:
                mpos = j
        # Exchange L[mpos] and L[i]
        L[i], L[mpos] = L[mpos], L[i]
        # Now L[:i+1] is sorted 
    return L

# Insertion Sort
def insertion_sort(L):
    n = len(L)
    if n < 1:
        return L
    else:
        for i in range(n):
            # Assume L[:i] is sorted
            j = i
            while j > 0 and L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
                j = j-1
            # Now L[:i+1] is sorted
        return L
    
# Insertion sort done recursively
def insert(L, v):
    n = len(L)
    if n < 1:
        return [v]
    else:
        if v >= L[-1]:
            return L + [v]
        else:
            return insert(L[:-1], v) + L[-1:]

def i_sort(L):
    n = len(L)
    if n < 1:
        return L
    L = insert(i_sort(L[:-1]), L[-1])
    return L

# Merge Sort

def merge(A, B):
    m, n = len(A), len(B)
    C, i, j, k = [], 0, 0, 0
    while k < m + n:
        if i == m:
            C.extend(B[j:])
            k += n - j
        elif j == n:
            C.extend(A[i:])
            k += m - i   
        elif A[i] < B[j]: 
            C.append(A[i])
            i, k = i + 1, k + 1
        else:
            C.append(B[j])
            j, k = j + 1, k + 1
    return C

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    L = merge_sort(A[:n//2])
    R = merge_sort(A[n//2:])
    
    B = merge(L, R) 
    return B       

# Binary Search

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
    
# Quick Sort

def quicksort(L, l, r):
    # Sort L[l:r]
    if r - l <= 1:
        return L
    
    pivot, lower, upper = L[l], l+1, l+1 
    for i in range(l+1, r):
        if L[i] > pivot:
            #Extend upper segment 
            upper = upper + 1
        else:
            #Exchange L[i] with start of upper segment 
            L[i], L[lower] = L[lower], L[i]
            #Shift both segments
            lower, upper = lower + 1, upper + 1
    #Move pivot between upper and lower
    L[l], L[lower - 1] = L[lower -1], L[l]
    lower = lower - 1
    #Recursive Calls
    quicksort(L, l, lower)
    quicksort(L, lower + 1, upper)
    return L
    

import string
def combinationSort(strList):
  # Create a dictionary with 26 keys from characters 'a' to 'z', each key has an empty list as value.
  groups = {k: [] for k in string.ascii_lowercase}

  # Using this dictionary to group strings with same initial character.  
  for i in range(len(strList)):
    char=strList[i][0]
    groups[char].append(strList[i])
  
  strList=[]
  # Recreate the list from all the strings in groups, iterating on groups from a to z.
  for char in groups.keys():
    for s in groups[char]:
      strList.append(s)
  
  L1 = strList.copy() # Saving intermediate result to return later.
  i = 1
  left = 0
  # As there can be no more than 100 strings with same initial character.
  # Using insertion sort within group.
  while i<len(strList):
    right = i
    while(right>left and strList[right][0] == strList[right-1][0] and int(strList[right-1][1:])<int(strList[right][1:])):
      strList[right], strList[right-1] = strList[right-1], strList[right]
      right -= 1
    i += 1
  
  return L1, strList

O(logn) binary search :

def binarysearch(L,v,s,e):
    if e - s == 0:
        return(v==L[s])
    mid = (e + s)//2
    if v == L[mid]:
        return(True)
    if v < L[mid]:
        return(binarysearch(L,v,s,mid-1))
    else:
        return(binarysearch(L,v,mid+1,e))
    
def binarysearch(L, v):
    s = 0
    e = len(L)
    m = 0
    while s < e: 
        m = s + (e - s) // 2
        if L[m] < v:
            s = m + 1
        elif L[m] > v:
            e = m - 1
        else:
            return m
    return -1


  
    
    
    
            


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


        
    
        
        

            
