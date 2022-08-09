class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue == [])
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)

def fun(Q):
    if (not Q.isempty()):
        i = Q.dequeue()
        fun(Q)
        Q.enqueue(i)

Q = Queue()

Q.queue=[12,24,20,6,12,8,16] # Initial Queue

fun(Q)
print(Q.queue)
print(Q.queue[2])