'''
Given a 2D matrix M where each cell M[i][j] contains some number of coins, find a path to collect maximum coins from cell (x1, y1) to cell (x2, y2) in matrix M where x2 >= x1 and y2 >= y1. 

You can only travel one step right or one step down in each move. 

Write a function MaxCoinsPath(M, x1, y1, x2, y2) that accepts a matrix M, index (x1, y1) and index (x2, y2) of the destination cell in matrix M. The funciton should return the maximum number of coins collected across all paths from source to destination. 
'''

# Solution

def MaxCoinPath(M,x1,y1,x2,y2):
    MCP=[]
    
    # Create matrix same size of M and initialized with 0
    for i in range(len(M)):
        L = []
        for j in range(len(M[0])):
            L.append(0)
        MCP.append(L)
    
    # Initialize x1 row and y1 coloumn    
    MCP[x1][y1] = M[x1][y1]
    for i in range(y1+1,len(M[0])):
        MCP[x1][i]= MCP[x1][i-1] + M[x1][i]
    for i in range(x1+1,len(M)):
        MCP[i][y1]= MCP[i-1][y1] + M[i][y1]
	
	# Calculate value for each cell
    for i in range(x1+1,len(M)):
        for j in range(y1+1,len(M[0])):
            MCP[i][j] = max(MCP[i-1][j],MCP[i][j-1]) + M[i][j]
    
    # Return max coin value at x2,y2
    return MCP[x2][y2]

M = eval(input())
(x1,y1)= eval(input())
(x2,y2) = eval(input())
print(MaxCoinPath(M,x1,y1,x2,y2))


'''
Input
	[[2,1,3,2,5],[3,5,2,4,6],[7,6,1,3,2],[2,9,4,7,8],[1,4,5,11,3]]
	(0,0)
	(4,4)
Output
	52

Input
	[[20,15,31,21,5],[13,15,22,14,26],[27,6,11,13,12],[32,29,4,27,8],[10,4,15,18,10]]
	(0,0)
	(3,3)
Output
	152
'''
