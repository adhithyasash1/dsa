'''
Write a function MaxValueSelection(items, C) that accepts a dictionary items where each key
of the dictionary represents the item name and the corresponding value is a tuple (number of
units, value of all units) and function accept one more variable C which represents the
maximum capacity of units you can select from all items to get maximum value.
'''

# Solution

def maxValueSelection(items, c):
	total_value = 0
	for i in sorted(items, key=lambda x:items[x][1]/items[x][0], reverse=True):
		if items[i][0] <= c:
			total_value += items[i][1]
			c -= items[i][0]
		else:
			total_value += items[i][1]/items[i][0] * c
			c = 0
	return total_value

# Suffix

items = eval(input())
c = int(input())
print(int(maxValueSelection(items, c)))


'''
Input
	{1:(10,60),2:(20,100),3:(30,120)}
	50
Output
	240

Input
	{1:(4,400),2:(9,1800),3:(10,3500),4:(20,4000),5:(2,1000),6:(1,200)}
	20
Output
	6100
'''
