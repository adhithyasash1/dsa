'''
Write a python function combinationSort(strList) that takes a list of unique strings as argument,
where each string is a combination of a letter from a to z and a number from 0 to 99, 
the initial character in string being the letter.

ex : d34, g54, d12, b87, g1, c65, g40, g5, d77

this function should sort the list and return two lists (L1, L2) in the order mentioned below

L1 : First list should contain all strings sorted in ascending order with respect to
     first character only, all the strings with same initial character should be in the same 
     order as in the original list.

L2 : In the list L1 above, sort the strings starting with the same character, in descending 
     with respect to the number formed by the remaining characters.
'''


def combinationSort(L):
    L1 = [ ]
    for i in L:
        L1.append((i[0], i[1:]))
    L2 = sorted(L1, key = lambda x: x[0])
    L1= [ ]
    L1 = [i[0] + i[1] for i in L2]
    L3 = sorted(L1, key = lambda x: int(x[1:]), reverse = True)
    L4 = sorted(L3, key = lambda x: x[0])
    return L1, L4
