'''
Write a Python function KminGreaterThan(arr, k, num), that accepts an unsorted list arr , two
numbers k and num, 

returns True if the kth smallest element in the list arr is greater than or
equal to num, otherwise returns False. 

Try to write a solution that runs O(nlogk) in time.

Example : 
    input :
        66 55 43 34 12 7 2 20 5
        5
        18

    output : 
        True
'''
class max_heap:
    def __init__(self):
        self.size=0
        self.arr = []
    
    def isempty(self):
        return True if (self.size == 0) else False
    
    def max(self):
        return self.arr[0] if self.size>0 else None
    
    # Heapify element at index i
    def heapify_down(self, i):
        n = self.size
        a = self.arr
        while (i<n):
            gg = l = 2 * i + 1
            r = 2 * i + 2
            # gg is greater of left and right child
            if (l<n and r<n and a[l] < a[r]):
                gg = r
            if (gg<n and a[gg] > a[i]):
                a[i], a[gg] = a[gg], a[i]
                i = gg
            else:
                break
    
    def delete_max(self):
        max = self.arr[0]
        last = self.arr.pop()
        #size of heap after pop operation will reduce by 1
        self.size -= 1
        if (self.size > 0):
            self.arr[0] = last
            self.heapify_down(0)
        return max
    
    # Replace max element with x
    def replace_max(self, x):
        max = self.arr[0]
        self.arr[0] = x
        self.heapify_down(0)
        return max
    
    # Heapify last element in the heap
    def heapify_up(self):
        i = self.size - 1
        while (i>0):
            parent = (i-1)//2
            if (self.arr[i] > self.arr[parent]):
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break
    
    # Insert to min heap
    def insert_max_heap(self, x):
        self.arr.append(x)
        self.size += 1
        self.heapify_up()
    
# This function first finds the kth smallest element and than compares it with x
def KminGreaterThan(arr, k, num):
    # Build max heap of size k
    h = max_heap()
    for i in range(k):
        h.insert_max_heap(L[i])
    # Insert the next element in the list if it is smaller than the max in heap.
    # This will ensure that the heap contains k minimum elements from the parsed elements.
    for i in range(k, len(arr)):
        if (h.max() > arr[i]):
            h.replace_max(arr[i])
    return True if (h.max() >= num) else False 

# Suffix 
L = [int(item) for item in input().split(" ")]
k = int(input())
num = int(input())
print(KminGreaterThan(L, k, num))

'''
Function heapSort(arr) sorts the array arr using max heap. 

Complete the function heapify(arr, n, i), that takes three arguments, 
arr is the max heap array, n is the number of elements in heap arr and i is the index of element 
that needs to be heapified and heapifies the array from index 0 to n-1 with respect to element at index i.

Example : 
    input : 
        45 23 6 12 9 1 22 58
    output :
        1 6 9 12 22 23 45 58
'''

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Suffix 
L = [int(item) for item in input().split(" ")]
heapSort(L)
print(*L)

'''
A country's defense organization wants to setup a private fiber network to connect all its camps
around the country which will be disconnected from the INTERNET(world wide web). It wants to
excluding only one camp, which will be connected to the INTERNET. Camps that can be connected
to each other via fiber and the associated cable cost to connect them is given as an adjacency list
representation Alist for all n camp of the company in the format below.

{'camp_1': [(camp_a, cost_1_a), (camp_b, cost_1_b] . . .,
'camp_2': [(camp_c, cost_2_c), (camp_d, cost_2_d) . . .,
.
.
.
'camp_n']: [(camp_x, cost_2_x), (camp_y, cost_2_y) . . .}

In the above Alist , camp_1 can be connected to camp_a with a cable cost of cost_1_a units
and to camp_b with cable cost as cost_1_b units, and so on for all the n camps. The cable cost
two connect any two cities will always be positive.

Write a Python function connectCamps(Alist, exCamp) that accepts the Alist as described
above and a camp exCamp , returns the minimum cost required to connect all the camps
excluding the exCamp . If the camps cannot be connected after excluding exCamp return -1 . The
function will be called to check for the cost excluding each camp one by one so try to make it
efficient that runs in O((m+n)logn) time, where m is the number of pairs of camps that can be
connected.

Example : 
    input : 
        7 # number of camps
        [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),
        (1,3,40),(3,4,60),(2,4,20)] #edges, camps that can be connected and the cost
        associated
        4 # excluded camp

    output :
        190

    input :
        8 # number of camps
        [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),
        (1,3,40),(3,4,60),(2,4,20),(6,7,77)] #edges, camps that can be connected and
        the cost associated
        6 # excluded camp

    output : 
        -1
'''

from collections import deque
# Helper function
class myStack:
    def __init__(self):
        self.Q = deque()

    def pop(self):
        return self.Q.pop()

    def push(self, x):  
        return self.Q.append(x)

    def isempty(self):
        return False if self.Q else True

# Checks using BFS if the graph is connected excluding the node exCamp
def isConnectedExcluding(Alist, exCamp):
    vertices = [v for v in Alist.keys() if v!=exCamp]
    visited = {k:False for k in vertices}
    st = myStack()
    st.push(vertices[0])
    while not st.isempty():
        curr = st.pop()
        visited[curr] = True
        for (v, d) in Alist[curr]:
            if (v != exCamp and not visited[v]):
                st.push(v)
    # Check if all are visited
    return all(value == True for value in visited.values())
# Do not remove the site from graph, rather exclude it from each comparision and calculation.

def connectSites(Alist, exCamp):
    # Check if the graph is connected
    if not isConnectedExcluding(Alist, exCamp):
        return -1
    edges, te = [], []
    components, members, size = {}, {}, {}
    minCost = 0
    # Create edge list and union find data structure excluding exCamp connected edges
    for u in Alist.keys():
        if (u != exCamp):
            edges.extend([(d,u,v) for (v,d) in Alist[u] if v!=exCamp])
            components[u], members[u], size[u] = u, [u], 1
    edges.sort()
    # For undirected graph remove duplicate edges
    distinctEdges = [edges[0]]
    for i in range(len(edges)-1):
        if not ((edges[i][0] == edges[i+1][0])
            and edges[i][1]==edges[i+1][2] and edges[i][2]==edges[i+1][1]):
            distinctEdges.append(edges[i+1])
    edges=distinctEdges
    
    # Calculate MST and minimum cost
    for (d,u,v) in edges:
        if (components[u] != components[v]):
            te.append((u,v))
            minCost += d
            c_old = components[u]
            c_new = components[v]
            for k in members[c_old]:
                components[k] = c_new
                members[c_new].append(k)
                size[c_new] += 1
    return minCost

# Suffix 
size = int(input())
edges = eval(input())
exCamp = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(connectSites(WL, exCamp))


