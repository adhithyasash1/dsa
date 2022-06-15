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


'''
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
'''
	

