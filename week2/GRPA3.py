'''
Merging two sorted arrays in place

Given a custom implementation of list named MyList.
On MyList objects you can perform read operations similar to the in build 
lists in python, example use A[i] to read element in index i in MyList object A.

The only possible operation that you can use to edit data in MyList objects is
by calling the swap method. For instance, A.swap(indexA, B, indexB) will swap values
at A[indexA] and B[indexB], and A.swap(index1, A, index2) will swap A[index1] and A[index2],
where indexA, indexB, index1, index2 are all integers.

Complete the python function mergeInPlace(A, B) that accepts two MyLists A and B containing
integers that are sorted in ascending order and merges them in place (without using any other list)
such that after merging, A and B are still sorted in ascending order with the smallest 
element of both MyLists as the first element of A.

Input : 
	2 4 6 9 13 15
	1 3 5 10
Output :
	[1,2,3,4,5,6]
	[9,10,13,15]
'''

def mergeInPlace(A, B):
	a, b = len(A), len(B)
	if a > b:
		for i in range(b):
			for j in range(a):
				if A[j] >= B[i]:
					A.swap(j, B, i)

		for i in range(b):
			for j in range(i+1, b):
				if B[i] >= B[j]:
					B.swap(i, B, j)
		return(A, B)

	elif a < b:
		for i in range(b):
			for j in range(a):
				if A[j] >= B[i]:
					A.swap(j, B, i)
		
		for i in range(b):
			for j in range(i+1, b):
				if B[i] >= B[j]:
					B.swap(i, B, j)
		return(A, B)

	elif a == b:
		for i in range(a):
			for j in range(b):
				if A[i] >= B[j]:
					A.swap(i, B, j)

		for i in range(b):
			for j in range(i+1, b):
				if B[i] >= B[j]:
					B.swap(i, B, j)
		return(A, B)


# Solution 2

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

def mergeInPlace(A, B):
    C = merge(A, B)
    m, n = len(A), len(B)
    ans1, ans2 = [], []
    if m > n:
        for i in range(m):
            ans1.append(C[i])
        for j in range(m, m+n):
            ans2.append(C[j])
    elif n > m:
        for i in range(m):
            ans1.append(C[i])
        for j in range(m, m+n):
            ans2.append(C[j])
    if ans1 != B and ans2 !=A: 
        return ans1, ans2
