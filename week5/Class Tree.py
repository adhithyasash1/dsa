class Tree:
    # Constructor:
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
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
            return (self.value != None and 
                    self.left.isempty() and 
                    self.right.isempty())
        
class Tree:
    # Inorder traversal
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+
                   [self.value]+
                   self.right.inorder())
    # Display Tree as a string
    def __str__(self):
        return(str(self.inorder()))
    
class Tree:
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
        
class Tree:
    def minval(self):
        if self.left.isempty():
            return(self.value)
        else:
            return(self.left.minval())
    def maxval(self):
        if self.right.isempty():
            return(self.value)
        else:
            return(self.right.maxval())
        
class Tree:
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
    
class Tree:
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
    
    
class Tree:
    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right

        newleft = Tree(v)
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

        newright = Tree(v)
        newright.left = tlr
        newright.right = tr

        self.value = vl
        self.left = tll
        self.right = newright
        return

class Tree:
    def height(self):
        if self.isempty():
            return(0)
        else:
            return(1 + max(self.left.height(), self.right.height())

class Tree:
    def insert(self,v):
        if v < self.value:
            self.left.insert(v)
            self.left.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)
            return
        if v > self.value:
            self.right.insert(v)
            self.right.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)
            return