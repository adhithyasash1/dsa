''' given an array based on min_heap (arr)
write a python function min_max(arr) that
to convert arr to a max Heap, 

the function should change the original arr
to max heap, the expected time complexity is 
O(n)

Input
    66 55 43 34 12 7 2 20 5
Output
    True
'''

def mh(a,k):
    l=2*k+1
    r=2*k+2
    mini=k
    if l<len(a) and a[l]>a[k]:
        mini=l
    if r<len(a) and a[r]>a[mini]:
        mini=r
    if mini!=k:
        a[k],a[mini]=a[mini],a[k]
        mh(a,mini)

def min_max(arr):
    x=int((len(arr)//2)-1)
    for i in range(x,-1,-1):
        mh(arr,i)

# Solution 2

def heapify(A, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2     
    if l < n and A[largest] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] 
        heapify(A, n, largest)
 

def min_max(A):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(A,n,i)
