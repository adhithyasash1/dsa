class minheap:
    def __init__(self):
        self.A = []
    
    def min_heapify(self,k):
        l = 2 * k + 1
        r = 2 * k + 2
        smallest = k
        if l < len(self.A) and self.A[l] < self.A[smallest]:
            smallest = l
        if r < len(self.A) and self.A[r] < self.A[smallest]:
            smallest = r
        if smallest != k:
            self.A[k], self.A[smallest] = self.A[smallest], self.A[k]
            self.min_heapify(smallest)

    def build_min_heap(self,L):
        self.A = []
        for i in L:
            self.A.append(i)
        n = int((len(self.A)//2)-1)
        for k in range(n, -1, -1):
            self.min_heapify(k)

        
    def delete_min(self):
        item = None
        if self.A != []:
            self.A[0],self.A[-1] = self.A[-1],self.A[0]
            item = self.A.pop()
            self.min_heapify(0)
        return item


    def insert_in_minheap(self,d):
        self.A.append(d)
        index = len(self.A)-1
        while index > 0:
            parent = (index-1)//2
            if self.A[index] < self.A[parent]:
                self.A[index],self.A[parent] = self.A[parent],self.A[index]
                index = parent
            else:
                break

'''
heap = minheap()
heap.build_min_heap([6,5,4,3,2])
print(heap.A)
heap.insert_in_minheap(1)
print(heap.A)
heap.insert_in_minheap(8)
print(heap.A)
print(heap.delete_min())
print(heap.delete_min())
print(heap.A)
'''