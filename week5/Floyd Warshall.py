''' 
Order of Complexity = O(n^3) 

No improvement in complexity even if the input is in Adjacency List

we only need the previous slice in order to compute the current slice

which reduces the Space Complexity to O(n^2)

''' 

def floydwarshall(WMat):
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat)*rows*rows + 1
    # setting up shortest path matrix
    # SP = zero matrix with with 'n' rows, 'n' columns and n+1 dimensions in terms of stages of iterations 
    SP = np.zeros(shape=(rows,cols,cols+1))
    # first stage we construct SP[0] matrix, initialize all values to infinity 
    for i in range(rows):
        for j in range(cols):
            SP[i,j,0] = infinity
    # for every i-j edge (direct edge) in SP[0] matrix
    # we set the value in our SP matrix to be the weight of that direct edge between i-j
    # we create the first stage of SP matrix 
    # direct edge recorded weights in SP matrix, is the first stage: SP[0](i, j) 
    for i in range(rows):
        for j in range(cols):
            # WMat[i,j,0] tells me whether there is an edge from i to j or not
            # WMat[i,j,1] gives me the edge weight if there is an edge from i to j
            if WMat[i,j,0] == 1:
                SP[i,j,0] = WMat[i,j,1]
    # from 1 to n, we run every pair (i, j) and for every k, we either keep the shortest path
    # or we update the shortest path thru (i, k) to (k, j) 
    # new path whose weight is shorter by going thru (k-1) edges
    for k in range(1,cols+1):
        for i in range(rows):
            for j in range(cols):
                # we take the minimum of ( what is already exists as shortest path or 
                # new shortest path computed by going thru (k-1) edges [lesser weight] )
                # --> min of ( SP[k-1](i, j) or SP[k-1](i, k) + SP[k-1](k, j) )
                SP[i,j,k] = min(SP[i,j,k-1],
                                SP[i,k-1,k-1]+SP[k-1,j,k-1])
    # return the last stage of iteration (one at index 'n')
    return(SP[:,:,cols])


''' 
order of time complexity is (n^3): 

running 3 nested loops for stabilizing the matrix

order of space complexity is (n^2): 

since, we do not need SP[0](i, j) to compute SP[2](i, j)
we need only the previous stage which is SP[1](i, j) { to calculate SP[1](i, j), we need SP[0](i, j) } 
in this way we can pop off the stages once we have calculated the next stage. 

'''