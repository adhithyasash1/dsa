# https://leetcode.com/problems/search-in-rotated-sorted-array/
def pbs(arr, target):
    pivot = findPivot(arr, 0, len(arr) - 1)

    # array is not rotated at all
    # just do normal binary search
    if pivot == -1:
        return bs(arr,  0, len(arr) - 1, target)

    if arr[pivot] == target:
        return pivot

    if arr[0] <= target:
        return bs(arr, 0, pivot-1, target)

    return bs(arr, pivot + 1, len(arr)-1, target)

def bs(arr, s, e, target):
    # do this one yourself: just normal binary search
    pass

def findPivot(arr, s, e):
    if e < s:
        return -1

    if e == s:
        return e

    m = s + (e - s) // 2

    if m < e and arr[m] > arr[m+1]:
        return m
    if m > s and arr[m] < arr[m-1]:
        return m-1

    if arr[s] >= arr[m]:
        return findPivot(arr, s, m-1)

    return findPivot(arr, m+1, e)
