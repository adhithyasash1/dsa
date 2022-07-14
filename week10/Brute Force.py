# Brute force approach
# Complexity : O(mn)

# Nested scan from left to right in t for p

def stringmatch(t,p):
    poslist = []
    for i in range(len(t)-len(p)+1):
        matched = True
        j = 0
        while j < len(p) and matched:
            if t[i+j] != p[j]:
                matched = False
            j = j+1
        if matched:
            poslist.append(i)
    return(poslist)

print(stringmatch('abababbababbbbababab','abab'))

# Nested scan from right to left in t for p

def stringmatchrev(t,p):
    poslist = []
    for i in range(len(t)-len(p)+1):
        matched = True
        j = len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j = j-1
        if matched:
            poslist.append(i)
    return(poslist)

print(stringmatchrev('abababbababbbbababab','abab'))