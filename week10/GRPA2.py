'''
Write a function FindPattern(T, P) which accepts a string T and a string P
where length(P) <= length(T). In pattern P, $ is special symbol that represents 
a single character, that will match any character.

The function returns a list of tuples in the format
	[(start matched index of pattern in T, matched pattenr)]
'''

# Solution

def FindPattern(T,P):
    last = {} # Preprocess
    for i in range(len(P)):
        if P[i] != '$':
            last[P[i]] = i
    poslist=[]
    i = 0 # Loop
    while i <= (len(T)-len(P)):
        matched,j = True,len(P)-1
        while j >= 0 and matched:
            if P[j] != '$':
                if T[i+j] != P[j]:
                    matched = False
            j = j - 1            
        if matched:
            poslist.append((i,T[i:i+len(P)]))
            i = i + 1
        else:
            j = j + 1
            if T[i+j] in last.keys():
                i = i + max(j-last[T[i+j]],1)
            else:
                i = i + 1
    return(poslist)
T = input()
P = input()
print(FindPattern(T,P))

'''
Input
	abcabedsgababcjigdabjhtadce
	ab$$$
Output
	[(0, 'abcab'), (3, 'abeds'), (9, 'ababc'), (11, 'abcji'), (18, 'abjht')]

Input
	abcabedsgababcjigdabjhtadce
	$$$$ab
Output
	[(5, 'edsgab'), (7, 'sgabab'), (14, 'jigdab')]

Input
	abcdacbdcradcebcdabccaceddebbacabbacbdadbbcca
	$d$b$c$
Output
	[(15, 'cdabcca'), (38, 'adbbcca')]

Input
	abccbaabcbacacbaabbccabcaaccbbacbacbacbbcacbacbca
	$$$$$ba$$$
Output
	[(4, 'baabcbacac'), (9, 'bacacbaabb'), (24, 'aaccbbacba'), (27, 'cbbacbacba'), (30, 'acbacbacbb'), (38, 'bbcacbacbc')]
'''
