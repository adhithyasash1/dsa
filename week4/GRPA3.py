'''
Long journey
A tourist wants to travel around India from north to south. He has a policy that he never travels
back towards the north. Write a Python function longJourney (AList) to find him a route with

which he can visit the maximum number of cities according to his policy, where AList represents
a graph of cities and routes between them. Every edge in adjacenty list AList is a feasible route
between one city to another from north to south. The function should return a list in the order
the cities are to be visited to visit maximum cities.

'''

AList = {'Madurai': ['Cochin', 'Kanyakumari'],
 'Vaishali': [],
 'Varanasi': ['Khajuraho', 'Bodhgaya'],
 'Thiruvanandhapuram': ['Kanyakumari'],
 'Udaipur': ['Gir', 'Ajanta'],
 'Rishikesh': ['Delhi'],
 'Shimla': ['Rishikesh'],
'Bangalore': ['Chennai', 'Madurai'],
'Agra': ['Ranthambore'],
'Ellora': ['Aurangabad'],
'Bodhgaya': ['Kolkatta'],
'Cochin': ['Thiruvanandhapuram'],
'Pushkar': ['Udaipur', 'Ranthambore'],
'Gir': [],
'Aurangabad': ['Mumbai'],
'Kolkatta': ['Ajanta', 'Bangalore', 'Chennai'],
'Chennai': ['Madurai'],
'Sravasti': ['Kushinagar'],
'Leh': ['Shimla'],
'Sarnath': ['Varanasi'],
'Delhi': ['Jaipur', 'Agra', 'Sravasti'],
'Goa': ['Cohin', 'Bangalore'],
'Kanyakumari': [],
'Kushinagar': ['Sarnath', 'Vaishali'],
'Khajuraho': ['Ajanta'],
'Jaipur': ['Pushkar'],
'Mumbai': ['Goa'],
'Ajanta': ['Ellora', 'Aurangabad']}

def DFSInitList(AList):
    # Initialization
    (visited,parent) = ({},{})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return(visited,parent)

def DFSList(AList,visited,parent,v):
    visited[v] = True
    for k in AList[v]:
        if k in visited.keys():
            if (not visited[k]):
                parent[k] = v
                (visited,parent) = DFSList(AList,visited,parent,k)                
    return(visited,parent)

def cities_reached(visited):
    ans = [ ]
    for key, values in visited.items():
        if visited[key] == True:
            ans.append(key)
    return ans

def get_keys(AList):
    ans = [ ]
    for key in AList.keys():
        ans.append(key)
    return ans
    
def longJourney(AList):
    maxi = []
    cities_reached = []
    cities = get_keys(AList)
    for i in cities:
        visited, parent = DFSInitList(AList)
        visited, parent = DFSList(AList,visited,parent,i)
        cities_reached = cities_reached(visited)
        if len(cities_reached) >= len(maxi):
                maxi = cities_reached
    return maxi

# Solution 2

def longJourney(Alist):
    visited = {}
    for i in Alist.keys():
        visited[i] = False
    
    cities = []
    def DFS(s,path):
        visited[s] = True
        if path == []:
            path.append(s)
        for k in Alist[s]:
            if not visited[k]:
                DFS(k,path+[k])
        path.append(s)
        cities.append(path)
        path.pop()
        visited[s] = False
        
    
    DFS('Leh',path=[])
    max = 0
    index = 0
    for i in range(len(cities)):
        if len(cities[i]) > max:
            max = len(cities[i])
            index = i
    return cities[index]

# Solution 3

# A Queue class to keep track of the visited nodes
class Queue:
  def __init__(self):
    self.queue = []

  def addq(self, v):
    self.queue.append(v)

  def delq(self):
    v = None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
      return v

  def isempty(self):
    return self.queue == []

  def __str__(self):
    return str(self.queue)
 
# Dictionary inversion for d which has list as values
def dInv(d): 
  d_ = {}
  if not isinstance(list(d.values())[0], list):
    for k, v in d.items():
      if v not in d_:
        d_[v] = []
      d_[v].append(k)
    return d_

  if isinstance(list(d.values())[0], list):
    for k, v in d.items():
      for v_ in v:
        if v_ not in d_:
          d_[v_] = []
        d_[v_].append(k)
    return d_

# Longest path function from the lecture
def longestpathlist(AList): 
  indegree, lpath = {}, {}
  for u in AList:
    indegree[u], lpath[u] = 0, 0
  for u in AList:
    for v in AList[u]:
      indegree[v] = indegree[v] + 1
  
  zerodegreeq = Queue()
  for u in AList:
    if indegree[u] == 0:
      zerodegreeq.addq(u)
  
  while not zerodegreeq.isempty():
    j = zerodegreeq.delq()
    indegree[j] = indegree[j] - 1
    for k in AList[j]:
      indegree[k] = indegree[k] - 1
      lpath[k] = max(lpath[k], lpath[j] + 1)
      if indegree[k] == 0:
        zerodegreeq.addq(k)
  return lpath
  
def longJourney(AList):
  lpath = longestpathlist(AList) # longest path (dict)
  IAList = dInv(AList) # inverse adjacency list to get the reverse graph
  Ilj = dInv(lpath) # longest path as key and list of cities as values

  maxVal = max(lpath.values()) # value of longest path in which the city ends in the longest path
  prev = Ilj[maxVal][0] # last city
  path = [prev] # appending the last city
  for i in range(maxVal, -1, -1): # going backwards from last city to the first city in terms of longest path
    for p in Ilj[i]: # for every city p has the longest path i
      if p in IAList[prev]: 
        path.append(p) # append to path if there is edge from p to prev in AList or edge from prev to p in IAList(reversed graph)
        prev = p
  return path[::-1] # reverse the path since it is computed from the last

