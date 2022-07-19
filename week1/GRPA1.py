'''
Write a function Find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer)
where the size of L is greater than P. The task is to pick P different elements from list L,
where the difference between maximum value and minimum value in selected elements is 
minimum compared to other differences in possible subset of p elements.

The function returns this minimum difference value

Note : the list can contain more than one subset of p elements that have the same minimum value.

Input:
    L = [3,4,1,9,56,7,9,12,13] and p = 5
Output:
    6
'''

def find_Min_Difference(L,P):
  #sort the list
  L.sort()
  N = P
  M = len(L)
  # initalize the min difference with largest difference
  min_diff = max(L) - min(L)
  # Make the window of p elements in sorted list and compare the difference of last an first element of window with `min_diff` if it is less, then update value of `min_diff` with new value and shift window by one and repeat it again and again till last. Finally, we will get minimum difference. 
  for i in range(M-N+1):
    if L[i+N-1] - L[i] < min_diff:
      min_diff = L[i+N-1] - L[i]
  return min_diff

L = [1,2,3,-4,3,2,1,5,-6,7,8,9,10]
P = 6
print(find_Min_Difference(L,P))












