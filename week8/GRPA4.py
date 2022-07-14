'''
Write a python function MoM7pos(arr) that accepts a list arr of integers (not necessarily distinct) and computes the median of medians (of blocks) M dividing the list arr into blocks of 7 and returns the position of M in arr if it were sorted. 

If M is repeated more than once in the list arr, return the index of first occurence of M in arr if it were sorted. 

For simplicity the size of arr will be a multiple of 7

Solution should run in O(n) time.
'''

# Solution 1

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

def MoM7Pos(L):
    x = MoM(L)
    return(sorted(L).index(x))
arr=[int(item) for item in input().split(" ")]
print(MoM7Pos(arr))

# Solution 2

def partitionPos(arr, pivot):
  arr[pivot], arr[0] = arr[0], arr[pivot]
  l = 1
  r = len(arr)-1
  while (l<r):
    while(arr[l] < arr[0]):
      l+=1
    while(arr[r]>=arr[0]):
      r-=1
    arr[l], arr[r] = arr[r], arr[l]

  return l-1

def MoM7(arr):
  if len(arr) <= 7:
    arr.sort()
    return(arr[len(arr)//2])

  # Construct list of block medians
  M = []

  for i in range(0, len(arr), 7):
    X = arr[i:i+7]
    X.sort()
    M.append(X[len(X)//2])

  return(MoM7(M))

def MoM7Pos(arr): 
  mom = MoM7(arr)
  return partitionPos(arr, arr.index(mom))
arr=[int(item) for item in input().split(" ")]
print(MoM7Pos(arr))

'''
Input
	5 4 3 1 1 4 6 1 4 1 4 3 3 3 2 5 6 3 5 4 6 5 2 4 5 6 5 4
Output
	18

Input
	21 0 5 20 6 3 18 1 15 0 0 21 15 15 0 3 20 15 10 18 1 16 7 13 9 6 17 7
Output
	14
'''


