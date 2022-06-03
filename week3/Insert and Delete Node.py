def insert(self, v):
	newnode = Node(v)
	newnode.prev = self.last
	if self.head is None:
		self.next = newnode
		self.prev = newnode
	else:
		self.last.next = newnode
		self.last = newnode

def delete(self, v):
	if self.head is not None:
		if self.head is self.last:
			self.head = None
			self.last = None 

		else:
			self.last  = self.last.prev
			self.last.next = None