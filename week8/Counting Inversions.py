'''
Divide and conquer example

Counting inversions

1) Compare your profile with other customers 

2) Identify people who share your likes and dislikes 

3) No inversions – rankings identical 

4) Every pair inverted – maximally dissimilar 

5) Number of inversions ranges from 0 to n(n – 1) / 2 

6) An inversion is a pair (i, j), i < j, where j appears before i 

7) Recurrence: 2T(n/2) + n = O(nlogn)

'''

def mergeAndCount(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k,count) = ([],0,0,0,0)
    while k < m+n:
        if i == m:
            C.append(B[j])
            j += 1
            k += 1
        elif j == n:
            C.append(A[i])
            i += 1
            k += 1
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
            k += 1
        else:
            C.append(B[j])
            j += 1
            k += 1
            count += m-i            
    return(C,count)

def inversionCount(A):
    n = len(A)
    if n <= 1:
        return(A,0)
    (L,countL) = inversionCount(A[:n//2])
    (R,countR) = inversionCount(A[n//2:])
    (B,countB) = mergeAndCount(L,R)
    return(B,countL + countR + countB)
L = [2, 4, 3, 1, 5]
print(inversionCount(L)[1])


'''
Your Ranking : [1, 2, 3, 4, 5]

Your Friend's Ranking : L

Output : 

4 # 4 is the number of inversions

'''