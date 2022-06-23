class Tree:
    # Constructor:
    def __init__(self, initval = None):
        self.value = initval
        if self.value: # if there is a leaf node then it should point to two empty trees for initialization
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return
    
    # Only empty node has value None
    def isempty(self):
        return (self.value == None)
    
    # Leaf nodes have both children empty
    def isleaf(self): 
        return (self.value != None and self.left.isempty() and self.right.isempty())
    
    # Inorder traversal
    def inorder(self): # Enumerate in sorted order
        if self.isempty(): 
            return([])
        else: # Recursively apply inorder traversal, (recursively) take all values in the LHS, take singleton value in middle, take all values from RHS, put them all in a list and return them
            return(self.left.inorder()+[self.value]+self.right.inorder())
        # Display Tree as a string
    
    def __str__(self):
        return(str(self.inorder()))
    
    # Check if value v occurs in tree
    def find(self,v):
        if self.isempty():
            return(False)
        if self.value == v:
            return(True)
        if v < self.value:
            return(self.left.find(v))
        if v > self.value:
            return(self.right.find(v))
    
    # return minimum value for tree rooted on self - Minimum is left most node in the tree
    def minval(self):
        if self.left.isempty():
            return(self.value)
        else:
            return(self.left.minval())
    
    # return max value for tree rooted on self  - Maximum is right most node in the tree
    def maxval(self):
        if self.right.isempty():
            return(self.value)
        else:
            return(self.right.maxval())
    
    # insert new element in binary search tree
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            return
        if v > self.value:
            self.right.insert(v)
            return
    
    # delete element from binary search tree
    def delete(self,v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            elif self.right.isempty():
                self.copyleft()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
    
    # Convert leaf node to empty node
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return
    
    # Promote left child
    def copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left = self.left.left
        return
    
    # Promote right child
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return

    

T = Tree()
bst = [9,8,7,6,5,4,3,2,1]
k = 4
for i in bst:
    T.insert(i)
print('Element in BST are:= ',T.inorder())
print('Maximum element in BST are:= ',T.maxval())
print('Minimum element in BST are:= ',T.minval())
print(k,'is present or not = ',T.find(k))
T.delete(3)
print('Element in BST after delete 3:= ',T.inorder())

'''
Output : 

Element in BST are:=  [1, 2, 3, 4, 5, 6, 7, 8, 9]
Maximum element in BST are:=  9
Minimum element in BST are:=  1
4 is present or not =  True
Element in BST after delete 3:=  [1, 2, 4, 5, 6, 7, 8, 9]
''' 