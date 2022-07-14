'''
Knuth-Morris-Pratt algorithm

a) Compute the automaton for p efficiently 

b) Match p against itself 
		match[j] = kif suffix of p[:j+1] matches prefix p[:k] 

c) Suppose suffix of p[:j+1] matches prefix p[:k]
		If p[j+1] == p[k], extend the match 
		
		Otherwise try to find a shorter prefix that can be extended by p[j+1] 

d) Usually refer to match as failure function fail 
		Where to fall back if match fails

Computing the fail function : 

a) Initialize fail[j] = 0 for all j 

b) k keeps track of length of current match 

c) j is next position to update fail 

d) If p[j] == p[k] extend the match, set fail[j] = k+1 

e) If p[j] != p[k] find a shorter prefix that matches suffix of p[:j] 
		Step back to fail[k-1]

f) If we don’t find a nontrivial prefix to extend, retain fail[j] = 0, move to next position

Implementation of KMP algorithm : 

--> Scan t from beginning 
--> j is next position in t 
--> k is currently matched position in p 
--> If t[j] == p[k] extend the match 
--> If t[j] != p[k], update match prefix 
--> If we reach the end of the while loop, no match

Analysis : 

--> The Knuth, Morris, Pratt algorithm efficiently computes the automaton describing prefix matches in the pattern p 
--> Complexity of preprocessing the fail function is O(m)
--> After preprocessing, can check matches in the text t in O(n)
--> Overall, KMP algorithm works in time O(m + n)

'''

def kmp_fail(p):
    m = len(p)
    fail = [0 for i in range(m)]
    j,k = 1,0
    while j < m:
        if p[j] == p[k]:
            fail[j] = k+1
            j,k = j+1,k+1
        elif k > 0:
            k = fail[k-1]
        else:
            j = j+1
    return(fail)

def find_kmp(t, p):
    match =[]
    n,m = len(t),len(p)
    if m == 0:
        match.append(0)
    fail = kmp_fail(p)
    j = 0
    k = 0
    while j < n:
        if t[j] == p[k]:
            if k == m - 1:
                match.append(j - m + 1)
                k = 0
            else:
                j,k = j+1,k+1
        elif k > 0:
            k = fail[k-1]
        else:
            j = j+1
    return(match)

print(find_kmp('ababaabbaba','aba'))