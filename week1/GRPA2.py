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
                
    













