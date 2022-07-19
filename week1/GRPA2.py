'''
Goldbach's conjecture is one of the oldest and best-known unsolved problems in number
theory. It states that every even number greater than 2 is the sum of two prime numbers.
For Example:
12 = 5 +7

26 = 3 + 23 or 7 + 19 or 13 +13
Write a function Goldbach(n) where in is a positive even number(n > 2 ) that returns a list of
tuples. In each tuple (a, b) where a <= b, a and b should be prime numbers and the sum of

a and b should be equal to n .

Input:
    1 12
Output:
    [(5,7)]

Input:
    26
Output:
    [(3, 23) , (7, 19) , (13,13) ]
'''


def factors(n):
    ans = [ ]
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans

def prime(n):
    return factors(n) == [1, n]

def primes_upto(n):
    ans = [ ]
    for i in range(1, n):
        if prime(i):
            ans.append(i)
    return ans

def goldbach(z):
    ans = primes_upto(z)
    res = [ ]
    for i in ans:
        for j in ans:
            if i + j == z:
                if (j,i) not in res:
                    res.append((i,j))
    return res
                
    
                
    













