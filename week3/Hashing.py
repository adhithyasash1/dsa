class Hashing:
  def __init__(self,m):
    self.hashtable = []
    for i in range(m):
        self.hashtable.append(None)     
    self.m = m
  
  def hashfunction(self, data):
    	i = 0
    	key = (((data) % self.m + i ) % self.m)
    	while self.hashtable[key] != None and i < self.m:
    		key = (((data) % self.m + i ) % self.m)
    		i += 1
    	return key
  
  def store_data(self, data):
	    if self.hashtable.count(None) != 0:
		    key = self.hashfunction(data)
		    self.hashtable[key] = data
	    else:
		    print('Hash table is full')

  def display_hashtable(self):
	    return self.hashtable
    
m = 11
data=[24, 36, 58, 65, 62, 79]
A = Hashing(m)
for i in data:
	A.store_data(i)
print(A.display_hashtable())