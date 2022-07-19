'''
For a pattern p, some integer x, p^x refers to x repetitions of p, for example ab^3 = ababab, 
abc^2 = abcabc

Write a python function findContinuousRepetitions(t, p) which accepts a text t and a pattern p 
and returns the maximum value of x such that p^x is a substring of t.
'''

def findContinuousRepetitions(t, p):
  last = {} # Preprocess
  m = len(p)
  for i in range(m):
    last[p[i]] = i
  poslist, i, count, maxR = [], 0, 0, 0 # Loop
  
  while i <= (len(t)-m):
    matched,j = True,len(p)-1
    poslist.append(i)
    while j > 0 and matched:
      if t[i+j] != p[j]:
        matched = False
        count = 0
      j = j - 1
    if matched:
      count += 1
      if (count > maxR): maxR = count 
      i = i + m
    else:
      j = j + 1
      if t[i+j] in last.keys():
        i = i + max(j-last[t[i+j]],1)
      else:
        i = i + j + 1
  return maxR

'''
Input
    abcdabababcdabab
    ab
Output
    3

Input
    euoorujifuEJiecjwbEJibmaouEJiEJiEJiEJiEJiEJiEJiqhykzEJiEJiEJi
    EJi
Output
    7
'''


# My Response

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
    if len(match) > 0: 
        return(match)
    else:
        return None

def findContinuousRepetitions(t, p):
    l = [ ]
    x = find_kmp(t, p)
    l.append(p)
    i = p
    while x != None:
        p = p + i
        x = find_kmp(t, p)
        l.append(p)
    return len(l)-1

t = input()
p = input()
print(findContinuousRepetitions(t, p))

