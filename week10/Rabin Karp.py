'''
Rabin-Karp Algorithm

--> Suppose Σ = {0, 1, . . . , 9} 
--> Any string over Σ can be thought of as a number in base 10 
--> Pattern p is an m-digit number (nP)  
--> Each substring of length m in the text t is again an m-digit number 
--> Scan t and compare the number (nB) generated by each block of m letters with the pattern number (nP)
'''

def rabinkarp(t,p):
    poslist = []
    numt,nump = 0,0
    for i in range(len(p)):
        numt = 10*numt + int(t[i])
        nump = 10*nump + int(p[i])
    if numt == nump:
        poslist.append(0)
    for i in range(1,len(t)-len(p)+1):
        numt = numt - int(t[i-1])*(10**(len(p)-1))
        numt = 10*numt + int(t[i+len(p)-1])
        if numt == nump:
            poslist.append(i)
    return(poslist)

print(rabinkarp('233323233454323','23'))