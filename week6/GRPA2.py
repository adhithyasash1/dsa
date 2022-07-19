'''
Write a Python function maxLessThan(root, K), 
that accepts the root node of the binary search tree
and a number K and returns the maximum number
less than or equal to K in the tree. 

If K is the less than every number
in the tree return None . 
Each node in the tree is an object of class Tree,
and the tree will have at least one node.

Input
	50 52 54 74 93 100 114 124 130 143
	92
Output
	74
'''

class Tree:
	#constructor

	def __init__(self, initval = None):
		self.value = initval
		if self.value:
			self.left = self.right = Tree()
		else:
			self.left = self.right = None
		return 

	#only empty node has value None

	def isempty(self):
		return (self.value == None)

	#leaf nodes have both children empty

	def isleaf(self):
		return(self.value != None and self.left.isempty() and self.right.isempty())

	#not a member of class Tree

	def maxLessThan(root, k):
		max = root.value
		temp = root
		while (not temp.isempty()):
			if (temp.value and K<temp.value):
			temp = temp.left
			elif (temp.value and K>=temp.value):
			max = temp.value
			temp = temp.right
		if (K >= max):
		return max
		else:
		return None


#code

class Tree:
  #constructor
  def __init__(self, initval=None):
    self.value = initval
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = self.right = None
    return
  
  #Only empty node has value None
  def isempty(self):
    return(self.value == None)
  
  #Leaf nodes have both children empty
  def isleaf(self):
    return(self.value != None and self.left.isempty() and self.right.isempty())
  
#insert element to BST
def insertToBST(root, x):
  # Tree should have atleast one element.
  temp = root
  while (not temp.isempty()):
    if (x < temp.value):
      temp = temp.left
    else:
      temp = temp.right

  temp.value = x
  temp.left = Tree()
  temp.right = Tree()
def maxLessThan(root, K):
    max = root.value
    temp = root
    while (not temp.isempty()):
        if (temp.value and K<temp.value):
            temp = temp.left
        elif (temp.value and K>=temp.value):
            max = temp.value
            temp = temp.right
    if (K >= max):
        return max
    else:
        return None
L = [int(item) for item in input().split(" ")]
x = int(input())
root = Tree(L[0])
for item in L[1:]:
  insertToBST(root, item)

print(maxLessThan(root, x))
