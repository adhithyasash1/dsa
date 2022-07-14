'''
Boyer-Moore Algorithm

a) Initialize last[c] for each c in p 
	Single scan, rightmost value is recorded 

b) Nested loop, compare each segment t[i:i + len(p)] with p 

c) If p matches, record and shift by 1 

d) We find a mismatch at t[i + j] 
		If j > last[t[i + j]], shift by j - last[t[i + j]] 

		If last[t[i + j]] > j, shift by 1 
			Should not shift p to left!

		If t[i + j] not in p, shift by j + 1

--> Worst case complexity remains : O(mn)

But efficient in everyday practice, almost always works in best case scenario
'''

def boyermoore(t,p):
    last = {} # Preprocess
    for i in range(len(p)):
        last[p[i]] = i
    poslist=[]
    i = 0
    while i <= (len(t)-len(p)):
        matched,j = True,len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j = j - 1
        if matched:
            poslist.append(i)
            i = i + 1
        else:
            j = j + 1
            if t[i+j] in last.keys():
                i = i + max(j-last[t[i+j]],1)
            else:
                i = i + j + 1
    return(poslist)

print(boyermoore('abcaaacabc','abc'))


