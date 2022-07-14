'''
A manufacturing plant has N independent working lines. Each job requires different amount of
time to be completed and due time. Optimize the scheduling of jobs for every line so that every
job is will be completed within due time or minimum lateness possible.

Write a function minimizeLateness(N, jobs) to return the sequence of job ids to be scheduled
in list of list. jobs is the tuple of (job_id, time_required, due_time) , where job_id ,
time_required and due_time are the unique number assigned to job, relative time required to
complete the job and absolute time before which the job should have completed respectively.

Note:
job_id is given from 0 to m-1, for m jobs.

For each test case there will be a upper bound of lateness on the second line of input. The
lateness of your optimum schedule should be less than or equal to the upper bound of lateness.

Example : 
	Input :
		N = 2
		36 # upper bound of lateness
		jobs = [ (0, 10, 15),
		(1, 9, 15),
		(2, 2, 10),
		(3, 6, 14),
		(4, 5, 6),
		(5, 5, 7),
		(6, 2, 6),
		(7, 7, 11),
		(8, 3, 5),
		(9, 4, 9) ]

	Output : 
		[[8, 5, 2, 7, 1], [6, 4, 9, 3, 0]]
'''

def minimizeLateness(N, jobs):
	sortedL = sorted(jobs, key=lambda x:(x[2], x[1], x[0]))
	optimum = [ [] for i in range(N) ]
	usedtime = { i:0 for i in range(N) }
	i = 0
	while i < len(sortedL):
		freeline = min(usedtime, key=lambda x:usedtime[x])
		optimum[freeline].append(sortedL[i][0])
		usedtime[freeline] += sortedL[i][1]
		i += 1
	return optimum
	
	# suffix (invisible)
def lateness(optimum, jobs):
	jobdict = {job[0]:(job[0],job[1],job[2]) for job in jobs}
	time = 0
	late = 0
	for optID in optimum:
		time += jobs[optID][1]
		overtime = time - jobdict[optID][2]
		late += overtime if overtime >= 0 else 0
	return late
	
N = int(input())
m = int(input())
jobs = []
while True:
	line = input().strip()
	if line == '':
		break
	t = line.split(' ')
	jobs.append((int(t[0]), int(t[1]), int(t[2])))
	
optimum = minimizeLateness(N, jobs)
extratime = 0
for i in range(N):
	extratime += lateness(optimum[i], jobs)
if extratime <= m:
	print('Passed')
else:
	print('Improve your algorithm')

'''
Write a function Huffman(s) that accepts a string of characters a,b,c,d,e and f without any space.
The function should generate prefix code for each character based on its frequency in string s and return a 
dictionary where the key represents the character and the corresponding value represents Huffman code for
that character.

Select two smallest frequency nodes each time, if more than 2 nodes have the same 
smallest frequency, then select nodes in the lexicographical order of their symbol.
Assume x and y are the two smallest nodes, then : 

-> if x.frequency < y.frequency then x will always come on the right of the parent node.
-> if x.frequency = y.frequency then the symbol of the node (in lexicographical order) will become the left child, and others will become the right child of the parent node.
-> if x is a left node and y is a right node, then parent node will be identified by x.symbol + y.symbol for further creation of tree.

Example : 

Input : 

s = 'aaaacccbbdddddddeeefffff'
# frequency of each character : 
a - 4
b - 2
c - 3
d - 7
e - 3
f - 5

Output : 

a 111
b 000 
c 001
d 01
e 110
f 01

Huffman Coding

Algorithm : 

1) Calculate the frequency of each character in the string.
2) Sort the characters in increasing order of the frequency.
3) Make each unique character as a leaf node.
4) Create an empty node z. Assign the minimum frequency to the left child of z and assign the second minimum frequency to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.
5) Remove these two minimum frequencies from Q and add the sum into the list of frequencies.
6) Insert node z into the tree.
7) Repeat steps 3 to 5 for all the characters.
8) For each non-leaf node, assign 0 to the left edge and 1 to the right edge.
'''

class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

# Solution        
        
def Huffman(s):
    huffcode = {}
    char = list(s)
    freqlist = []
    unique_char = set(char)
    for c in unique_char:
        freqlist.append((char.count(c),c))
    nodes = []
    for nd in sorted(freqlist):
        nodes.append((nd,Node(nd[0],nd[1])))
    while len(nodes) > 1:
        nodes.sort()
        L = nodes[0][1]
        R = nodes[1][1]
        newnode = Node(L.frequency + R.frequency, L.symbol + R.symbol,L,R)
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(((L.frequency + R.frequency, L.symbol + R.symbol),newnode))

    for ch in unique_char:
        temp = newnode
        code = ''
        while ch != temp.symbol:           
            if ch in temp.left.symbol:
                code += '0'
                temp = temp.left
            else:
                code += '1'
                temp = temp.right
        huffcode[ch] = code   
    return huffcode


s = 'abbcaaaabbcdddeee'
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])

'''
Output : 

a 10
b 01
c 110
d 111
e 00


At each recursive step, extract letters with minimum frequency and replace by composite letter with combined frequency 
Store frequencies in an array  
Linear scan to find minimum values 
|A| = k, number of recursive calls is (k-1)
Complexity is O(k^2)
Instead, maintain frequencies in an heap 
Extracting two minimum frequency letters and adding back compound  letter are both O(logk)
Complexity drops to O(klogk)
'''




'''
Write a function decode(root, ciphertext) that accepts a variable root which contains the
reference of the root node of Huffman tree and an encoded message ciphertext in the form of
a string (using 0 and 1). The function returns the decoded message in the form of a string.
Structure of node in given Huffman tree
Leaf node contains the final symbol (in red color)

Sample Input
	0001110001110000011011001 #Encoded message

Output
	bababcdef # Decoded message
'''

# Solution

def decode(root,ciphertext):
	message =''
	temp = root
	for i in ciphertext:
		if i == '0':
			temp = temp.left
		if i == '1':
			temp = temp.right
		if temp.left == None and temp.right == None:
			message += temp.symbol
			temp = root
	return message

# Suffix 

class Node:
	def __init__(self,frequency,symbol=None,left=None,right=None):
		self.frequency = frequency
		self.symbol = symbol
		self.left = left
		self.right = right

def Huffman(s):
	char = list(s)
	freqlist=[]
	unique = set(char)
	for c in unique:
		freqlist.append((char.count(c),c))
	nodes = []
	for nd in sorted(freqlist):
		nodes.append((nd,Node(nd[0],nd[1])))
	while len(nodes) > 1:
		nodes.sort()
		L = nodes[0][1]
		R = nodes[1][1]
		newnode = Node(L.frequency + R.frequency,L.symbol+R.symbol,L,R)
		nodes.pop(0)
		nodes.pop(0)
		nodes.append(((L.frequency+R.frequency,L.symbol+R.symbol),newnode))
	return newnode

# huffman code
'''
a 111
b 000
c 001
d 10
e 110
f 01
'''
s = 'aaaacccbbdddddddeeefffff'
cipher = input()
res = Huffman(s)
print(decode(res,cipher))




'''
Write a method MaxValueSelection(items, C) that accepts a dictionary items where each key
of the dictionary represents the item name and the corresponding value is a tuple (number of
units, value of all units) and function accept one more variable C which represents the
maximum capacity of units you can select from all items to get maximum value.
'''

# Solution

def MaxValueSelection(items, C):
	itemlist = []
	for i,j in items.items():
		itemlist.append((j[1]/j[0],i,j[0]))
	itemlist.sort(reverse=True)
	maxvalue = 0
	for itm in itemlist:
		if C > itm[2]:
			maxvalue += itm[0]*itm[2]
			C = C - itm[2]
		else:
			maxvalue += C*itm[0]
			C = 0
			break
	return maxvalue

# Suffix 

items = eval(input())
C = int(input())
print(round(MaxValueSelection(items, C),2))

'''
Input
	
	{1:(10,60),2:(20,100),3:(30,120)}
	50

Output

	240.0

Input
	
	{1:(4,1600),2:(9,2700),3:(10,3500),4:(5,4000),5:(2,1000),6:(2,1200),7:
	(2,1350),8:(9,1800),9:(10,2300),10:(5,1530),11:(2,100),12:(1,120),13:
	(2,1600),14:(3,2700),15:(7,3500),16:(8,4000),17:(1,1000),18:(6,1200),19:
	(1,1350),20:(10,1800),21:(2,2300),22:(10,1530),23:(4,100),24:(1,125)}
	1

Output
	
	1350.0
'''



'''
A task manager receives different tasks at the same or different times in a day, and he follows the
shortest task first strategy to finish tasks to reduce the average waiting time for all tasks.
Each task takes some time to finish, called burst time . At the particular time t , manager select
shortest burst time task to perform next from all task received till time t . The new task only
can be started after the completion of the current running task.

Write a function STF(task) that accept a non-empty list of task in the format [(task_id,
arrival_time, burst_time),...] and returns a list of task_id in which they performed.

	---> If two tasks have the same arrival and burst time, then smaller task_id will perform first.
'''

# Solution 

def STF(task):
	schedule = []
	waiting = []
	tasklist = []
	for i,j,k in task:
		tasklist.append((j,k,i))
	tasklist.sort()
	waiting.append((tasklist[0][1],tasklist[0][0],tasklist[0][2]))
	for t in tasklist:
		if t[0] <= waiting[0][1]:
			if (t[1],t[0],t[2]) not in waiting:
				waiting.append((t[1],t[0],t[2]))
	waiting.sort()
	endtime = waiting[0][1]
	while len(schedule) != len(task):
		schedule.append(waiting[0][2])
		endtime += waiting[0][0]
		waiting.pop(0)
		if waiting == []:
			for t in tasklist:
				if waiting ==[]:
					if t[2] not in schedule:
						waiting.append((t[1],t[0],t[2]))
				else :
					if (t[0] <= waiting[0][1] or t[0] <= endtime) and t[2] not in schedule:
						waiting.append((t[1],t[0],t[2]))
		else:
			for t in tasklist:
				if t[0] <= endtime and t[2] not in schedule:
					if (t[1],t[0],t[2]) not in waiting:
						waiting.append((t[1],t[0],t[2]))
		waiting.sort()
	return schedule

# Suffix 

task = eval(input())
print(STF(task))

'''
Input
	
	[(1,2,6),(2,5,2),(3,1,8),(4,0,3),(5,4,4)]

Output

	[4, 1, 2, 5, 3]

Input
	
	[(1,2,6),(2,5,2),(3,1,8),(4,0,1),(5,4,4),(6,1,7),(7,4,3),(8,5,5)]

Output
	
	[4, 6, 2, 7, 5, 8, 1, 3]

'''




'''

Write a function IsCodeValid(hfcode, message) that accept a dictionary hfcode in which key
represents the character and corresponding value represents the Huffman code for that
character and function accept one more string message (encoded message generated using
Huffman codes). The function returns True if message is valid, otherwise return False .
'''

# Solution

def IsCodeValid(hfcode,message):
	emsg = ''
	huffcode ={}
	maxlength=0
	for i,j in hfcode.items():
		huffcode[j]=i
		if len(j) > maxlength:
			maxlength=len(j)
	cd = ''
	for b in message:
		cd += b
		if len(cd) > maxlength:
			return False
		if cd in huffcode:
			emsg += huffcode[cd]
			cd = ''
	if cd == '':
		return True
	else:
		return False

# Suffix 

hfcode = eval(input())
message = input()
print(IsCodeValid(hfcode,message))

''' 
Input
	
	{'a':'000', 'b':'0010', 'c':'0011', 'd':'01', 'e':'10', 'f':'11'}
	111010111001011100011

Output

	True

Input
	
	{'a':'111', 'b':'000', 'c':'001', 'd':'10', 'e':'110', 'f':'01'}
	111011

Output
	
	False
'''




'''
Write a function IsTreeBalanced(node) that accepts root node node of the binary search tree
and returns True if the tree is balanced, otherwise return False . The tree is balanced if the
absolute value of the balance factor of each node is less than 2.

	---> balance_factor(node) = abs(left height of node - right height of node)
	---> Initially, height of all nodes are None
'''

# Solution

def check(node):
	if node.left == None:
		hl = 0
	else:
		hl = node.left.height
	if node.right == None:
		hr = 0
	else:
		hr = node.right.height
	if abs(hl - hr) > 1:
		return False
	return True

flag = True

def IsTreeBalanced(node):
	global flag
	if node.isempty():
		node.height = 1
	else:
		IsTreeBalanced(node.left)
		IsTreeBalanced(node.right)
		node.height = 1 + max(node.left.height, node.right.height)
		if check(node) == False:
			flag = False
	return flag

# Suffix

class Tree:
	# Constructor:
	def __init__(self,initval=None):
		self.value = initval
		if self.value:
			self.left = Tree()
			self.right = Tree()
			self.height = None
		else:
			self.left = None
			self.right = None
			self.height = None
		return
	
	def isempty(self):
		return (self.value == None)
	
	def isleaf(self):
		return (self.value != None and self.left.isempty() and self.right.isempty())
	
	def insert(self,v):
		if self.isempty():
			self.value = v
			self.left = Tree()
			self.right = Tree()
			self.height = 1
			return
		if self.value == v:
			return
		if v < self.value:
			self.left.insert(v)
		if v > self.value:
			self.right.insert(v)

A = Tree()
nodes = eval(input())
for i in nodes:
	A.insert(i)

print(IsTreeBalanced(A))

'''
Input
	
	[10,5,3,2,20,15,25,30]

Output

	False

Input
	
	[5,4,3,6,7]

Output
	
	True
'''



























