'''
def gcd(m, n):
    ans = [ ]
    for i in range(1, min(m, n)+1):
        if m % i == 0 and n % i == 0:
            ans.append(i)
    return ans[-1]

def gcd(m, n):
    for i in range(1, min(m, n)+1):
        if m % i == 0 and n % i == 0:
            ans = i
    return ans
'''

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

def firstprimes(n):
    count, i, ans = 0, 1, [ ]
    while count < n:
        if prime(i):
             count, ans = count+1, ans+[i]
        i = i + 1
    return ans

def prime_a(n):
    ans = True
    for i in range(2, n):
        if n % i == 0:
            ans = False
            break
    return ans
        
def prime_b(n):
    result,i = True,2
    while result and i < n:
        if n % i == 0:
            result = False
            break
        i = i + 1
    return result

import math
def prime_c(n):
    result,i = True,2
    while result and i < math.sqrt(n):
        if n % i == 0:
            result = False
            break
        i = i + 1
    return result

def prime_diff(n):
    lastprime = 2
    ans = { }
    for i in range(3, n+1):
        if prime(i):
            d = i - lastprime
            lastprime = i
            if d in ans.keys():
                ans[d] += 1
            else:
                ans[d] = 1
    return ans
'''

def gcd(m, n):
    a, b = max(m, n), min(m, n)
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


    
    





















