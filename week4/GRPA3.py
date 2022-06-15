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




'''
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
'''  
    

























