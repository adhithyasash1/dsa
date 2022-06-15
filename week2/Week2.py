'''
Consider a list L containing n integers, where each integer i is in the range [0, r) that is 0 <=
i < r , r<1000 and n>>r (n is much greater than r). Write a Python function sortInRange(L,
r) to sort the list L in ascending order. Try to write a solution that runs in asymptotic
complexity.

Example : 
	input :
		L: 2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2
		r: 4

	output : 
		0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3
'''
def sortInRange(L, r):
	# Create a dictionary with r keys for each integer in range r, initialize every value to 0
	countDict = dict.fromkeys(range(r), 0)
	# Iterate over the array and count each integer in the list
	for num in L:
		countDict[num] += 1
	index=0
	for key in countDict.keys():
		for i in range(countDict[key]):
			L[index] = key
			index += 1

'''
Consider a list students of tuples, where each tuple contains the first name(string) and roll
number(int) of a student. 

Write a Python function sortTuples(students) to sort the list by roll
numbers in ascending order.

For example : 
students = [("Ram", 104), ("Sam", 101), ("Sita", 103), ("Ram", 207)]

after running sortTuples(students) , the list should be

students = [("Sam", 101), ("Sita", 103), ("Ram", 104), ("Ram", 207)]
'''

def sortTuples(students):
	size = len(students)
	for i in range(1, size):
		j = i
		while (j>0 and (students[j][1] < students[j - 1][1])):
			temp = students[j]
			students[j]= students[j - 1]
			students[j - 1]= temp
			j -= 1

# Suffix 
s = []
n = int(input())
for i in range(n):
	data = input().split()
	s.append((data[0], int(data[1])))
sortTuples(s)
for item in s:
	print(*item)

'''
Write a Python function findIntersection(L1, L2) that accepts two integer lists L1 and L2
and return a list that contains elements that are common to both lists. 

Write a solution that runs in O(nlogn) time.

L1 contains all distinct integers and L2 contains all distinct integers, but there can be many
elements common between L1 and L2.

List L1 intersection L2 contains all elements that are common to L1 and L2 . The elements in
the returned list can be in any order.

For example :
if L1 = [5, 8, 2] and L2 = [6, 8] 
then, findIntersection(L1, L2) should return list [8]

if L1 = [3, 7, 2, 9, 5] and L2 = [6, 3, 7, 5] 
then, findIntersection(L1, L2) should return list [3, 7, 5]
'''

def binarySearch(L, k):
	s = len(L)
	if(s < 1):
		return False
	left = 0
	right = s - 1
	while(left <= right):
		mid = (left + right)//2
		if (k == L[mid]):
			return True
		elif (k < L[mid]):
			right = mid - 1
		else:
			left = mid + 1
	return False

def findIntersection(L1, L2):
	L1.sort()
	L3 = []
	for item in L2:
		if (binarySearch(L1, item) == True):
			L3.append(item)
	return L3

'''
You have a deck of shuffled cards ranging from 0 to 100,000,000. There are 2 sub-ordinate below
you and two subordinates below them and it goes on.

The job of the sub-ordinate is to split the deck of cards that they received and give it to two
sub-ordinate of them. If they receive a deck of cards from their subordinates, they merge it
in an ascending order and give it their higher level.

If a subordinate received only two card, then he/she himself/herself arrange in ascending
order give it back that to the superior.

If a subordinate received only one card, then he/she will give back that to the superior.

Your task is to find how many people (including you) are required to sort the cards and print the
sorted deck of cards and number of people required as a tuple.

Write the function def subordinates(L):

Terminology:
(67) subordinate number 67
[1, 3, 5, 2] -> [1, 2, 3, 5] deck of cards got -> deck of cards returned
--------------------------------
(0) [3, 1, 2, 0, 5] -> [0, 1, 2, 3, 5]
|
|--(1) [3, 1] -> [1, 3]
|
|--(2) [2, 0, 5] -> [0, 2, 5]
|
|--(3) [2] -> [2]
|
|--(4) [0, 5] -> [0, 5]

Example :

input - [194, 69, 103, 150, 151, 44, 103, 98]

output - ([44, 69, 98, 103, 103, 150, 151, 194], 7

input - [10, 33, 45, 67, 92, 100, 5]

output - ([5, 10, 33, 45, 67, 92, 100], 7)
'''

def merge(A, B):
	m, n = len(A), len(B)
	C, i, j, k = [], 0, 0, 0
	while k < m + n:
		if i == m:
			C.extend(B[j:])
			k = k + n - j
		elif j == n:
			C.extend(A[i:])
			k = k + m - i
		elif A[i] < B[j]:
			C.append(A[i])
			i, k = i + 1, k + 1
		else:
			C.append(B[j])
			j, k = j + 1, k + 1
	return C

def mergesort(L):
	global c
	c += 1
	n = len(L)
	if n == 2:
		return L if L[0] < L[1] else L[::-1]
	if n <= 1:
		return L
	m = n//2
	l = mergesort(L[:m])
	r = mergesort(L[m:])
	L_ = merge(l, r)
	return L_

def subordinates(L):
	return mergesort(L), c
	
c = 0
print(subordinates(eval(input())))

'''
Given a list L of random numbers and another number pairSum , 

find whether there exists two numbers in the list such that their sum is equal to pairSum . 

Complete the below Python function findPair(L, pairSum) that performs this operation. 

Try to write a solution which runs in O(nlogn) or better

For example consider the below list :

We need to find if there exists any pair whose sum is equal to 21. 
11+10 = 21. So the function should return True.
'''

def findPair(L, x):
	L.sort()
	left = 0
	right = len(L) - 1
	while(left < right):
		sum = L[left] + L[right]
		if (sum == x):
			return True
		elif (sum > x):
			right -= 1
		else:
			left += 1
	return False

# Suffix
L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))

'''
Write a Python function listUnion(L1, L2) that accepts two integer lists L1 and L2 and return
a list that is the union( L1 U L2 ) of the two lists and is sorted in ascending order. 

Try to write a solution that runs in O(n log n) time.

L1 contains all distinct integers and L2 contains all distinct integers, but there can be many
elements common between L1 and L2 .

List ( L1 U L2 ) contains all distinct elements of L1 and L2 combined, and is sorted in ascending
order.
'''

def findUnion(L1, L2):
	L1.sort()
	L2.sort()
	L3 = []
	
	s1 = len(L1)
	s2 = len(L2)
	
	p1 = p2 = 0
	while (p1<s1 and p2<s2):
		if (L1[p1] == L2[p2]):
			L3.append(L1[p1])
			p1+=1
			p2+=1
		elif (L1[p1] < L2[p2]):
			L3.append(L1[p1])
			p1+=1
		else:
			L3.append(L2[p2])
			p2+=1
	while(p1<s1):
		L3.append(L1[p1])
		p1+=1
	while(p2<s2):
		L3.append(L2[p2])
		p2+=1
	return L3

set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
print(*findUnion(set1, set2))





