class DisjointSet: 
    def __init__(self, n):
        self.MAKESET(n)
    
    def MakeSet(self, n):
        self.S = [-1 for x in range(n)]

    def Find(self, X):
        if( self.S[X] < 0 ): 
            return X
        else:
            return self.FIND(self.S[X])

    def Union(self, root1, root2):
        if self.FIND(root1) == self.FIND(root2):
            return
        if self.S[root2] < self.S[root1]:
            self.S[root2] += self.S[root1] 
            self.S[root1] = root2
        else:
            self.S[root1] += self.S[root2]
            self.S[root2] = root1

    def FindBySize(self, X):
         if( self.S[X] < 0 ): 
            return X
         else:
            self.S[X] = FINDBYSIZE(self.S[X])
            return self.S[X]




