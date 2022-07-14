'''
Python program to find first and last occurrences of a number in a given sorted list
 
if x is present in L then returns the index of First Occurrence of x in L[0,...,n-1], 
otherwise value is None

if x is present in L then returns the index of Last Occurrence of x in L[0,...,n-1], 
otherwise value is None

'''

def first(L, low, high, x, n) :
    if(high >= low) :
        mid = low + (high - low) // 2
        if(( mid == 0 or x > L[mid - 1]) and L[mid] == x) :
            return mid
        elif (x > L[mid]) :
            return first(L, (mid + 1), high, x, n)
        else :
            return first(L, low, (mid - 1), x, n)
     
    return None

def last(L, low, high, x, n) :
    if (high >= low) :
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < L[mid + 1]) and L[mid] == x) :
            return mid
        elif (x < L[mid]) :
            return last(L, low, (mid - 1), x, n)
        else :
            return last(L, (mid + 1), high, x, n)
             
    return None
     
def findOccOf(L, x):
    n = len(L)
    First = first(L, 0, n - 1, x, n)
    Last = last(L, 0, n - 1, x, n)
    return (First, Last)

L = [3, 3, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9, 10, 10, 11, 13, 14, 14, 14, 14, 14, 14]
print(findOccOf(L, 5))