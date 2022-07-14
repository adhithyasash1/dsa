'''
Write a Python function kthLargest(arr, k) that accepts a list arr of integers of size n and an
integer k, such that k<=n and returns the kth largest integer in arr. 

The solution should run in O(n) time.

Example : 
	Input : 
		7 10 4 3 20 15
	Output:
		3

	Input : 
		15 10 3 4 8 9 12 5
	Output:
		2
'''

def kthLargest(arr, k):
	return fast(arr, 0, len(arr), k)

def Medianofmedian(L):
	if(len(L)<=5):
		L.sort()
		return(L[len(L)//2])
	M=[]
	for i in range(0,len(L),5):
		x=L[i:i+5]
		x.sort()
		M.append(x[len(x)//2])
	return (Medianofmedian(M))

def fast(L,l,r,k):
	if(k<l) and (k>r-l):
		return None
	pivot=Medianofmedian(L[l:r])
	pivotpos=min([i for i in range(l,r) if L[i]==pivot])
	(L[l],L[pivotpos])=(L[pivotpos],L[l])
	(pivot,lower,upper)=(L[l],l+1,l+1)
	for i in range(l+1,r):
		if L[i]<pivot:
			upper=upper+1
		else:
			(L[i],L[lower])=(L[lower],L[i])
			(lower,upper)=(lower+1,upper+1)
	(L[l],L[lower-1])=(L[lower-1],L[l])
	lower=lower-1
	lowerlen=lower-l
	if k<=lowerlen:
		return(fast(L,l,lower,k))
	elif k==(lowerlen+1):
		return(L[lower])
	else:
		return(fast(L,lower+1,r,k-(lowerlen+1)))

# Suffix

arr=[int(item) for item in input().split(" ")]
k=int(input())
print(kthLargest(arr, k))


'''
Given a Python function Karatsuba(x, y) that implements Karatsuba's algorithm, that multiplies
two integers x and y recursively. Length of integers x and y may or may not be same. 

Refer the definition of function Karatsuba(x,y) and complete the Python function
calculateAndAssign(x,y) that accepts two integers x and y and returns five variables that will
be used in subsequent recursive calls to function Karatsuba(x,y).

Example : 
	Input : 
		345
		23
	Output : 
		7935

	Input : 
		7892
		3456
	Output : 
		27274752

'''
def Karatsuba(x, y):
	if x < 10 and y < 10:
		return x * y
	var1, var2, var3, var4, var5 = calculateAndAssign(x, y)
	ad_plus_bc = Karatsuba(var1, var2) - var3 - var4
	return (10 ** (2*var5))*var3 + (10 ** var5)*ad_plus_bc + var4

def calculateAndAssign(x, y):
	num1_length = len(str(x))
	num2_length = len(str(y))
	n = max(num1_length,num2_length)
	l = n//2
	num1 = x // (10 ** l)
	rem1 = x % (10 ** l)
	num2 = y // (10 ** l)
	rem2 = y % (10 ** l)
	ac = Karatsuba(num1, num2)
	bd = Karatsuba(rem1, rem2)
	return (num1 + rem1), (num2 + rem2), ac, bd, l


'''
Write a function Findpeak(L) that accepts a list L of n elements and returns the peak element of
the list. A list element is a peak if it is greater than its neighbors. For corner elements, we need to
consider only one neighbor. Write a solution of complexity. Consider that there is only
one peak is in the list, L.
'''

# Solution

def findPeakUtil(arr, low, high, n):
	mid = low + (high - low)/2
	mid = int(mid)
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
		return arr[mid]
	elif (mid > 0 and arr[mid - 1] > arr[mid]):
		return findPeakUtil(arr, low, (mid - 1), n)
	else:
		return findPeakUtil(arr, (mid + 1), high, n)

def findPeak(L):
	n = len(L)
	return findPeakUtil(L,0,n-1,n)

L = eval(input())
print(findPeak(L))

'''
Input
	[5, 10, 20, 15]
Output
	20

Input
	[9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8]
Output
	9
'''



'''
Write a function findMedian(A,B) that accept two sorted list A and B of the same size and
function return median of the sorted merged list of A and B. write a solution of O(logn).
	
	---> If length of sorted merged list is odd then median is middle element.
	---> If length of sorted merged list is even then median is average of two middle elements.
'''

# Solution

def median(A,B,sA,lA,sB,lB):
	n = lA - sA + 1
	mid = n // 2
	midA = sA + mid
	if n % 2 == 0:
		midB = sB + mid - 1
	else:
		midB = sB + mid
	if n == 1:
		return (A[sA] + B[sB]) / 2
	elif n == 2:
		return (max(A[sA], B[sB]) + min(A[lA], B[lB])) / 2
	elif A[midA] == B[midB]:
		return (A[midA] + B[midB]) / 2
	elif A[midA] > B[midB]:
		return median(A, B, sA, midA, midB, lB)
	elif A[midA] < B[midB]:
		return median(A, B, midA, lA, sB, midB)

def findMedian(A,B):
	return median(A,B,0,len(A)-1,0,len(B)-1)

A = eval(input())
B = eval(input())
print(findMedian(A,B))

'''
Input
	[1,2,3,4,5,6]
	[7,8,9,10,12,13]
Output
	6.5

Input
	[6,7,8,9,10,11,12]
	[1,2,3,3,3,3,3]
Output
	4.5
'''



'''
Write a function KthElement(A,B,k) that accept two sorted list A and B of the size n and m
respectively and a integer value k and function return Kth element in the sorted merged list of A
and B from start. write a solution of O(logn + logm).
'''

# Solution

def kth(arr1, arr2, n, m, k):
	if n == 1 or m == 1:
		if m == 1:
			arr2, arr1 = arr1, arr2
			m = n
		if k == 1:
			return min(arr1[0], arr2[0])
		elif k == m + 1:
			return max(arr1[0], arr2[0])
		else:
			if arr2[k - 1] < arr1[0]:
				return arr2[k - 1]
			else:
				return max(arr1[0], arr2[k - 2])
	
	mid1 = (n - 1)//2
	mid2 = (m - 1)//2
	
	if (mid1 + mid2 + 1) < k:
		if arr1[mid1] < arr2[mid2]:
			return kth(arr1[mid1 + 1:], arr2, n - mid1 - 1, m, k - mid1 - 1)
		else:
			return kth(arr1, arr2[mid2 + 1:], n, m - mid2 - 1, k - mid2 - 1)
	else:
		if arr1[mid1] < arr2[mid2]:
			return kth(arr1, arr2[:mid2 + 1], n, mid2 + 1, k)
		else:
			return kth(arr1[:mid1 + 1], arr2, mid1 + 1, m, k)
	
def KthElement(A,B,k):
	return kth(A,B,len(A),len(B),k)


A = eval(input())
B = eval(input())
k = int(input())
print(KthElement(A,B,k))

'''
Input
	[6,7,8,9,10,11,12]
	[2,3,3,7,9]
	5
Output
	7

Input
	[1,2,3,4]
	[7,8,9,10,12,13]
	4
Output
	4
'''



'''
Write a function pickingNumbers(a) that accept a list a and return the length of the longest set
of element where the absolute difference between any two elements is less than or equal to 1.
'''

# Solution

def pickingNumbers(a):
	a.sort()
	count=1
	pos=0
	maxx=0
	for i in range(1,len(a)):
		if(abs(a[i]-a[pos])<=1):
			count=count+1
		else:
			if(count>maxx):
				maxx=count
			count=1
			pos=i
	if(maxx>count):
		return maxx
	else:
		return count

a=[int(item) for item in input().split(" ")]
print(pickingNumbers(a))

'''
Input
	4 6 5 3 3 1
Output
 	3

Input
	7 12 13 19 17 7 3 18 9 18 13 12 3 13 7 9 18 9 18 9 13 18 13 13 18 18 17 17 13
	3 12 13 19 17 19 12 18 13 7 3 3 12 7 13 7 3 17 9 13 13 13 12 18 18 9 7 19 17
	13 18 19 9 18 18 18 19 17 7 12 3 13 19 12 3 9 17 13 19 12 18 13 18 18 18 17
	13 3 18 19 7 12 9 18 3 13 13 9 7
Output
	30
'''




'''
Write a Python function kthSmallest(arr, k) that accepts a list arr of integers of size n and an
integer k , such that k<=n and returns the k th smallest integer in arr . The solution should run
in O(n) time.
'''

# Solution 

def kthSmallest(arr, k):
	return fastselect(arr, 0, len(arr), k)

def MoM(L): 
	# Median of medians
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

def fastselect(L,l,r,k): 
	# k-th smallest in L[l:r]
	if (k < 1) or (k > r-l):
		return(None)
	
	# Find MoM pivot and move to L[l]
	pivot = MoM(L[l:r])
	pivotpos = min([i for i in range(l,r) if L[i] == pivot])
	(L[l],L[pivotpos]) = (L[pivotpos],L[l])
	
	(pivot,lower,upper) = (L[l],l+1,l+1)
	
	for i in range(l+1,r):
		if L[i] > pivot: 
			# Extend upper segment
			upper = upper + 1
		else: 
			# Exchange L[i] with start of upper segment
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

arr=[int(item) for item in input().split(" ")]
k=int(input())
print(kthSmallest(arr, k))

'''
Input
	15 10 3 4 8 9 12 5
	2
Output
	4

Input
	7 10 4 3 20 15
	3
Output
	7
'''

	

















































