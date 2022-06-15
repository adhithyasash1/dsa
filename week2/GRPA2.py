def findMax(arr, low, high):
    if (high == low):
        return arr[low]

    mid = low + (high - low) // 2
    if(mid==0 and arr[mid]>arr[mid+1]):
          return arr[mid]
 
    if (mid < high and arr[mid + 1] < arr[mid] and mid>0 and arr[mid]>arr[mid-1]):
        return arr[mid]
     
    if (arr[low] > arr[mid]):
        return findMax(arr, low, mid - 1)
    else:
        return findMax(arr, mid + 1, high)
 
def findLargest(L):
    n = len(L)
    return (findMax(L, 0, n - 1))