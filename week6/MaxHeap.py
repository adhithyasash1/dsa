class maxheap:
    def __init__(self):
        self.A = []
    
    def max_heapify(self,k):
        l = 2 * k + 1
        r = 2 * k + 2
        largest = k
        if l < len(self.A) and self.A[l] > self.A[largest]:
            largest = l
        if r < len(self.A) and self.A[r] > self.A[largest]:
            largest = r
        if largest != k:
            self.A[k], self.A[largest] = self.A[largest], self.A[k]
            self.max_heapify(largest)

    def build_max_heap(self,L):
        self.A = []
        for i in L:
            self.A.append(i)
        n = int((len(self.A)//2)-1)
        for k in range(n, -1, -1):
            self.max_heapify(k)

        
    def delete_max(self):
        item = None
        if self.A != []:
            self.A[0],self.A[-1] = self.A[-1],self.A[0]
            item = self.A.pop()
            self.max_heapify(0)
        return item


    def insert_in_maxheap(self,d):
        self.A.append(d)
        index = len(self.A)-1
        while index > 0:
            parent = (index-1)//2
            if self.A[index] > self.A[parent]:
                self.A[index],self.A[parent] = self.A[parent],self.A[index]
                index = parent
            else:
                break

'''
heap = maxheap()
heap.build_max_heap([1,2,3,4,5,6])
print(heap.A)
heap.insert_in_maxheap(7)
print(heap.A)
heap.insert_in_maxheap(8)
print(heap.A)
print(heap.delete_max())
print(heap.delete_max())
print(heap.A)
'''