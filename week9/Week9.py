'''
A thief robbing a store and can carry a maximum weight of W in his bag. There are n items in the
store with weights { } and corresponding values { }. What
items should he select to get maximum value? He cannot break an item, either he picks the
complete item or doesn’t pick it.

Write a function MaxValue(Items, W) that accepts a dictionary Items , where the key of the
dictionary represents the item number (1 to n) and the corresponding value is a tuple (weight of
item, Value of item) . The function accepts one more integer W , which represents the
maximum weight capacity of the bag. The function returns the total value of all selected items,
which is maximum in all possible selection.

Explanation :
	The thief can pick items 2 and 3 where the total weight of picked items is 3 + 4 = 7 which is less
	than the maximum capacity of the bag, but he gets maximum value (60) for this selection.
'''

# Solution code

def MaxValue(Items,W):
	(m, n) = (len(Items), W)
	c = []
	for i in range(m + 1):
		row = []
		for j in range(n + 1):
			row.append(0)
		c.append(row.copy())
	for i in range(1,m+1):
		for w in range(1,n + 1):
			if Items[i][0] > w:
				c[i][w] = c[i - 1][w]
			else:
				c[i][w] = max(c[i - 1][w],Items[i][1] + c[i - 1][w-Items[i][0]])
	return(int(c[m][n]))

#Suffix Code(Visible)

W = int(input())
Items= eval(input())
print(MaxValue(Items,W))

'''
Input
	8 # W - Maximum weight capacity of bag
	{1: (2,10),2: (3,20),3: (4,40)} # Items
Output
	60 # total value is 60 which is maximum.

Input
	10
	{1:(5,20), 2:(1,50), 3:(16,80), 4:(4,100), 5:(5,200),6:(4,150),7:(2,300),8:
	(6,120),9:(3,70),10:(6,40)}
Output
	570
'''



'''
You're given a list of tuples Activity for n activities, where in each tuple (activity_name, S,
F, P) , activity activity_name is scheduled to be done from start time S to finish time F and
obtains a profit of P after the finish.

Find out the maximum profit you can obtained by scheduled activities, but no two activities
should be in the subset with overlapping of time frame. If you choose an activity that finishes at
time x then another activity can be started at time x , not before that.

Write a function MaxProfit(Activity) that accepts a list of tuples Activity for n activities and
returns the value of maximum profit that can be obtained by scheduled activities.

Explanation :
	Consider input, 
		[('A',1,2,40),('B',3,4,5),('C',0,7,6),('D',1,2,3),('E',5,6,8),('F',5,9,2),
		('G',10,11,9),('H',0,11,35)]

	output, 
		62

	Activity schedule [A, B, E, G] gives a profit of 62 which is the maximum in all possible
	schedules.
'''

# Solution code

def tuplesort(L, index):
	L_ = []
	for t in L:
		L_.append(t[index:index+1] + t[:index] + t[index+1:])
	L_.sort()
	
	L__ = []
	for t in L_:
		L__.append(t[1:index+1] + t[0:1] + t[index+1:])
	return L__

def MaxProfit(Activity):
	n = len(Activity)
	act = tuplesort(Activity, 2)
	MaxProfit = []
	for a in act:
		MaxProfit.append(a[3])
	for i in range(1, n):
		for j in range(0, i):
			if act[i][1] >= act[j][2] and MaxProfit[i] < MaxProfit[j] + act[i][3] + 1:
				MaxProfit[i] += act[i][3]
	return max(MaxProfit)

# Suffix code

L = eval(input())
print (MaxProfit(L))

'''
Input
	[('A',1,2,2),('B',3,4,15),('C',5,7,16),('D',7,8,3),('E',8,9,8),('F',5,9,2),
	('G',10,11,9),('H',0,11,15)]
Output
	53

Input
	[('A',0,2,22),('B',2,4,45),('C',3,7,26),('D',5,8,13)]
Output
	80
'''




'''
Here is an function to return the maximum value in a list of integers. There is an error in this
function. Provide an input list for which maxbad produces an incorrect output.
'''
def maxbad(L):
	mymax = 0
	for i in range(len(L)):
		if L[i] > mymax:
			mymax = L[i]
	return(mymax)

# Solution

L = [-1,-2,-3,-4]

'''
Here is an function to return the maximum value among three positive integers. There is an error
in this function. Provide an input triple (n1,n2,n3) , where n1 , n2 and n3 are all positive
integers, for which max3bad produces an incorrect output.
'''

def max3bad(x,y,z):
	maximum = 0
	if x >= y:
		if x >= z:
			maximum = x
	elif y >= z:
		maximum = y
	else:
		maximum = z
	return(maximum)

# Solution

x = 3
y = 2
z = 5




'''
You are given weights and values of N items, put these items in a knapsack of capacity W to get
the maximum total value in the knapsack. Note that we have only one quantity of each item. In
other words, given two integer list value[0..N-1] and weight[0..N-1] which represent values
and weights associated with N items respectively. Also given an integer W which represents
knapsack capacity, find out the maximum value subset of value such that sum of the weights of
this subset is smaller than or equal to capacity W . You cannot break an item, either pick the
complete item or don’t pick it (0-1 property).

Write the function knapSack(W, weight, value, N) that returns the maximum possible value
you can get.
'''

# Solution

def knapSack(W, weight, value, N):
	st = [[0 for i in range(W+1)]for j in range(N+1)]
	for i in range(1,N+1):
		for j in range(1,W+1):
			if (weight[i-1]<=j):
				st[i][j]=max(value[i-1]+st[i-1][j-weight[i-1]],st[i-1][j])
			else:
				st[i][j]=st[i-1][j]
	return st[N][W]

'''
Input
	6
	10
	[4,4,5,6,7,2]
	[50,40,60,6,91,2]
Output
	110

Input
	8
	50
	[20, 30, 22, 10, 33, 19, 20, 40]
	[34, 56, 78, 23, 45, 70, 67, 45]
Output
	160
'''



'''
Given a rod of length n inches and an list of prices price that contains prices of all pieces of size
smaller or equal n . Determine the maximum value obtainable by cutting up the rod and selling
the pieces.

Write a function cutRod(n,price) that return the he maximum value obtainable by cutting up
the rod and selling the pieces
'''

# Solution

def cutRod(n,price):
	length=[]
	st=[[0 for i in range(n+1)] for j in range(n+1)]
	for i in range(1,n+1):
		length.append(i)
	for i in range(1,n+1):
		for j in range(1,n+1):
			if(length[i-1]<=j):
				st[i][j]=max(price[i-1]+st[i][j-length[i-1]],st[i-1][j])
			else:
				st[i][j]=st[i-1][j]
	return st[n][n]

'''
Input
	8 #n
	[1, 5, 8, 9, 10, 17, 17, 20] #price
Output
	22 #maximum value
	(The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5+17=22)

Input
	10
	[2,1,10,2,50,16,7,8,9,10]
Output
	100
'''


'''
A subsequence of a given sequence is a sequence that can be derived from the given sequence
by deleting some or no elements without changing the order of the remaining elements.

Write a function subsequenceProductCount(L, k) that accepts a list L of distinct positive
integers. Function returns number of subsequences having product of elements is smaller than
k.
'''

# Solution

def subsequenceProductCount(L, k):
	n = len(L)
	dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
	for i in range(1, k + 1):
		for j in range(1, n + 1):
			dp[i][j] = dp[i][j - 1]
			if L[j - 1] <= i and L[j - 1] > 0:
				dp[i][j] += dp[i // L[j - 1]][j - 1] + 1
	return dp[k][n]

'''
Input
	[1,2,3,4] #L
	10 #k
Output
	11 # number of subsequences having product of elements is smaller than 10
	{
		Following are all possible subsequence of L having product of elements is smaller than 10
		
		[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [1, 2, 3], [1, 2, 4]
	}

Input
	[1,2,3,4,5,6]
	12
Output
	21
'''
