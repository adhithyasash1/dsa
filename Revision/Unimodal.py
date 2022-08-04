# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, arr):
        s, e = 0, len(arr) - 1
        while s < e:
            m = s + (e - s) // 2
            if arr[m] > arr[m + 1]:
                e = m
            else:
                s = m + 1
        # here s == e
        return e
