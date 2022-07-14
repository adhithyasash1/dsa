'''
for a given AVL Tree, write a method to insert(self, v) to
create a height balanced tree after insertion of the
element v
'''

# Solution 

class AVLTree:
    # Constructor:
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
        else:
            self.left = None
            self.right = None
            self.height = 0
        return

    def isempty(self):
        return (self.value == None)

    def isleaf(self):
        return (self.value != None and self.left.isempty() and self.right.isempty())

    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right
        newleft = AVLTree(v)
        newleft.left = tl
        newleft.right = trl
        self.value = vr
        self.right = trr
        self.left = newleft
        return
    
    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tll = self.left.left
        tlr = self.left.right
        tr = self.right
        newright = AVLTree(v)
        newright.left = tlr
        newright.right = tr
        self.right = newright
        self.value = vl
        self.left = tll
        return
    
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
            return        
        if self.value == v:
            return        
        if v < self.value:
            self.left.insert(v)
            self.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)            
        if v > self.value:
            self.right.insert(v)
            self.rebalance()            
            self.height = 1 + max(self.left.height, self.right.height)    
                              
    def rebalance(self):
        if self.left == None:
            hl = 0
        else:
            hl = self.left.height
        if self.right == None:
            hr = 0
        else:
            hr = self.right.height                        
        if  hl - hr > 1:
            if self.left.left.height > self.left.right.height:
                self.rightrotate()
            if self.left.left.height < self.left.right.height:
                self.left.leftrotate()
                self.rightrotate()
            self.updateheight()        
        if  hl - hr < -1:
            if self.right.left.height < self.right.right.height:
                self.leftrotate()
            if self.right.left.height > self.left.right.height:
                self.right.rightrotate()
                self.leftrotate()
            self.updateheight()
            
    def updateheight(self):
        if self.isempty():
            return
        else:
            self.left.updateheight()
            self.right.updateheight()
            self.height = 1 + max(self.left.height, self.right.height)
    
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+ [self.value]+ self.right.inorder())
    
    def preorder(self):
        if self.isempty():
            return([])
        else:
            return([self.value] + self.left.preorder()+  self.right.preorder())
    
    def postorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.postorder()+ self.right.postorder() + [self.value])

A = AVLTree()
nodes = eval(input())
for i in nodes:
    A.insert(i)

print(A.inorder())
print(A.preorder())
print(A.postorder())

'''
Input 
	[10,15,20,5,4,12,25,30]
Output
	[4, 5, 10, 12, 15, 20, 25, 30]
	[10, 5, 4, 15, 12, 25, 20, 30]
	[4, 5, 12, 20, 30, 25, 15, 10]

Input
	[100,50,25,125,150,175,15,10,5,200]
Output
	[5, 10, 15, 25, 50, 100, 125, 150, 175, 200]
	[125, 15, 10, 5, 50, 25, 100, 175, 150, 200]
	[5, 10, 25, 100, 50, 15, 150, 200, 175, 125]
'''
