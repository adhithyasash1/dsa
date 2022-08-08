class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if nums[i]+nums[j] > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                f = binarysearch(nums, (0 - (nums[i]+nums[j])), j+1,n-1) 
                if f != -1:
                    l = [nums[i]] + [nums[j]] + [nums[f]]   
                    res.append(l)
        return res

def binarysearch(L, v , s , e):
    m = 0
    while s <= e: 
        m = s + (e - s) // 2
        if L[m] < v:
            s = m + 1
        elif L[m] > v:
            e = m - 1
        else:
            return m
    return -1