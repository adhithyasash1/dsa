'''
Write a function MakePalindrome(s) that accepts a non-empty string s of  letters
in lowercase and without spaces. 

The function returns the smallest string that converts s into a palindrome 
by adding it on the front of s. If input string s is already a palindrome, then
return None. Try to given an O(n) solution.
'''

# Solution 1

def kmp_fail(p):
# Initialize
    m = len(p)
    fail = [0 for i in range(m)]
# Update
    j,k = 1,0
    while j < m:
        if p[j] == p[k]: #k+1 chars match
            fail[j] = k+1
            j,k = j+1,k+1
        elif k > 0: #find shorter prefix
            k = fail[k-1]
        else: #no match found at j
            j = j+1
    return(fail[-1])

def MakePalindrome(s):
    if len(s)==0:
        return s
    m = kmp_fail(s + '#' + s[::-1])
    if m == len(s):
        return None        
    else:
        return s[m:][::-1]
s = input()
print(MakePalindrome(s))

# Solution 2

def isPalindrome(s):
    l = len(s)
    i = 0
    j = l-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return (True)
    
def MakePalindrome(s):
    k = s
    cnt = 0
    Flag = False
    
    while len(s) > 0:
        
        if (isPalindrome(s)):
            Flag = True
            break
        
        else:
            cnt += 1
            s = s[:-1]
    
    if cnt == 0:
        return None
    else:
        return k[::-1][:cnt]

s = input()
print(MakePalindrome(s))

'''
Input
	abcdefghijk
Output
	kjihgfedcb

Input
	bcdefghijkllkjihgfedcba
Output
	a

Input
	abcdefghijklmnopqrstuvwxyz
Output
	zyxwvutsrqponmlkjihgfedcb
'''




