'''
A popular meeting hall in a city receives many overlapping applications to hold meetings. The manager wishes to satisfy as many customers as possible. Each application is a tuple (id, start_day, end_day) where id, start_day and end_day are the unique id assigned to the application, starting day of the meeting and the ending day of the meeting, ends inclusive respectively. 

Write a function no_overlap(L) to return the list of 
customer ids whose applications are accepted that ensures optimal scheduling. Let L be the list of tuples with (id, start_day, end_day)
'''

# Solution 1

def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index:index+1] + t[:index] + t[index+1:])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1:index+1] + t[0:1] + t[index+1:])
    return L__

def no_overlap(L):
    sortedL = tuplesort(L, 2)
    accepted = [sortedL[0][0]]
    for i, s, f in sortedL[1:]:
        if s > L[accepted[-1]][2]:
            accepted.append(i)
    return accepted


# Solution 2

def no_overlap(L):
    end_day = []
    accepted = []
    prev_mini = 0

    for i in L:
        end_day.append(i[2])

    while len(end_day)>0:
        mini = min(end_day)
        end_day.remove(mini)

        for i in L:
            if i[2] == mini:
                if i[1] > prev_mini:
                    prev_mini = mini
                    accepted.append(i[0])
    return  accepted

'''
Input
	0 1 2
	1 1 3
	2 1 5
	3 3 4
	4 4 5
	5 5 8
	6 7 9
	7 10 13
	8 11 12
Output
	4

Input
	0 4 11
	1 6 10
	2 3 7
	3 2 6
	4 3 7
	5 4 9
	6 4 11
	7 3 9
	8 8 11
	9 3 9
	10 8 12
	11 5 7
	12 9 17
	13 3 11
	14 6 7
	15 8 12
	16 4 12
	17 4 5
	18 6 9
	19 6 8
	20 1 3
	21 10 15
	22 6 8
	23 5 13
	24 2 3
	25 8 10
	26 7 8
	27 10 15
	28 1 5
	29 2 4
	30 2 6
	31 1 8
	32 5 8
	33 2 10
	34 7 12	
	35 3 8
	36 6 13
	37 6 11
	38 6 12
	39 1 8
	40 8 9
	41 8 15
	42 7 15
	43 4 7
	44 8 12
	45 4 10
	46 6 14
	47 9 15
	48 5 13
	49 3 5
Output
	5
'''
