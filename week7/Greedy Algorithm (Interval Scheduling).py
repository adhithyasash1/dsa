'''
Interval scheduling
Scenario example

▪ IIT Madras has a special video classroom for delivering online  lectures 

▪ Different teachers want to book the classroom 

▪ Slots may overlap, so not all bookings can be honored 

▪ Choose a subset of bookings to maximize the number of teachers  who get to use the room 

1) Sort all jobs which based on end time in increasing order.
2) Take the interval which has earliest finish time.
3) Repeat next two steps till you process all jobs.
4) Eliminate all intervals which have start time less than selected interval’s end time.
5) If interval has start time greater than current interval’s end time, at it to set. Set current interval to new interval.

'''

def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index:index+1] + t[:index] + t[index+1:])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1:index+1] + t[0:1] + t[index+1:])
    return L__

def intervalschedule(L):
    sortedL = tuplesort(L, 2)
    accepted = [sortedL[0][0]]
    for i, s, f in sortedL[1:]:
        if s > L[accepted[-1]][2]:
            accepted.append(i)
    return accepted
#(job id,start time, finish time) in each tuple of list L
L = [(0, 1, 2),(1, 1, 3),(2, 1, 5),(3, 3, 4),(4, 4, 5),(5, 5, 8),(6, 7, 9),(7, 10, 13),(8, 11, 12)]
print(len(intervalschedule(L)))

Output : 

4