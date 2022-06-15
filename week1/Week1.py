'''
A positive integer m is a prime product if it can be written as p × q , where p and q are both
primes.

Write a Python function prime_product(m) that takes an integer m as input and returns True if
m is a prime product and False otherwise. (If m is not positive, function should return False .)
'''

def factors(n):
    ans = [ ]
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans

def prime(n):
    return factors(n) == [1, n]

def prime_product(n):
    ans = factors(n)
    res = [ ]
    for i in ans:
        for j in ans:
            if i*j == n:
                res.append((i, j))
    for i in res:
        if prime(i[0]) and prime(i[1]):
            return True
        else:
            pass
    return False
                
'''
Write a function del_char(s,c) that takes strings s and c as input, where c has length 1 (i.e., a
single character), and returns the string obtained by deleting all occurrences of c in s.

If c has length other than 1, the function should return s.
'''

def del_char(s,c):
    st = [ ]
    for i in s:
        st.append(i)
    for i in st:
        if i == c:
            st.pop(st.index(i))
    ans = ''
    for i in st:
        ans += str(i)
    return ans

'''
Write a function shuffle(l1,l2) that takes two lists, 11 and l2 as input, and returns a list
consisting of the first element in l1 , then the first element in l2 , then the second element in
l2 , then the second element in l2 , and so on. If the two lists are not of equal length, the
remaining elements of the longer list are appended at the end of the shuffled output.
'''

def EvaluateExpression(input()):
    string = s.split(' ')
    ans = 0
    stack = [ ]
    for i in string:
        if i.isdigit():
            stack.append(i)
        elif i in '*/+-':
            lol = ''
            B = stack.pop()
            A = stack.pop()
            lol = str(A)+i+str(B)
            ans = eval(lol)
            stack.append(ans)
    return(ans)

'''
Write a function expanding(L) that takes a list of integer L as input and returns True if the
absolute difference between each adjacent pair of elements strictly increases.
'''

def expanding(l):
    if len(l) <= 2:
        return(True)
    diff = abs(l[1]-l[0])
    return(diff < abs(l[2]-l[1]) and expanding(l[1:]))

def expanding_iterative(l):
    if len(l) <= 2:
        return(True)
    olddiff = abs(l[1]-l[0])
    for i in range(2,len(l)):
        newdiff = abs(l[i]-l[i-1])
        if newdiff <= olddiff:
            return(False)
        olddiff = newdiff
    return(True)

# Suffix (Visible)
L = eval(input())
print(expanding(L))

'''
Write a Python function sumsquare(l) that takes a nonempty list of integers as input and returns
a list [odd,even] ,

where odd is the sum of squares all the odd numbers in l and even is the
sum of squares of all the even numbers in l.
'''

def even(n):
    return(n%2 == 0)

def sumsquare(l):
    oddsum = 0
    evensum = 0
    for n in l:
        if even(n):
            evensum += n*n
        else:
            oddsum += n*n
    return([oddsum,evensum])

# Suffix (Visible)
L = eval(input())
print(sumsquare(L))

'''
Write a Python function histogram(l) that takes as input a list of integers with repetitions and
returns a list of pairs as follows :

for each number n that appears in l , there should be exactly one pair (n,r) in the list
returned by the function, where r is the number of repetitions of n in l.

the final list should be sorted in ascending order by r , the number of repetitions. For
numbers that occur with the same number of repetitions, arrange the pairs in ascending
order of the value of the number.
'''

def build_table(l):
    # Use a dictionary to build a frequency table
    frequency = {}
    # For each number, create a new entry in the table or increment the
    for n in l:
        if n in frequency.keys():
            frequency[n] = frequency[n] + 1
        else:
            frequency[n] = 1
    return(frequency)

def sort_table(fdict):
    # First build a list of the form (r,n)
    flist = [ (fdict[n],n) for n in fdict.keys() ]
    # Sort this list using built in sort, which will sort first by frequency, then by value
    flist.sort()
    # Flip each pair and return
    return( [ (n,r) for (r,n) in flist ])

def histogram(l):
    frequency_table = build_table(l)
    return(sort_table(frequency_table))

# Suffix code(Visible)
L=eval(input())
print(histogram(L))



